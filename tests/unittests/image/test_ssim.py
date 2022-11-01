# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import namedtuple
from functools import partial

import numpy as np
import pytest
import torch
from pytorch_msssim import ssim
from skimage.metrics import structural_similarity
from torch import Tensor

from torchmetrics.functional import structural_similarity_index_measure
from torchmetrics.image import StructuralSimilarityIndexMeasure
from unittests.helpers import seed_all
from unittests.helpers.testers import NUM_BATCHES, MetricTester

seed_all(42)

Input = namedtuple("Input", ["preds", "target"])

BATCH_SIZE = 2  # custom batch size to prevent memory issues in CI
_inputs = []
for size, channel, coef, dtype in [
    (12, 3, 0.9, torch.float),
    (13, 1, 0.8, torch.float32),
    (14, 1, 0.7, torch.double),
    (13, 3, 0.6, torch.float32),
]:
    preds2d = torch.rand(NUM_BATCHES, BATCH_SIZE, channel, size, size, dtype=dtype)
    _inputs.append(
        Input(
            preds=preds2d,
            target=preds2d * coef,
        )
    )
    preds3d = torch.rand(NUM_BATCHES, BATCH_SIZE, channel, size, size, size, dtype=dtype)
    _inputs.append(
        Input(
            preds=preds3d,
            target=preds3d * coef,
        )
    )


def _sk_ssim(
    preds,
    target,
    data_range,
    sigma,
    kernel_size=None,
    return_ssim_image=False,
    gaussian_weights=True,
    reduction_arg="elementwise_mean",
):
    if len(preds.shape) == 4:
        c, h, w = preds.shape[-3:]
        sk_preds = preds.view(-1, c, h, w).permute(0, 2, 3, 1).numpy()
        sk_target = target.view(-1, c, h, w).permute(0, 2, 3, 1).numpy()
    elif len(preds.shape) == 5:
        c, d, h, w = preds.shape[-4:]
        sk_preds = preds.view(-1, c, d, h, w).permute(0, 2, 3, 4, 1).numpy()
        sk_target = target.view(-1, c, d, h, w).permute(0, 2, 3, 4, 1).numpy()

    results = torch.zeros(sk_preds.shape[0], dtype=target.dtype)
    if not return_ssim_image:
        for i in range(sk_preds.shape[0]):
            res = structural_similarity(
                sk_target[i],
                sk_preds[i],
                data_range=data_range,
                multichannel=True,
                gaussian_weights=gaussian_weights,
                win_size=kernel_size,
                sigma=sigma,
                use_sample_covariance=False,
                full=return_ssim_image,
            )
            results[i] = torch.from_numpy(np.asarray(res)).type(preds.dtype)
        return results if reduction_arg != "sum" else results.sum()
    else:
        fullimages = torch.zeros(target.shape, dtype=target.dtype)
        for i in range(sk_preds.shape[0]):
            res, fullimage = structural_similarity(
                sk_target[i],
                sk_preds[i],
                data_range=data_range,
                multichannel=True,
                gaussian_weights=gaussian_weights,
                win_size=kernel_size,
                sigma=sigma,
                use_sample_covariance=False,
                full=return_ssim_image,
            )
            results[i] = torch.from_numpy(res).type(preds.dtype)
            fullimage = torch.from_numpy(fullimage).type(preds.dtype)
            if len(preds.shape) == 4:
                fullimages[i] = fullimage.permute(2, 0, 1)
            elif len(preds.shape) == 5:
                fullimages[i] = fullimage.permute(3, 0, 1, 2)
        return results, fullimages


def _pt_ssim(
    preds,
    target,
    data_range,
    sigma,
    kernel_size=11,
    reduction_arg="elementwise_mean",
):
    results = ssim(target, preds, data_range=data_range, win_size=kernel_size, win_sigma=sigma, size_average=False)

    return results if reduction_arg != "sum" else results.sum()


