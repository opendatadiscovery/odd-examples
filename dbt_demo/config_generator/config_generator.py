import os
import pathlib
from uuid import uuid4

import yaml
from odd_models.api_client.v2.odd_api_client import Client

platform_url = os.getenv("PLATFORM_HOST_URL", "http://odd-platform:8080")
path = pathlib.Path().cwd()
opt_path = path.parent / "opt"

client = Client(host=platform_url)

collector_config = {
    "token": client.create_token(name=f"demo-token-{uuid4()}", description="demo-token"),
    "platform_host_url": platform_url,
    "chunk_size": 1000,
    "plugins": [{
    "type": "postgresql",
    "name": "postgres_adapter",
    "description": "",
    "database": os.getenv("SAKILA_POSTGRES_DATABASE"),
    "host": os.getenv("SAKILA_POSTGRES_HOST"),
    "port": os.getenv("SAKILA_POSTGRES_PORT"),
    "user": os.getenv("SAKILA_POSTGRES_USER"),
    "password": os.getenv("SAKILA_POSTGRES_PASSWORD"),
    }],
}

with open(opt_path / "collector_config.yaml", "w") as f:
    f.write(yaml.dump(collector_config))