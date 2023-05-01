### odd-profiler-demo

![screenshot.png](./assets/screenshot.png)

#### Provided datasources:
- [x] PostgreSQL
- [ ] AzureSql
- [ ] MySQL
- [ ] Microsoft SQL Server

### Run demo
```commandline
docker compose up
```
#### Flow

1. Firstly it will run `database` and `odd-platform` services.
2. Next, after `config-generator` will be built and run, it calls Platform's API to retrieve tokens and create config files for collectors.
3. After all config files were stored to the mounted `configs` folder `odd-collector` will be started to fetch metadata for datasets from datasources.
4. When `odd-collector` ingested metadata to Platform and exited, `odd-profiler` will be started to calculate statistics and autolabel dataset's fields.

#### Notes
* Demo can take some time and depend on host machine.

* If you want to change something in `config_generator.py` and rerun `docker compose` use:
```commandline
docker compose up --build
```

