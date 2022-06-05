#!/bin/bash
# shellcheck disable=SC2164
cd "$(dirname "$0")"

git pull --recurse-submodules
(cd SuConfig/ && git pull)

cp -rv SuConfig/SuCicadaBot/conf/. conf/