@pytest.mark.parametrize(
    "preds, target",
    [(i.preds, i.target) for i in _inputs],
)
@pytest.mark.parametrize("sigma", [1.5, 0.5])
class TestSSIM(MetricTester):
    atol = 6e-3

    @pytest.mark.parametrize("ddp", [True, False])
    @pytest.mark.parametrize("dist_sync_on_step", [True, False])
    def test_ssim_sk(self, preds, target, sigma, ddp, dist_sync_on_step):
        self.run_class_metric_test(
            ddp,
            preds,
            target,
            StructuralSimilarityIndexMeasure,
            partial(_sk_ssim, data_range=1.0, sigma=sigma, kernel_size=None),
            metric_args={
                "data_range": 1.0,
                "sigma": sigma,
            },
            dist_sync_on_step=dist_sync_on_step,
        )

    @pytest.mark.parametrize("ddp", [True, False])
    @pytest.mark.parametrize("dist_sync_on_step", [True, False])
    def test_ssim_pt(self, preds, target, sigma, ddp, dist_sync_on_step):
        self.run_class_metric_test(
            ddp,
            preds,
            target,
            StructuralSimilarityIndexMeasure,
            partial(_pt_ssim, data_range=1.0, sigma=sigma),
            metric_args={
                "data_range": 1.0,
                "sigma": sigma,
            },
            dist_sync_on_step=dist_sync_on_step,
        )

    @pytest.mark.parametrize("ddp", [True, False])
    @pytest.mark.parametrize("dist_sync_on_step", [True, False])
    def test_ssim_without_gaussian_kernel(self, preds, target, sigma, ddp, dist_sync_on_step):
        self.run_class_metric_test(
            ddp,
            preds,
            target,
            StructuralSimilarityIndexMeasure,
            partial(_sk_ssim, data_range=1.0, sigma=sigma, kernel_size=None),
            metric_args={
                "gaussian_kernel": False,
                "data_range": 1.0,
                "sigma": sigma,
            },
            dist_sync_on_step=dist_sync_on_step,
        )

    @pytest.mark.parametrize("reduction_arg", ["sum", "elementwise_mean", None])
    def test_ssim_functional_sk(self, preds, target, sigma, reduction_arg):
        self.run_functional_metric_test(
            preds,
            target,
            structural_similarity_index_measure,
            partial(_sk_ssim, data_range=1.0, sigma=sigma, kernel_size=None, reduction_arg=reduction_arg),
            metric_args={"data_range": 1.0, "sigma": sigma, "reduction": reduction_arg},
        )

    @pytest.mark.parametrize("reduction_arg", ["sum", "elementwise_mean", None])
    def test_ssim_functional_pt(self, preds, target, sigma, reduction_arg):
        self.run_functional_metric_test(
            preds,
            target,
            structural_similarity_index_measure,
            partial(_pt_ssim, data_range=1.0, sigma=sigma, reduction_arg=reduction_arg),
            metric_args={"data_range": 1.0, "sigma": sigma, "reduction": reduction_arg},
        )

    # SSIM half + cpu does not work due to missing support in torch.log
    @pytest.mark.xfail(reason="SSIM metric does not support cpu + half precision")
    def test_ssim_half_cpu(self, preds, target, sigma):
        self.run_precision_test_cpu(
            preds, target, StructuralSimilarityIndexMeasure, structural_similarity_index_measure, {"data_range": 1.0}
        )

    @pytest.mark.skipif(not torch.cuda.is_available(), reason="test requires cuda")
    def test_ssim_half_gpu(self, preds, target, sigma):
        self.run_precision_test_gpu(
            preds, target, StructuralSimilarityIndexMeasure, structural_similarity_index_measure, {"data_range": 1.0}
        )


@pytest.mark.parametrize(
    ["pred", "target", "kernel", "sigma"],
    [
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, 11], [1.5]),  # len(kernel), len(sigma)
        ([1, 16, 16], [1, 16, 16], [11, 11], [1.5, 1.5]),  # len(shape)
        ([1, 1, 16, 16], [1, 1, 16, 16], [11], [1.5, 1.5]),  # len(kernel), len(sigma)
        ([1, 1, 16, 16], [1, 1, 16, 16], [11], [1.5]),  # len(kernel), len(sigma)
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, 0], [1.5, 1.5]),  # invalid kernel input
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, 10], [1.5, 1.5]),  # invalid kernel input
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, -11], [1.5, 1.5]),  # invalid kernel input
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, 11], [1.5, 0]),  # invalid sigma input
        ([1, 1, 16, 16], [1, 1, 16, 16], [11, 0], [1.5, -1.5]),  # invalid sigma input
    ],
)
def test_ssim_invalid_inputs(pred, target, kernel, sigma):
    pred_t = torch.rand(pred, dtype=torch.float32)
    target_t = torch.rand(target, dtype=torch.float64)
    with pytest.raises(TypeError):
        structural_similarity_index_measure(pred_t, target_t)

    pred = torch.rand(pred)
    target = torch.rand(target)
    with pytest.raises(ValueError):
        structural_similarity_index_measure(pred, target, kernel_size=kernel, sigma=sigma)


def test_ssim_unequal_kernel_size():
    """Test the case where kernel_size[0] != kernel_size[1]"""
    preds = torch.tensor(
        [
            [
                [
                    [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
                    [1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
                    [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
                ]
            ]
        ]
    )
    target = torch.tensor(
        [
            [
                [
                    [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
                    [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
                    [1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                    [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0],
                    [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
                ]
            ]
        ]
    )
    # kernel order matters
    assert torch.isclose(
        structural_similarity_index_measure(preds, target, gaussian_kernel=True, sigma=(0.25, 0.5)),
        torch.tensor(0.08869550),
    )
    assert not torch.isclose(
        structural_similarity_index_measure(preds, target, gaussian_kernel=True, sigma=(0.5, 0.25)),
        torch.tensor(0.08869550),
    )

    assert torch.isclose(
        structural_similarity_index_measure(preds, target, gaussian_kernel=False, kernel_size=(3, 5)),
        torch.tensor(0.05131844),
    )
    assert not torch.isclose(
        structural_similarity_index_measure(preds, target, gaussian_kernel=False, kernel_size=(5, 3)),
        torch.tensor(0.05131844),
    )


@pytest.mark.parametrize(
    "preds, target",
    [(i.preds, i.target) for i in _inputs],
)
def test_full_image_output(preds, target):
    out = structural_similarity_index_measure(preds[0], target[0])
    assert isinstance(out, Tensor)
    assert out.numel() == 1

    out = structural_similarity_index_measure(preds[0], target[0], return_full_image=True)
    assert isinstance(out, tuple)
    assert len(out) == 2
    assert out[0].numel() == 1
    assert out[1].shape == preds[0].shape
