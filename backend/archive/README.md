# Fastapi Best Practices Service

This service can be used as an example service for developers

https://github.com/StarDylan/StellarElixirs/blob/85807d66637a70478dc73f699d255aaa1db97e07/src/logger_init.py#L4

## Build locally
```bash
sudo docker build -t fastapi-best-practices .
sudo docker rm -f fastapi-best-practices || true
sudo docker run --name fastapi-best-practices -p 9876:8080 fastapi-best-practices
```

```bash
uvicorn "src.app:app" --host 0.0.0.0 --port 8080 --log-config log-config.yaml
```
