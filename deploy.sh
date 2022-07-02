#!/bin/bash

rsync -av --delete \
  --exclude={'.idea','*.iml'}  \
  ./ peng@peng.sucicada.cf:~/APP/SuCicadaBot/

# shellcheck source=update.sh
ssh peng@peng.sucicada.cf 'bash -c "source ~/.bashrc && ~/APP/SuCicadaBot/update.sh"'
