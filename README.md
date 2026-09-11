# Setup
```
uv python install 3.13
uv python pin 3.13
uv sync
```

# Usage
```
uv run --env-file=.env main.py
```

# Container
```
sudo docker image build --tag testing .
sudo docker container create --name testing testing
sudo docker container start testing
sudo docker container exec --interactive --tty testing bash
```