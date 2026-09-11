# Setup
```
uv python install 3.13
uv python pin 3.13
uv sync
```

# Usage
```
export AUTHORIZATION=get_in_your_browser_request_when_accessing_the_portal
uv run main.py
```

# Container
```
sudo docker image build --no-cache --tag discord-social-sdk .
sudo docker container create --name discord-social-sdk discord-social-sdk
sudo docker container start discord-social-sdk
sudo docker container exec --interactive --tty discord-social-sdk bash
```