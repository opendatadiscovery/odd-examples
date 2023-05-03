### Run
```
docker compose up --build
```

### That command will start the following containers:
1. database - postgres database to store the metadata
2. odd-platform - Open Data Discovery platform server at http://localhost:8080, which will be used to store the metadata.
3. sakila database - postgres database with sample data
4. dbt - service to run dbt commands, build and test the models using odd-cli
5. odd-collector - service to collect metadata from sakila database and push it to odd-platform

After odd-collector finishes, you can check the metadata in odd-platform at http://localhost:8080

### Clean up
```
docker compose rm -f --volumes
```