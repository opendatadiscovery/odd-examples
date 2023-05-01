FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends && apt-get install uuid-runtime

WORKDIR /usr/src/dbt/dbt_project

# Install the dbt Postgres adapter. This step will also install dbt-core
RUN pip install --upgrade pip
RUN pip install dbt-postgres
RUN pip install odd-cli==0.1.22

# Install dbt dependencies (as specified in packages.yml file)
# Build seeds, models and snapshots (and run tests wherever applicable)
ARG ODD_PLATFORM_HOST

# CMD ["/bin/bash", "-c", "build_and_test.sh"]
ENTRYPOINT ["sh", "build_and_test.sh"]