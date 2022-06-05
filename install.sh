#!/bin/bash
# shellcheck disable=SC2164

function git_sparse_clone() (
  pwd=$(pwd)
  rurl="$1" localdir="$2" && shift 2
  mkdir -p "$localdir"
  cd "$localdir"
  git init
  git remote add -f origin "$rurl"
  git config core.sparseCheckout true
  for i; do
    echo "$i" >> .git/info/sparse-checkout
  done
  git pull origin master
  git branch --set-upstream-to=origin/master master
  cd "$pwd"
)

cd "$(dirname "$0")"
git_sparse_clone "git@github.com:SuCicada/SuConfig.git" "SuConfig" "SuCicadaBot/"

ls -lR SuConfig
cp -rv SuConfig/SuCicadaBot/conf/. conf/
