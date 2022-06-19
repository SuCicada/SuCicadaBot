#!/bin/bash
# shellcheck disable=SC2164

cd "$(dirname "$0")"
cp conf/supervisor/* ~/etc/supervisor/conf.d/
supervisorctl.sh update
supervisorctl.sh restart sucicada_bot:
