## Demo example for Delta Lake stored at Minio storage. 

1. Firstly we need to create network for spark cluster for correct work of spark cluster and odd-platform
```bash
docker network create spark
```

2. Next we need to start all services, except collector, which will be started later.
Services:
    1. `database` - postgresql database for odd-platform
    2. `odd-platform` - OpenDataDiscovery Platform, started at ```http://localhost:8082```
    3. `spark` and `spark-worker` - spark master
    4. `minio` - minio storage for delta lake, started at ```http://localhost:9000``` with credentials ```minioadmin:minioadmin```
    5. `jupyter` - jupyter notebook with demo notebook, started ```http://localhost:8890```
```bash
docker compose up -d database odd-platform spark spark-worker minio jupyter
```
3. After all services are started, you can open jupyter notebook at ```http://localhost:8890/lab/tree/delta_lake.ipynb```
4. For collector we need to create token with any name we want and run it and use it in collector configuration.
Next command creates token with name `odd_collector` and creates collector configuration file `odd_collector.yaml` in '/config' directory.
```bash
sh create_collector.sh odd_collector
```
5. As we have collector configuration file, we can start collector.
It can take some time fetching data from Minio storage.
```bash
docker compose up -d odd-collector-aws
```
7. Open OpenDataDiscovery Platform UI at ```http://localhost:8082``` to check the results.
8. Cleanup
```bash
docker compose down --volumes
```
Remove network
```bash
docker network rm spark
```