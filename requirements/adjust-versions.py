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
import logging
import os
import re
import sys
from typing import Dict, Optional

from packaging.version import Version

VERSIONS = [
    dict(torch="1.13.0", torchvision="0.14.0", torchtext="0.14.0"),  # nightly
    dict(torch="1.12.1", torchvision="0.13.1", torchtext="0.13.1"),  # stable
    dict(torch="1.12.0", torchvision="0.13.0", torchtext="0.13.0"),
    dict(torch="1.11.0", torchvision="0.12.0", torchtext="0.12.0"),
    dict(torch="1.10.2", torchvision="0.11.3", torchtext="0.11.2"),
    dict(torch="1.10.1", torchvision="0.11.2", torchtext="0.11.1"),
    dict(torch="1.10.0", torchvision="0.11.1", torchtext="0.11.0"),
    dict(torch="1.9.1", torchvision="0.10.1", torchtext="0.10.1"),
    dict(torch="1.9.0", torchvision="0.10.0", torchtext="0.10.0"),
    dict(torch="1.8.2", torchvision="0.9.1", torchtext="0.9.1"),
    dict(torch="1.8.1", torchvision="0.9.1", torchtext="0.9.1"),
    dict(torch="1.8.0", torchvision="0.9.0", torchtext="0.9.0"),
]
VERSIONS.sort(key=lambda v: Version(v["torch"]), reverse=True)


def find_latest(ver: str) -> Dict[str, str]:
    # drop all except semantic version
    ver = re.search(r"([\.\d]+)", ver).groups()[0]
    # in case there remaining dot at the end - e.g "1.9.0.dev20210504"
    ver = ver[:-1] if ver[-1] == "." else ver
    logging.info(f"finding ecosystem versions for: {ver}")

    # find first match
    for option in VERSIONS:
        if option["torch"].startswith(ver):
            return option

    raise ValueError(f"Missing {ver} in {VERSIONS}")


def main(path_req: str, torch_version: Optional[str] = None) -> None:
    if not torch_version:
        import torch

        torch_version = torch.__version__
    assert torch_version, f"invalid torch: {torch_version}"
    latest = find_latest(torch_version)

    if path_req == "conda":
        # this is a special case when we need to get the remaining lib versions
        # req = " ".join([f"{lib}={ver}" if ver else lib for lib, ver in latest.items() if lib != "torch"])
        req = " ".join([f"{lib}={ver}" for lib, ver in latest.items() if lib != "torch" and ver])
        print(req)
        return

    with open(path_req) as fp:
        req = fp.readlines()
    # remove comments
    req = [r[: r.index("#")] if "#" in r else r for r in req]
    req = [r.strip() for r in req]

    for lib, ver in latest.items():
        for i, ln in enumerate(req):
            m = re.search(r"(\w\d-_)*?[>=]{0,2}.*", ln)
            if m and m.group() == lib:
                req[i] = f"{lib}=={ver}" if ver else lib

    req = [r + os.linesep for r in req]
    logging.info(req)  # on purpose - to debug
    with open(path_req, "w") as fp:
        fp.writelines(req)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main(*sys.argv[1:])
