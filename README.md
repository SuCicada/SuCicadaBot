# run
```bash
git clone git@github.com:SuCicada/SuCicadaBot.git --recurse-submodules
cd SuCicadaBot
bash install.sh

pip3 install poetry 
poetry install
poetry run python bot_console.py
poetry run python bot_telegram.py
poetry run python bot_qq.py
```
poetry export --without-hashes -o requirements.txt

## dev - wsl
```bash
update-hosts
sudo systemctl restart sshd
ssh -fgN -R 10809:win.ip:10809 localhost
```

## dev - remote
```bash
rsync -av --delete --exclude .idea  ./ peng@peng.sucicada.cf:~/APP/SuCicadaBot
```

## update
```bash
bash update.sh
```



```bash
pip3 install virtualenv
virtualenv venv
pip install nb-cli

nb adapter install nonebot-adapter-onebot
nb driver install websockets 

# telegram
nb driver install httpx
nb adapter install nonebot-adapter-telegram

# console
pip install websocket-client

source venv/Scripts/activate
```

```bash
nb plugin install nonebot-plugin-apscheduler
pip install croniter
```

- dev
```bash
wget https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc2/go-cqhttp_windows_amd64.exe

cd /home/peng/APP && mkdir cqhttp && cd cqhttp
wget https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc2/go-cqhttp_linux_amd64.tar.gz -O /tmp/go-cqhttp_linux_amd64.tar.gz && {
  tar zxvf /tmp/go-cqhttp_linux_amd64.tar.gz -C /tmp  
  mv /tmp/go-cqhttp .
} 
```

- dev
  - https://docs.go-cqhttp.org
  - https://v2.nonebot.dev
  - https://onebot.adapters.nonebot.dev/docs
  - https://tianli-blog.club/2021/06/08/qqbot/#%E5%8A%9F%E8%83%BD
  - https://github.com/nonebot/awesome-nonebot

- problem
  - https://github.com/Mrs4s/go-cqhttp/issues/1469

