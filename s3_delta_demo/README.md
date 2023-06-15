## Demo example for Delta Lake stored at Minio storage
1. Create network
```bash
docker network create spark
```
2. Start main services
```bash
docker compose up -d database odd-platform spark spark-worker minio jupyter
```
3. After all services are started, you can open jupyter notebook at ```http://localhost:8890/lab/tree/delta_lake.ipynb```
4. Create token for collector
```bash
sh create_collector.sh odd_collector
```
5. Run collector
```bash
docker compose up -d odd-collector-aws
```
7. Open Odd Platform UI at ```http://localhost:8082``` to check the results.
8. Cleanup
Stop services with volumes
```bash
docker compose down --volumes
```
Remove network
```bash
docker network rm spark
```