import os
from uuid import uuid4
from odd_models.api_client.v2.odd_api_client import Client
import pathlib
import yaml


platform_url = os.getenv("PLATFORM_HOST_URL", "http://odd-platform:8080")
path = pathlib.Path().cwd()
opt_path = path.parent / "opt"

client = Client(host=platform_url)
token = client.create_token(name=f"demo-token-{uuid4()}", description="demo-token")

collector_config = {
    "token": token,
    "platform_host_url": platform_url,
    "chunk_size": 1000,
    "plugins": [{
    "type": "postgresql",
    "name": "postgres_adapter",
    "description": "",
    "database": 'fake_pii',
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    }],
}

profiler_config = {
    'token': token,
    'platform_host_url': platform_url,
    'profilers': [
        {
            'type': 'postgres',
            'name': 'postgres_profiler',
            'host': os.getenv("POSTGRES_HOST"),
            'port': os.getenv("POSTGRES_PORT"),
            'username': os.getenv('POSTGRES_USER'),
            'password': os.getenv('POSTGRES_PASSWORD'),
            'database': 'fake_pii'
        }
    ]
}



with open(opt_path / "collector_config.yaml", "w") as f:
    f.write(yaml.dump(collector_config))

with open(opt_path / "profiler_config.yaml", "w") as f:
    f.write(yaml.dump(profiler_config))
