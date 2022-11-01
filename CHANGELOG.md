# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Note: we move fast, but still we preserve 0.1 version (one feature release) back compatibility.**


## [unReleased] - 2022-MM-DD

### Added

- Added `TotalVariation` to image package ([#978](https://github.com/Lightning-AI/metrics/pull/978))

- Added option to pass `distributed_available_fn` to metrics to allow checks for custom communication backend for making `dist_sync_fn` actually useful ([#1301](https://github.com/Lightning-AI/metrics/pull/1301))


### Changed

- Changed `MeanAveragePrecision` to vectorize `_find_best_gt_match` operation ([#1259](https://github.com/Lightning-AI/metrics/pull/1259))


- Changed minimum Pytorch version to be 1.8 ([#1263](https://github.com/Lightning-AI/metrics/pull/1263))


- Changed in-place operation to out-of-place operation in `pairwise_cosine_similarity` ([#1288](https://github.com/Lightning-AI/metrics/pull/1288))


### Deprecated

-


### Removed

- Removed deprecated `BinnedAveragePrecision`, `BinnedPrecisionRecallCurve`, `RecallAtFixedPrecision` ([#1251](https://github.com/Lightning-AI/metrics/pull/1251))
- Removed deprecated `LabelRankingAveragePrecision`, `LabelRankingLoss` and `CoverageError` ([#1251](https://github.com/Lightning-AI/metrics/pull/1251))
- Removed deprecated `KLDivergence` and `AUC` ([#1251](https://github.com/Lightning-AI/metrics/pull/1251))

### Fixed

- Fixed high memory usage for certain classification metrics when `average='micro'` ([#1286](https://github.com/Lightning-AI/metrics/pull/1286))


- Fixed precision problems when `structural_similarity_index_measure` was used with autocast ([#1291](https://github.com/Lightning-AI/metrics/pull/1291))


- Fixed slow performance for confusion matrix based metrics ([#1302](https://github.com/Lightning-AI/metrics/pull/1302))


- Fixed restrictive dtype checking in `spearman_corrcoef` when used with autocast ([#1303](https://github.com/Lightning-AI/metrics/pull/1303))


## [0.10.1] - 2022-10-21

### Fixed

- Fixed broken clone method for classification metrics ([#1250](https://github.com/Lightning-AI/metrics/pull/1250))
- Fixed unintentional downloading of `nltk.punkt` when `lsum` not in `rouge_keys` ([#1258](https://github.com/Lightning-AI/metrics/pull/1258))
- Fixed type casting in `MAP` metric between `bool` and `float32` ([#1150](https://github.com/Lightning-AI/metrics/pull/1150))


## [0.10.0] - 2022-10-04

### Added

- Added a new NLP metric `InfoLM` ([#915](https://github.com/Lightning-AI/metrics/pull/915))
- Added `Perplexity` metric ([#922](https://github.com/Lightning-AI/metrics/pull/922))
- Added `ConcordanceCorrCoef` metric to regression package ([#1201](https://github.com/Lightning-AI/metrics/pull/1201))
- Added argument `normalize` to `LPIPS` metric ([#1216](https://github.com/Lightning-AI/metrics/pull/1216))
- Added support for multiprocessing of batches in `PESQ` metric ([#1227](https://github.com/Lightning-AI/metrics/pull/1227))
- Added support for multioutput in `PearsonCorrCoef` and `SpearmanCorrCoef` ([#1200](https://github.com/Lightning-AI/metrics/pull/1200))

### Changed

- Classification refactor (
    [#1054](https://github.com/Lightning-AI/metrics/pull/1054),
    [#1143](https://github.com/Lightning-AI/metrics/pull/1143),
    [#1145](https://github.com/Lightning-AI/metrics/pull/1145),
    [#1151](https://github.com/Lightning-AI/metrics/pull/1151),
    [#1159](https://github.com/Lightning-AI/metrics/pull/1159),
    [#1163](https://github.com/Lightning-AI/metrics/pull/1163),
    [#1167](https://github.com/Lightning-AI/metrics/pull/1167),
    [#1175](https://github.com/Lightning-AI/metrics/pull/1175),
    [#1189](https://github.com/Lightning-AI/metrics/pull/1189),
    [#1197](https://github.com/Lightning-AI/metrics/pull/1197),
    [#1215](https://github.com/Lightning-AI/metrics/pull/1215),
    [#1195](https://github.com/Lightning-AI/metrics/pull/1195)
)
- Changed update in `FID` metric to be done in online fashion to save memory ([#1199](https://github.com/Lightning-AI/metrics/pull/1199))
- Improved performance of retrieval metrics ([#1242](https://github.com/Lightning-AI/metrics/pull/1242))
- Changed `SSIM` and `MSSSIM` update to be online to reduce memory usage ([#1231](https://github.com/Lightning-AI/metrics/pull/1231))

### Deprecated

- Deprecated `BinnedAveragePrecision`, `BinnedPrecisionRecallCurve`, `BinnedRecallAtFixedPrecision` ([#1163](https://github.com/Lightning-AI/metrics/pull/1163))
  * `BinnedAveragePrecision` -> use `AveragePrecision` with `thresholds` arg
  * `BinnedPrecisionRecallCurve` -> use `AveragePrecisionRecallCurve` with `thresholds` arg
  * `BinnedRecallAtFixedPrecision` -> use `RecallAtFixedPrecision` with `thresholds` arg
- Renamed and refactored `LabelRankingAveragePrecision`, `LabelRankingLoss` and `CoverageError` ([#1167](https://github.com/Lightning-AI/metrics/pull/1167))
  * `LabelRankingAveragePrecision` -> `MultilabelRankingAveragePrecision`
  * `LabelRankingLoss` -> `MultilabelRankingLoss`
  * `CoverageError` -> `MultilabelCoverageError`
- Deprecated `KLDivergence` and `AUC` from classification package ([#1189](https://github.com/Lightning-AI/metrics/pull/1189))
  * `KLDivergence` moved to `regression` package
  * Instead of `AUC` use `torchmetrics.utils.compute.auc`

### Fixed

- Fixed a bug in `ssim` when `return_full_image=True` where the score was still reduced ([#1204](https://github.com/Lightning-AI/metrics/pull/1204))
- Fixed MPS support for:
  * MAE metric ([#1210](https://github.com/Lightning-AI/metrics/pull/1210))
  * Jaccard index ([#1205](https://github.com/Lightning-AI/metrics/pull/1205))
- Fixed bug in `ClasswiseWrapper` such that `compute` gave wrong result ([#1225](https://github.com/Lightning-AI/metrics/pull/1225))
- Fixed synchronization of empty list states ([#1219](https://github.com/Lightning-AI/metrics/pull/1219))


## [0.9.3] - 2022-08-22

### Added

- Added global option `sync_on_compute` to disable automatic synchronization when `compute` is called ([#1107](https://github.dev/Lightning-AI/metrics/pull/1107))

### Fixed

- Fixed missing reset in `ClasswiseWrapper` ([#1129](https://github.com/Lightning-AI/metrics/pull/1129))
- Fixed `JaccardIndex` multi-label compute ([#1125](https://github.com/Lightning-AI/metrics/pull/1125))
- Fix SSIM propagate device if `gaussian_kernel` is False, add test ([#1149](https://github.com/Lightning-AI/metrics/pull/1149))


## [0.9.2] - 2022-06-29

### Fixed

- Fixed mAP calculation for areas with 0 predictions ([#1080](https://github.com/Lightning-AI/metrics/pull/1080))
- Fixed bug where avg precision state and auroc state was not merge when using MetricCollections ([#1086](https://github.com/Lightning-AI/metrics/pull/1086))
- Skip box conversion if no boxes are present in `MeanAveragePrecision` ([#1097](https://github.com/Lightning-AI/metrics/pull/1097))
- Fixed inconsistency in docs and code when setting `average="none"` in `AvaragePrecision` metric ([#1116](https://github.com/Lightning-AI/metrics/pull/1116))


## [0.9.1] - 2022-06-08

### Added

- Added specific `RuntimeError` when metric object is on the wrong device ([#1056](https://github.com/Lightning-AI/metrics/pull/1056))
- Added an option to specify own n-gram weights for `BLEUScore` and `SacreBLEUScore` instead of using uniform weights only. ([#1075](https://github.com/Lightning-AI/metrics/pull/1075))

### Fixed

- Fixed aggregation metrics when input only contains zero ([#1070](https://github.com/Lightning-AI/metrics/pull/1070))
- Fixed `TypeError` when providing superclass arguments as `kwargs` ([#1069](https://github.com/Lightning-AI/metrics/pull/1069))
- Fixed bug related to state reference in metric collection when using compute groups ([#1076](https://github.com/Lightning-AI/metrics/pull/1076))


## [0.9.0] - 2022-05-30

### Added

- Added `RetrievalPrecisionRecallCurve` and `RetrievalRecallAtFixedPrecision` to retrieval package ([#951](https://github.com/Lightning-AI/metrics/pull/951))
- Added class property `full_state_update` that determines `forward` should call `update` once or twice (
    [#984](https://github.com/Lightning-AI/metrics/pull/984),
    [#1033](https://github.com/Lightning-AI/metrics/pull/1033))
- Added support for nested metric collections ([#1003](https://github.com/Lightning-AI/metrics/pull/1003))
- Added `Dice` to classification package ([#1021](https://github.com/Lightning-AI/metrics/pull/1021))
- Added support to segmentation type `segm` as IOU for mean average precision ([#822](https://github.com/Lightning-AI/metrics/pull/822))

### Changed

- Renamed `reduction` argument to `average` in Jaccard score and added additional options ([#874](https://github.com/Lightning-AI/metrics/pull/874))

### Removed

- Removed deprecated `compute_on_step` argument (
    [#962](https://github.com/Lightning-AI/metrics/pull/962),
    [#967](https://github.com/Lightning-AI/metrics/pull/967),
    [#979](https://github.com/Lightning-AI/metrics/pull/979),
    [#990](https://github.com/Lightning-AI/metrics/pull/990),
    [#991](https://github.com/Lightning-AI/metrics/pull/991),
    [#993](https://github.com/Lightning-AI/metrics/pull/993),
    [#1005](https://github.com/Lightning-AI/metrics/pull/1005),
    [#1004](https://github.com/Lightning-AI/metrics/pull/1004),
    [#1007](https://github.com/Lightning-AI/metrics/pull/1007)
)

### Fixed

- Fixed non-empty state dict for a few metrics ([#1012](https://github.com/Lightning-AI/metrics/pull/1012))
- Fixed bug when comparing states while finding compute groups ([#1022](https://github.com/Lightning-AI/metrics/pull/1022))
- Fixed `torch.double` support in stat score metrics ([#1023](https://github.com/Lightning-AI/metrics/pull/1023))
- Fixed `FID` calculation for non-equal size real and fake input ([#1028](https://github.com/Lightning-AI/metrics/pull/1028))
- Fixed case where `KLDivergence` could output `Nan` ([#1030](https://github.com/Lightning-AI/metrics/pull/1030))
- Fixed deterministic for PyTorch<1.8 ([#1035](https://github.com/Lightning-AI/metrics/pull/1035))
- Fixed default value for `mdmc_average` in `Accuracy` ([#1036](https://github.com/Lightning-AI/metrics/pull/1036))
- Fixed missing copy of property when using compute groups in `MetricCollection` ([#1052](https://github.com/Lightning-AI/metrics/pull/1052))


## [0.8.2] - 2022-05-06


### Fixed

- Fixed multi device aggregation in `PearsonCorrCoef` ([#998](https://github.com/Lightning-AI/metrics/pull/998))
- Fixed MAP metric when using custom list of thresholds ([#995](https://github.com/Lightning-AI/metrics/pull/995))
- Fixed compatibility between compute groups in `MetricCollection` and prefix/postfix arg ([#1007](https://github.com/Lightning-AI/metrics/pull/1008))
- Fixed compatibility with future Pytorch 1.12 in `safe_matmul` ([#1011](https://github.com/Lightning-AI/metrics/pull/1011), [#1014](https://github.com/Lightning-AI/metrics/pull/1014))


## [0.8.1] - 2022-04-27

### Changed

- Reimplemented the `signal_distortion_ratio` metric, which removed the absolute requirement of `fast-bss-eval` ([#964](https://github.com/Lightning-AI/metrics/pull/964))

### Fixed

- Fixed "Sort currently does not support bool dtype on CUDA" error in MAP for empty preds ([#983](https://github.com/Lightning-AI/metrics/pull/983))
- Fixed `BinnedPrecisionRecallCurve` when `thresholds` argument is not provided ([#968](https://github.com/Lightning-AI/metrics/pull/968))
- Fixed `CalibrationError` to work on logit input ([#985](https://github.com/Lightning-AI/metrics/pull/985))


## [0.8.0] - 2022-04-14

### Added

- Added `WeightedMeanAbsolutePercentageError` to regression package ([#948](https://github.com/Lightning-AI/metrics/pull/948))
- Added new classification metrics:
  * `CoverageError` ([#787](https://github.com/Lightning-AI/metrics/pull/787))
  * `LabelRankingAveragePrecision` and `LabelRankingLoss` ([#787](https://github.com/Lightning-AI/metrics/pull/787))
- Added new image metric:
  * `SpectralAngleMapper` ([#885](https://github.com/Lightning-AI/metrics/pull/885))
  * `ErrorRelativeGlobalDimensionlessSynthesis` ([#894](https://github.com/Lightning-AI/metrics/pull/894))
  * `UniversalImageQualityIndex` ([#824](https://github.com/Lightning-AI/metrics/pull/824))
  * `SpectralDistortionIndex` ([#873](https://github.com/Lightning-AI/metrics/pull/873))
- Added support for `MetricCollection` in `MetricTracker` ([#718](https://github.com/Lightning-AI/metrics/pull/718))
- Added support for 3D image and uniform kernel in `StructuralSimilarityIndexMeasure` ([#818](https://github.com/Lightning-AI/metrics/pull/818))
- Added smart update of `MetricCollection` ([#709](https://github.com/Lightning-AI/metrics/pull/709))
- Added `ClasswiseWrapper` for better logging of classification metrics with multiple output values ([#832](https://github.com/Lightning-AI/metrics/pull/832))
- Added `**kwargs` argument for passing additional arguments to base class ([#833](https://github.com/Lightning-AI/metrics/pull/833))
- Added negative `ignore_index` for the Accuracy metric ([#362](https://github.com/Lightning-AI/metrics/pull/362))
- Added `adaptive_k` for the `RetrievalPrecision` metric ([#910](https://github.com/Lightning-AI/metrics/pull/910))
- Added `reset_real_features` argument image quality assessment metrics ([#722](https://github.com/Lightning-AI/metrics/pull/722))
- Added new keyword argument `compute_on_cpu` to all metrics ([#867](https://github.com/Lightning-AI/metrics/pull/867))

### Changed

- Made `num_classes` in `jaccard_index` a required argument ([#853](https://github.com/Lightning-AI/metrics/pull/853), [#914](https://github.com/Lightning-AI/metrics/pull/914))
- Added normalizer, tokenizer to ROUGE metric ([#838](https://github.com/Lightning-AI/metrics/pull/838))
- Improved shape checking of `permutation_invariant_training` ([#864](https://github.com/Lightning-AI/metrics/pull/864))
- Allowed reduction `None` ([#891](https://github.com/Lightning-AI/metrics/pull/891))
- `MetricTracker.best_metric` will now give a warning when computing on metric that do not have a best ([#913](https://github.com/Lightning-AI/metrics/pull/913))

### Deprecated

- Deprecated argument `compute_on_step` ([#792](https://github.com/Lightning-AI/metrics/pull/792))
- Deprecated passing in `dist_sync_on_step`, `process_group`, `dist_sync_fn` direct argument ([#833](https://github.com/Lightning-AI/metrics/pull/833))

### Removed

- Removed support for versions of [Pytorch-Lightning](https://github.com/PyTorchLightning/pytorch-lightning) lower than v1.5 ([#788](https://github.com/Lightning-AI/metrics/pull/788))
- Removed deprecated functions, and warnings in Text ([#773](https://github.com/Lightning-AI/metrics/pull/773))
  * `WER` and `functional.wer`
- Removed deprecated functions and warnings in Image ([#796](https://github.com/Lightning-AI/metrics/pull/796))
  * `SSIM` and `functional.ssim`
  * `PSNR` and `functional.psnr`
- Removed deprecated functions, and warnings in classification and regression ([#806](https://github.com/Lightning-AI/metrics/pull/806))
  * `FBeta` and `functional.fbeta`
  * `F1` and `functional.f1`
  * `Hinge` and `functional.hinge`
  * `IoU` and `functional.iou`
  * `MatthewsCorrcoef`
  * `PearsonCorrcoef`
  * `SpearmanCorrcoef`
- Removed deprecated functions, and warnings in detection and pairwise ([#804](https://github.com/Lightning-AI/metrics/pull/804))
  * `MAP` and `functional.pairwise.manhatten`
- Removed deprecated functions, and warnings in Audio ([#805](https://github.com/Lightning-AI/metrics/pull/805))
  * `PESQ` and `functional.audio.pesq`
  * `PIT` and `functional.audio.pit`
  * `SDR` and `functional.audio.sdr` and `functional.audio.si_sdr`
  * `SNR` and `functional.audio.snr` and `functional.audio.si_snr`
  * `STOI` and `functional.audio.stoi`
- Removed unused `get_num_classes` from `torchmetrics.utilities.data` ([#914](https://github.com/Lightning-AI/metrics/pull/914))

### Fixed

- Fixed device mismatch for `MAP` metric in specific cases ([#950](https://github.com/Lightning-AI/metrics/pull/950))
- Improved testing speed ([#820](https://github.com/Lightning-AI/metrics/pull/820))
- Fixed compatibility of `ClasswiseWrapper` with the `prefix` argument of `MetricCollection` ([#843](https://github.com/Lightning-AI/metrics/pull/843))
- Fixed `BestScore` on GPU ([#912](https://github.com/Lightning-AI/metrics/pull/912))
- Fixed Lsum computation for `ROUGEScore` ([#944](https://github.com/Lightning-AI/metrics/pull/944))


## [0.7.3] - 2022-03-23

### Fixed

- Fixed unsafe log operation in `TweedieDeviace` for power=1 ([#847](https://github.com/Lightning-AI/metrics/pull/847))
- Fixed bug in MAP metric related to either no ground truth or no predictions ([#884](https://github.com/Lightning-AI/metrics/pull/884))
- Fixed `ConfusionMatrix`, `AUROC` and `AveragePrecision` on GPU when running in deterministic mode ([#900](https://github.com/Lightning-AI/metrics/pull/900))
- Fixed NaN or Inf results returned by `signal_distortion_ratio` ([#899](https://github.com/Lightning-AI/metrics/pull/899))
- Fixed memory leak when using `update` method with tensor where `requires_grad=True` ([#902](https://github.com/Lightning-AI/metrics/pull/902))


## [0.7.2] - 2022-02-10

### Fixed

- Minor patches in JOSS paper.


## [0.7.1] - 2022-02-03

### Changed

- Used `torch.bucketize` in calibration error when `torch>1.8` for faster computations ([#769](https://github.com/Lightning-AI/metrics/pull/769))
- Improve mAP performance ([#742](https://github.com/Lightning-AI/metrics/pull/742))

### Fixed

- Fixed check for available modules ([#772](https://github.com/Lightning-AI/metrics/pull/772))
- Fixed Matthews correlation coefficient when the denominator is 0 ([#781](https://github.com/Lightning-AI/metrics/pull/781))


## [0.7.0] - 2022-01-17

### Added

- Added NLP metrics:
  - `MatchErrorRate` ([#619](https://github.com/Lightning-AI/metrics/pull/619))
  - `WordInfoLost` and `WordInfoPreserved` ([#630](https://github.com/Lightning-AI/metrics/pull/630))
  - `SQuAD` ([#623](https://github.com/Lightning-AI/metrics/pull/623))
  - `CHRFScore` ([#641](https://github.com/Lightning-AI/metrics/pull/641))
  - `TranslationEditRate` ([#646](https://github.com/Lightning-AI/metrics/pull/646))
  - `ExtendedEditDistance` ([#668](https://github.com/Lightning-AI/metrics/pull/668))
- Added `MultiScaleSSIM` into image metrics ([#679](https://github.com/Lightning-AI/metrics/pull/679))
- Added Signal to Distortion Ratio (`SDR`) to audio package ([#565](https://github.com/Lightning-AI/metrics/pull/565))
- Added `MinMaxMetric` to wrappers ([#556](https://github.com/Lightning-AI/metrics/pull/556))
- Added `ignore_index` to retrieval metrics ([#676](https://github.com/Lightning-AI/metrics/pull/676))
- Added support for multi references in `ROUGEScore` ([#680](https://github.com/Lightning-AI/metrics/pull/680))
- Added a default VSCode devcontainer configuration ([#621](https://github.com/Lightning-AI/metrics/pull/621))

### Changed

- Scalar metrics will now consistently have additional dimensions squeezed ([#622](https://github.com/Lightning-AI/metrics/pull/622))
- Metrics having third party dependencies removed from global import ([#463](https://github.com/Lightning-AI/metrics/pull/463))
- Untokenized for `BLEUScore` input stay consistent with all the other text metrics ([#640](https://github.com/Lightning-AI/metrics/pull/640))
- Arguments reordered for `TER`, `BLEUScore`, `SacreBLEUScore`, `CHRFScore` now expect input order as predictions first and target second ([#696](https://github.com/Lightning-AI/metrics/pull/696))
- Changed dtype of metric state from `torch.float` to `torch.long` in `ConfusionMatrix` to accommodate larger values ([#715](https://github.com/Lightning-AI/metrics/pull/715))
- Unify `preds`, `target` input argument's naming across all text metrics ([#723](https://github.com/Lightning-AI/metrics/pull/723), [#727](https://github.com/Lightning-AI/metrics/pull/727))
  * `bert`, `bleu`, `chrf`, `sacre_bleu`, `wip`, `wil`, `cer`, `ter`, `wer`, `mer`, `rouge`, `squad`

### Deprecated

- Renamed IoU -> Jaccard Index ([#662](https://github.com/Lightning-AI/metrics/pull/662))
- Renamed text WER metric ([#714](https://github.com/Lightning-AI/metrics/pull/714))
  * `functional.wer` -> `functional.word_error_rate`
  * `WER` -> `WordErrorRate`
- Renamed correlation coefficient classes: ([#710](https://github.com/Lightning-AI/metrics/pull/710))
  * `MatthewsCorrcoef` -> `MatthewsCorrCoef`
  * `PearsonCorrcoef` -> `PearsonCorrCoef`
  * `SpearmanCorrcoef` -> `SpearmanCorrCoef`
- Renamed audio STOI metric: ([#753](https://github.com/Lightning-AI/metrics/pull/753), [#758](https://github.com/Lightning-AI/metrics/pull/758))
  * `audio.STOI` to `audio.ShortTimeObjectiveIntelligibility`
  * `functional.audio.stoi` to `functional.audio.short_time_objective_intelligibility`
- Renamed audio PESQ metrics: ([#751](https://github.com/Lightning-AI/metrics/pull/751))
  * `functional.audio.pesq` -> `functional.audio.perceptual_evaluation_speech_quality`
  * `audio.PESQ` -> `audio.PerceptualEvaluationSpeechQuality`
- Renamed audio SDR metrics: ([#711](https://github.com/Lightning-AI/metrics/pull/711))
  * `functional.sdr` -> `functional.signal_distortion_ratio`
  * `functional.si_sdr` -> `functional.scale_invariant_signal_distortion_ratio`
  * `SDR` -> `SignalDistortionRatio`
  * `SI_SDR` -> `ScaleInvariantSignalDistortionRatio`
- Renamed audio SNR metrics: ([#712](https://github.com/Lightning-AI/metrics/pull/712))
  * `functional.snr` -> `functional.signal_distortion_ratio`
  * `functional.si_snr` -> `functional.scale_invariant_signal_noise_ratio`
  * `SNR` -> `SignalNoiseRatio`
  * `SI_SNR` -> `ScaleInvariantSignalNoiseRatio`
- Renamed F-score metrics: ([#731](https://github.com/Lightning-AI/metrics/pull/731), [#740](https://github.com/Lightning-AI/metrics/pull/740))
  * `functional.f1` ->  `functional.f1_score`
  * `F1` ->  `F1Score`
  * `functional.fbeta` ->  `functional.fbeta_score`
  * `FBeta` ->  `FBetaScore`
- Renamed Hinge metric: ([#734](https://github.com/Lightning-AI/metrics/pull/734))
  * `functional.hinge` ->  `functional.hinge_loss`
  * `Hinge` ->  `HingeLoss`
- Renamed image PSNR metrics ([#732](https://github.com/Lightning-AI/metrics/pull/732))
  * `functional.psnr` -> `functional.peak_signal_noise_ratio`
  * `PSNR` -> `PeakSignalNoiseRatio`
- Renamed image PIT metric: ([#737](https://github.com/Lightning-AI/metrics/pull/737))
  * `functional.pit` ->  `functional.permutation_invariant_training`
  * `PIT` ->  `PermutationInvariantTraining`
- Renamed image SSIM metric: ([#747](https://github.com/Lightning-AI/metrics/pull/747))
  * `functional.ssim` ->  `functional.scale_invariant_signal_noise_ratio`
  * `SSIM` ->  `StructuralSimilarityIndexMeasure`
- Renamed detection `MAP` to `MeanAveragePrecision` metric ([#754](https://github.com/Lightning-AI/metrics/pull/754))
- Renamed Fidelity & LPIPS image metric: ([#752](https://github.com/Lightning-AI/metrics/pull/752))
  * `image.FID` ->  `image.FrechetInceptionDistance`
  * `image.KID` ->  `image.KernelInceptionDistance`
  * `image.LPIPS` ->  `image.LearnedPerceptualImagePatchSimilarity`

### Removed

- Removed `embedding_similarity` metric ([#638](https://github.com/Lightning-AI/metrics/pull/638))
- Removed argument `concatenate_texts` from `wer` metric ([#638](https://github.com/Lightning-AI/metrics/pull/638))
- Removed arguments `newline_sep` and `decimal_places` from `rouge` metric ([#638](https://github.com/Lightning-AI/metrics/pull/638))

### Fixed

- Fixed MetricCollection kwargs filtering when no `kwargs` are present in update signature ([#707](https://github.com/Lightning-AI/metrics/pull/707))


## [0.6.2] - 2021-12-15

### Fixed

- Fixed `torch.sort` currently does not support bool `dtype` on CUDA ([#665](https://github.com/Lightning-AI/metrics/pull/665))
- Fixed mAP properly checks if ground truths are empty ([#684](https://github.com/Lightning-AI/metrics/pull/684))
- Fixed initialization of tensors to be on correct device for `MAP` metric ([#673](https://github.com/Lightning-AI/metrics/pull/673))


## [0.6.1] - 2021-12-06

### Changed

- Migrate MAP metrics from pycocotools to PyTorch ([#632](https://github.com/Lightning-AI/metrics/pull/632))
- Use `torch.topk` instead of `torch.argsort` in retrieval precision for speedup ([#627](https://github.com/Lightning-AI/metrics/pull/627))

### Fixed

- Fix empty predictions in MAP metric ([#594](https://github.com/Lightning-AI/metrics/pull/594), [#610](https://github.com/Lightning-AI/metrics/pull/610), [#624](https://github.com/Lightning-AI/metrics/pull/624))
- Fix edge case of AUROC with `average=weighted` on GPU ([#606](https://github.com/Lightning-AI/metrics/pull/606))
- Fixed `forward` in compositional metrics ([#645](https://github.com/Lightning-AI/metrics/pull/645))


## [0.6.0] - 2021-10-28

### Added

- Added audio metrics:
  - Perceptual Evaluation of Speech Quality (PESQ) ([#353](https://github.com/Lightning-AI/metrics/pull/353))
  - Short-Time Objective Intelligibility (STOI) ([#353](https://github.com/Lightning-AI/metrics/pull/353))
- Added Information retrieval metrics:
  - `RetrievalRPrecision` ([#577](https://github.com/Lightning-AI/metrics/pull/577))
  - `RetrievalHitRate` ([#576](https://github.com/Lightning-AI/metrics/pull/576))
- Added NLP metrics:
  - `SacreBLEUScore` ([#546](https://github.com/Lightning-AI/metrics/pull/546))
  - `CharErrorRate` ([#575](https://github.com/Lightning-AI/metrics/pull/575))
- Added other metrics:
  - Tweedie Deviance Score ([#499](https://github.com/Lightning-AI/metrics/pull/499))
  - Learned Perceptual Image Patch Similarity (LPIPS) ([#431](https://github.com/Lightning-AI/metrics/pull/431))
- Added `MAP` (mean average precision) metric to new detection package ([#467](https://github.com/Lightning-AI/metrics/pull/467))
- Added support for float targets in `nDCG` metric ([#437](https://github.com/Lightning-AI/metrics/pull/437))
- Added `average` argument to `AveragePrecision` metric for reducing multi-label and multi-class problems ([#477](https://github.com/Lightning-AI/metrics/pull/477))
- Added `MultioutputWrapper` ([#510](https://github.com/Lightning-AI/metrics/pull/510))
- Added metric sweeping:
  - `higher_is_better` as constant attribute ([#544](https://github.com/Lightning-AI/metrics/pull/544))
  - `higher_is_better` to rest of codebase ([#584](https://github.com/Lightning-AI/metrics/pull/584))
- Added simple aggregation metrics: `SumMetric`, `MeanMetric`, `CatMetric`, `MinMetric`, `MaxMetric` ([#506](https://github.com/Lightning-AI/metrics/pull/506))
- Added pairwise submodule with metrics ([#553](https://github.com/Lightning-AI/metrics/pull/553))
  - `pairwise_cosine_similarity`
  - `pairwise_euclidean_distance`
  - `pairwise_linear_similarity`
  - `pairwise_manhatten_distance`

### Changed

- `AveragePrecision` will now as default output the `macro` average for multilabel and multiclass problems ([#477](https://github.com/Lightning-AI/metrics/pull/477))
- `half`, `double`, `float` will no longer change the dtype of the metric states. Use `metric.set_dtype` instead ([#493](https://github.com/Lightning-AI/metrics/pull/493))
- Renamed `AverageMeter` to `MeanMetric` ([#506](https://github.com/Lightning-AI/metrics/pull/506))
- Changed `is_differentiable` from property to a constant attribute ([#551](https://github.com/Lightning-AI/metrics/pull/551))
- `ROC` and `AUROC` will no longer throw an error when either the positive or negative class is missing. Instead return 0 score and give a warning

### Deprecated

- Deprecated  `functional.self_supervised.embedding_similarity` in favour of new pairwise submodule

### Removed

- Removed `dtype` property ([#493](https://github.com/Lightning-AI/metrics/pull/493))

### Fixed

- Fixed bug in `F1` with `average='macro'` and `ignore_index!=None` ([#495](https://github.com/Lightning-AI/metrics/pull/495))
- Fixed bug in `pit` by using the returned first result to initialize device and type ([#533](https://github.com/Lightning-AI/metrics/pull/533))
- Fixed `SSIM` metric using too much memory ([#539](https://github.com/Lightning-AI/metrics/pull/539))
- Fixed bug where `device` property was not properly update when metric was a child of a module (#542)

## [0.5.1] - 2021-08-30

### Added

- Added `device` and `dtype` properties ([#462](https://github.com/Lightning-AI/metrics/pull/462))
- Added `TextTester` class for robustly testing text metrics ([#450](https://github.com/Lightning-AI/metrics/pull/450))

### Changed

- Added support for float targets in `nDCG` metric ([#437](https://github.com/Lightning-AI/metrics/pull/437))

### Removed

- Removed `rouge-score` as dependency for text package ([#443](https://github.com/Lightning-AI/metrics/pull/443))
- Removed `jiwer` as dependency for text package ([#446](https://github.com/Lightning-AI/metrics/pull/446))
- Removed `bert-score` as dependency for text package ([#473](https://github.com/Lightning-AI/metrics/pull/473))

### Fixed

- Fixed ranking of samples in `SpearmanCorrCoef` metric ([#448](https://github.com/Lightning-AI/metrics/pull/448))
- Fixed bug where compositional metrics where unable to sync because of type mismatch ([#454](https://github.com/Lightning-AI/metrics/pull/454))
- Fixed metric hashing ([#478](https://github.com/Lightning-AI/metrics/pull/478))
- Fixed `BootStrapper` metrics not working on GPU ([#462](https://github.com/Lightning-AI/metrics/pull/462))
- Fixed the semantic ordering of kernel height and width in `SSIM` metric ([#474](https://github.com/Lightning-AI/metrics/pull/474))


## [0.5.0] - 2021-08-09

### Added

- Added **Text-related (NLP) metrics**:
  - Word Error Rate (WER) ([#383](https://github.com/Lightning-AI/metrics/pull/383))
  - ROUGE ([#399](https://github.com/Lightning-AI/metrics/pull/399))
  - BERT score ([#424](https://github.com/Lightning-AI/metrics/pull/424))
  - BLUE score ([#360](https://github.com/Lightning-AI/metrics/pull/360))
- Added `MetricTracker` wrapper metric for keeping track of the same metric over multiple epochs ([#238](https://github.com/Lightning-AI/metrics/pull/238))
- Added other metrics:
  - Symmetric Mean Absolute Percentage error (SMAPE) ([#375](https://github.com/Lightning-AI/metrics/pull/375))
  - Calibration error ([#394](https://github.com/Lightning-AI/metrics/pull/394))
  - Permutation Invariant Training (PIT) ([#384](https://github.com/Lightning-AI/metrics/pull/384))
- Added support in `nDCG` metric for target with values larger than 1 ([#349](https://github.com/Lightning-AI/metrics/pull/349))
- Added support for negative targets in `nDCG` metric ([#378](https://github.com/Lightning-AI/metrics/pull/378))
- Added `None` as reduction option in `CosineSimilarity` metric ([#400](https://github.com/Lightning-AI/metrics/pull/400))
- Allowed passing labels in (n_samples, n_classes) to `AveragePrecision` ([#386](https://github.com/Lightning-AI/metrics/pull/386))

### Changed

- Moved `psnr` and `ssim` from `functional.regression.*` to `functional.image.*` ([#382](https://github.com/Lightning-AI/metrics/pull/382))
- Moved `image_gradient` from `functional.image_gradients` to `functional.image.gradients` ([#381](https://github.com/Lightning-AI/metrics/pull/381))
- Moved `R2Score` from `regression.r2score` to `regression.r2` ([#371](https://github.com/Lightning-AI/metrics/pull/371))
- Pearson metric now only store 6 statistics instead of all predictions and targets ([#380](https://github.com/Lightning-AI/metrics/pull/380))
- Use `torch.argmax` instead of `torch.topk` when `k=1` for better performance ([#419](https://github.com/Lightning-AI/metrics/pull/419))
- Moved check for number of samples in R2 score to support single sample updating ([#426](https://github.com/Lightning-AI/metrics/pull/426))

### Deprecated

- Rename `r2score` >> `r2_score` and `kldivergence` >> `kl_divergence` in `functional` ([#371](https://github.com/Lightning-AI/metrics/pull/371))
- Moved `bleu_score` from `functional.nlp` to `functional.text.bleu` ([#360](https://github.com/Lightning-AI/metrics/pull/360))

### Removed

- Removed restriction that `threshold` has to be in (0,1) range to support logit input (
    [#351](https://github.com/Lightning-AI/metrics/pull/351)
    [#401](https://github.com/Lightning-AI/metrics/pull/401))
- Removed restriction that `preds` could not be bigger than `num_classes` to support logit input ([#357](https://github.com/Lightning-AI/metrics/pull/357))
- Removed module `regression.psnr` and `regression.ssim` ([#382](https://github.com/Lightning-AI/metrics/pull/382)):
- Removed ([#379](https://github.com/Lightning-AI/metrics/pull/379)):
    * function `functional.mean_relative_error`
    * `num_thresholds` argument in `BinnedPrecisionRecallCurve`

### Fixed

- Fixed bug where classification metrics with `average='macro'` would lead to wrong result if a class was missing ([#303](https://github.com/Lightning-AI/metrics/pull/303))
- Fixed `weighted`, `multi-class` AUROC computation to allow for 0 observations of some class, as contribution to final AUROC is 0 ([#376](https://github.com/Lightning-AI/metrics/pull/376))
- Fixed that `_forward_cache` and `_computed` attributes are also moved to the correct device if metric is moved ([#413](https://github.com/Lightning-AI/metrics/pull/413))
- Fixed calculation in `IoU` metric when using `ignore_index` argument ([#328](https://github.com/Lightning-AI/metrics/pull/328))


## [0.4.1] - 2021-07-05

### Changed

- Extend typing ([#330](https://github.com/Lightning-AI/metrics/pull/330),
    [#332](https://github.com/Lightning-AI/metrics/pull/332),
    [#333](https://github.com/Lightning-AI/metrics/pull/333),
    [#335](https://github.com/Lightning-AI/metrics/pull/335),
    [#314](https://github.com/Lightning-AI/metrics/pull/314))

### Fixed

- Fixed DDP by `is_sync` logic to `Metric` ([#339](https://github.com/Lightning-AI/metrics/pull/339))


## [0.4.0] - 2021-06-29

### Added

- Added **Image-related metrics**:
  - Fréchet inception distance (FID) ([#213](https://github.com/Lightning-AI/metrics/pull/213))
  - Kernel Inception Distance (KID) ([#301](https://github.com/Lightning-AI/metrics/pull/301))
  - Inception Score ([#299](https://github.com/Lightning-AI/metrics/pull/299))
  - KL divergence ([#247](https://github.com/Lightning-AI/metrics/pull/247))
- Added **Audio metrics**: SNR, SI_SDR, SI_SNR ([#292](https://github.com/Lightning-AI/metrics/pull/292))
- Added other metrics:
  - Cosine Similarity ([#305](https://github.com/Lightning-AI/metrics/pull/305))
  - Specificity ([#210](https://github.com/Lightning-AI/metrics/pull/210))
  - Mean Absolute Percentage error (MAPE) ([#248](https://github.com/Lightning-AI/metrics/pull/248))
- Added `add_metrics` method to `MetricCollection` for adding additional metrics after initialization ([#221](https://github.com/Lightning-AI/metrics/pull/221))
- Added pre-gather reduction in the case of `dist_reduce_fx="cat"` to reduce communication cost ([#217](https://github.com/Lightning-AI/metrics/pull/217))
- Added better error message for `AUROC` when `num_classes` is not provided for multiclass input ([#244](https://github.com/Lightning-AI/metrics/pull/244))
- Added support for unnormalized scores (e.g. logits) in `Accuracy`, `Precision`, `Recall`, `FBeta`, `F1`, `StatScore`, `Hamming`, `ConfusionMatrix` metrics ([#200](https://github.com/Lightning-AI/metrics/pull/200))
- Added `squared` argument to `MeanSquaredError` for computing `RMSE` ([#249](https://github.com/Lightning-AI/metrics/pull/249))
- Added `is_differentiable` property to `ConfusionMatrix`, `F1`, `FBeta`, `Hamming`, `Hinge`, `IOU`, `MatthewsCorrcoef`, `Precision`, `Recall`, `PrecisionRecallCurve`, `ROC`, `StatScores` ([#253](https://github.com/Lightning-AI/metrics/pull/253))
- Added `sync` and `sync_context` methods for manually controlling when metric states are synced ([#302](https://github.com/Lightning-AI/metrics/pull/302))

### Changed

- Forward cache is reset when `reset` method is called ([#260](https://github.com/Lightning-AI/metrics/pull/260))
- Improved per-class metric handling for imbalanced datasets for `precision`, `recall`, `precision_recall`, `fbeta`, `f1`, `accuracy`, and `specificity` ([#204](https://github.com/Lightning-AI/metrics/pull/204))
- Decorated `torch.jit.unused` to `MetricCollection` forward ([#307](https://github.com/Lightning-AI/metrics/pull/307))
- Renamed `thresholds` argument to binned metrics for manually controlling the thresholds ([#322](https://github.com/Lightning-AI/metrics/pull/322))
- Extend typing ([#324](https://github.com/Lightning-AI/metrics/pull/324),
    [#326](https://github.com/Lightning-AI/metrics/pull/326),
    [#327](https://github.com/Lightning-AI/metrics/pull/327))

### Deprecated

- Deprecated `functional.mean_relative_error`, use `functional.mean_absolute_percentage_error` ([#248](https://github.com/Lightning-AI/metrics/pull/248))
- Deprecated `num_thresholds` argument in `BinnedPrecisionRecallCurve` ([#322](https://github.com/Lightning-AI/metrics/pull/322))

### Removed

- Removed argument `is_multiclass` ([#319](https://github.com/Lightning-AI/metrics/pull/319))

### Fixed

- AUC can also support more dimensional inputs when all but one dimension are of size 1 ([#242](https://github.com/Lightning-AI/metrics/pull/242))
- Fixed `dtype` of modular metrics after reset has been called ([#243](https://github.com/Lightning-AI/metrics/pull/243))
- Fixed calculation in `matthews_corrcoef` to correctly match formula ([#321](https://github.com/Lightning-AI/metrics/pull/321))

## [0.3.2] - 2021-05-10

### Added

- Added `is_differentiable` property:
    * To `AUC`, `AUROC`, `CohenKappa` and `AveragePrecision` ([#178](https://github.com/Lightning-AI/metrics/pull/178))
    * To `PearsonCorrCoef`, `SpearmanCorrcoef`, `R2Score` and `ExplainedVariance` ([#225](https://github.com/Lightning-AI/metrics/pull/225))

### Changed

- `MetricCollection` should return metrics with prefix on `items()`, `keys()` ([#209](https://github.com/Lightning-AI/metrics/pull/209))
- Calling `compute` before `update` will now give warning ([#164](https://github.com/Lightning-AI/metrics/pull/164))

### Removed

- Removed `numpy` as direct dependency ([#212](https://github.com/Lightning-AI/metrics/pull/212))

### Fixed

- Fixed auc calculation and add tests ([#197](https://github.com/Lightning-AI/metrics/pull/197))
- Fixed loading persisted metric states using `load_state_dict()` ([#202](https://github.com/Lightning-AI/metrics/pull/202))
- Fixed `PSNR` not working with `DDP` ([#214](https://github.com/Lightning-AI/metrics/pull/214))
- Fixed metric calculation with unequal batch sizes ([#220](https://github.com/Lightning-AI/metrics/pull/220))
- Fixed metric concatenation for list states for zero-dim input ([#229](https://github.com/Lightning-AI/metrics/pull/229))
- Fixed numerical instability in `AUROC` metric for large input ([#230](https://github.com/Lightning-AI/metrics/pull/230))

## [0.3.1] - 2021-04-21

- Cleaning remaining inconsistency and fix PL develop integration (
    [#191](https://github.com/Lightning-AI/metrics/pull/191),
    [#192](https://github.com/Lightning-AI/metrics/pull/192),
    [#193](https://github.com/Lightning-AI/metrics/pull/193),
    [#194](https://github.com/Lightning-AI/metrics/pull/194)
)


## [0.3.0] - 2021-04-20

### Added

- Added `BootStrapper` to easily calculate confidence intervals for metrics ([#101](https://github.com/Lightning-AI/metrics/pull/101))
- Added Binned metrics  ([#128](https://github.com/Lightning-AI/metrics/pull/128))
- Added metrics for Information Retrieval ([(PL^5032)](https://github.com/PyTorchLightning/pytorch-lightning/pull/5032)):
    * `RetrievalMAP` ([PL^5032](https://github.com/PyTorchLightning/pytorch-lightning/pull/5032))
    * `RetrievalMRR` ([#119](https://github.com/Lightning-AI/metrics/pull/119))
    * `RetrievalPrecision` ([#139](https://github.com/Lightning-AI/metrics/pull/139))
    * `RetrievalRecall` ([#146](https://github.com/Lightning-AI/metrics/pull/146))
    * `RetrievalNormalizedDCG` ([#160](https://github.com/Lightning-AI/metrics/pull/160))
    * `RetrievalFallOut` ([#161](https://github.com/Lightning-AI/metrics/pull/161))
- Added other metrics:
    * `CohenKappa` ([#69](https://github.com/Lightning-AI/metrics/pull/69))
    * `MatthewsCorrcoef` ([#98](https://github.com/Lightning-AI/metrics/pull/98))
    * `PearsonCorrcoef` ([#157](https://github.com/Lightning-AI/metrics/pull/157))
    * `SpearmanCorrcoef` ([#158](https://github.com/Lightning-AI/metrics/pull/158))
    * `Hinge` ([#120](https://github.com/Lightning-AI/metrics/pull/120))
- Added `average='micro'` as an option in AUROC for multilabel problems ([#110](https://github.com/Lightning-AI/metrics/pull/110))
- Added multilabel support to `ROC` metric ([#114](https://github.com/Lightning-AI/metrics/pull/114))
- Added testing for `half` precision ([#77](https://github.com/Lightning-AI/metrics/pull/77),
    [#135](https://github.com/Lightning-AI/metrics/pull/135)
)
- Added `AverageMeter` for ad-hoc averages of values ([#138](https://github.com/Lightning-AI/metrics/pull/138))
- Added `prefix` argument to `MetricCollection` ([#70](https://github.com/Lightning-AI/metrics/pull/70))
- Added `__getitem__` as metric arithmetic operation ([#142](https://github.com/Lightning-AI/metrics/pull/142))
- Added property `is_differentiable` to metrics and test for differentiability ([#154](https://github.com/Lightning-AI/metrics/pull/154))
- Added support for `average`, `ignore_index` and `mdmc_average` in `Accuracy` metric ([#166](https://github.com/Lightning-AI/metrics/pull/166))
- Added `postfix` arg to `MetricCollection` ([#188](https://github.com/Lightning-AI/metrics/pull/188))

### Changed

- Changed `ExplainedVariance` from storing all preds/targets to tracking 5 statistics ([#68](https://github.com/Lightning-AI/metrics/pull/68))
- Changed behaviour of `confusionmatrix` for multilabel data to better match `multilabel_confusion_matrix` from sklearn ([#134](https://github.com/Lightning-AI/metrics/pull/134))
- Updated FBeta arguments ([#111](https://github.com/Lightning-AI/metrics/pull/111))
- Changed `reset` method to use `detach.clone()` instead of `deepcopy` when resetting to default ([#163](https://github.com/Lightning-AI/metrics/pull/163))
- Metrics passed as dict to `MetricCollection` will now always be in deterministic order ([#173](https://github.com/Lightning-AI/metrics/pull/173))
- Allowed `MetricCollection` pass metrics as arguments ([#176](https://github.com/Lightning-AI/metrics/pull/176))

### Deprecated

- Rename argument `is_multiclass` -> `multiclass` ([#162](https://github.com/Lightning-AI/metrics/pull/162))

### Removed

- Prune remaining deprecated ([#92](https://github.com/Lightning-AI/metrics/pull/92))

### Fixed

- Fixed when `_stable_1d_sort` to work when `n>=N` ([PL^6177](https://github.com/PyTorchLightning/pytorch-lightning/pull/6177))
- Fixed `_computed` attribute not being correctly reset ([#147](https://github.com/Lightning-AI/metrics/pull/147))
- Fixed to Blau score ([#165](https://github.com/Lightning-AI/metrics/pull/165))
- Fixed backwards compatibility for logging with older version of pytorch-lightning ([#182](https://github.com/Lightning-AI/metrics/pull/182))


## [0.2.0] - 2021-03-12

### Changed

- Decoupled PL dependency ([#13](https://github.com/Lightning-AI/metrics/pull/13))
- Refactored functional - mimic the module-like structure: classification, regression, etc. ([#16](https://github.com/Lightning-AI/metrics/pull/16))
- Refactored utilities -  split to topics/submodules ([#14](https://github.com/Lightning-AI/metrics/pull/14))
- Refactored `MetricCollection` ([#19](https://github.com/Lightning-AI/metrics/pull/19))

### Removed

- Removed deprecated metrics from PL base ([#12](https://github.com/Lightning-AI/metrics/pull/12),
    [#15](https://github.com/Lightning-AI/metrics/pull/15))



## [0.1.0] - 2021-02-22

- Added `Accuracy` metric now generalizes to Top-k accuracy for (multi-dimensional) multi-class inputs using the `top_k` parameter ([PL^4838](https://github.com/PyTorchLightning/pytorch-lightning/pull/4838))
- Added `Accuracy` metric now enables the computation of subset accuracy for multi-label or multi-dimensional multi-class inputs with the `subset_accuracy` parameter ([PL^4838](https://github.com/PyTorchLightning/pytorch-lightning/pull/4838))
- Added `HammingDistance` metric to compute the hamming distance (loss) ([PL^4838](https://github.com/PyTorchLightning/pytorch-lightning/pull/4838))
- Added `StatScores` metric to compute the number of true positives, false positives, true negatives and false negatives ([PL^4839](https://github.com/PyTorchLightning/pytorch-lightning/pull/4839))
- Added `R2Score` metric ([PL^5241](https://github.com/PyTorchLightning/pytorch-lightning/pull/5241))
- Added `MetricCollection` ([PL^4318](https://github.com/PyTorchLightning/pytorch-lightning/pull/4318))
- Added `.clone()` method to metrics ([PL^4318](https://github.com/PyTorchLightning/pytorch-lightning/pull/4318))
- Added `IoU` class interface ([PL^4704](https://github.com/PyTorchLightning/pytorch-lightning/pull/4704))
- The `Recall` and `Precision` metrics (and their functional counterparts `recall` and `precision`) can now be generalized to Recall@K and Precision@K with the use of `top_k` parameter ([PL^4842](https://github.com/PyTorchLightning/pytorch-lightning/pull/4842))
- Added compositional metrics ([PL^5464](https://github.com/PyTorchLightning/pytorch-lightning/pull/5464))
- Added AUC/AUROC class interface ([PL^5479](https://github.com/PyTorchLightning/pytorch-lightning/pull/5479))
- Added `QuantizationAwareTraining` callback ([PL^5706](https://github.com/PyTorchLightning/pytorch-lightning/pull/5706))
- Added `ConfusionMatrix` class interface ([PL^4348](https://github.com/PyTorchLightning/pytorch-lightning/pull/4348))
- Added multiclass AUROC metric ([PL^4236](https://github.com/PyTorchLightning/pytorch-lightning/pull/4236))
- Added `PrecisionRecallCurve, ROC, AveragePrecision` class metric ([PL^4549](https://github.com/PyTorchLightning/pytorch-lightning/pull/4549))
- Classification metrics overhaul ([PL^4837](https://github.com/PyTorchLightning/pytorch-lightning/pull/4837))
- Added `F1` class metric ([PL^4656](https://github.com/PyTorchLightning/pytorch-lightning/pull/4656))
- Added metrics aggregation in Horovod and fixed early stopping ([PL^3775](https://github.com/PyTorchLightning/pytorch-lightning/pull/3775))
- Added `persistent(mode)` method to metrics, to enable and disable metric states being added to `state_dict` ([PL^4482](https://github.com/PyTorchLightning/pytorch-lightning/pull/4482))
- Added unification of regression metrics ([PL^4166](https://github.com/PyTorchLightning/pytorch-lightning/pull/4166))
- Added persistent flag to `Metric.add_state` ([PL^4195](https://github.com/PyTorchLightning/pytorch-lightning/pull/4195))
- Added classification metrics ([PL^4043](https://github.com/PyTorchLightning/pytorch-lightning/pull/4043))
- Added new Metrics API. ([PL^3868](https://github.com/PyTorchLightning/pytorch-lightning/pull/3868), [PL^3921](https://github.com/PyTorchLightning/pytorch-lightning/pull/3921))
- Added EMB similarity ([PL^3349](https://github.com/PyTorchLightning/pytorch-lightning/pull/3349))
- Added SSIM metrics ([PL^2671](https://github.com/PyTorchLightning/pytorch-lightning/pull/2671))
- Added BLEU metrics ([PL^2535](https://github.com/PyTorchLightning/pytorch-lightning/pull/2535))
