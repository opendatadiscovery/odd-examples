#!/bin/bash

COLLECTOR_NAME=$1

REQUEST_BODY="{\"name\": \"$COLLECTOR_NAME\"}"
ENDPOINT="http://localhost:8082/api/collectors"

RESPONSE=$(curl -d "$REQUEST_BODY" -H "Content-Type: application/json" -X POST "$ENDPOINT")
TOKEN=$(grep -o '"value":"[^"]*' <<< $RESPONSE | grep -o '[^"]*$')

if [ ${#TOKEN} == 0 ]; then
    echo "Something went wrong. Please check the logs."
    echo "$RESPONSE"
else
    echo "Collector created successfully with token ${TOKEN}."
    echo "Updating collector config..."

    TEMPLATE="$(pwd)/config/collector_config_template.yaml"
    CONFIG_FILE="$(pwd)/config/collector_config.yaml"

    sed "s/#TOKEN#/$TOKEN/g" "$TEMPLATE" > "$CONFIG_FILE"
    echo "Collector config at path $CONFIG_FILE updated successfully."
fi

