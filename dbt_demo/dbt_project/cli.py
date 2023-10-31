from pathlib import Path

from odd_dbt import config
from odd_dbt.domain.cli_args import CliArgs
from odd_dbt.libs.dbt import get_context
from odd_dbt.libs.odd import create_dbt_generator_from_oddrn
from odd_dbt.mapper.lineage import DbtLineageMapper
from odd_dbt.mapper.test_results import DbtTestMapper
from odd_dbt.service.odd import ingest_entities

cfg = config.Config(
    odd_platform_host="http://localhost:8080",
    odd_platform_token="",
    dbt_data_source_oddrn="//dbt/host/localhost",
)  # All fields can be set manually or read from ENV variables
client = config.create_odd_client(
    host=cfg.odd_platform_host, token=cfg.odd_platform_token
)
generator = create_dbt_generator_from_oddrn(oddrn=cfg.dbt_data_source_oddrn)
cli_args = CliArgs.default()

cli_args.profiles_dir = Path("./profiles")
cli_args.project_dir = Path(".")
cli_args.target = "local"
context = get_context(cli_args=cli_args)

data_entities = DbtTestMapper(context=context, generator=generator).map()
ingest_entities(data_entities, client)

data_entities = DbtLineageMapper(context=context, generator=generator).map()
ingest_entities(data_entities, client)
