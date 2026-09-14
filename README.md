# Project
```bash
# Setup.
uv python install 3.13
uv python pin 3.13
uv sync

# Execute.
export AUTHORIZATION=get_in_your_browser_request_when_accessing_the_portal
uv run main.py
```

# Container 
```bash
# Create image.
sudo docker image build --tag discord-social-sdk .

# Create container.
sudo docker container create --name discord-social-sdk discord-social-sdk
sudo docker container start discord-social-sdk
sudo docker container exec --interactive --tty discord-social-sdk bash

# Publish image.
sudo docker push ghcr.io/thiagola92/discord-social-sdk:latest
```