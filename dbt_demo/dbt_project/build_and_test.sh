dbt build --profiles-dir profiles

UNIQ_NAME="dbt_demo_$(uuidgen)"
export ODD_COLLECTOR_TOKEN="$(odd tokens create $UNIQ_NAME)"
echo "ODD_COLLECTOR_TOKEN=$ODD_COLLECTOR_TOKEN"
odd dbt test --profiles-dir profiles -t $ODD_COLLECTOR_TOKEN -h $ODD_PLATFORM_HOST
