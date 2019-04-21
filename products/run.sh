#!/bin/bash

# Check if rabbit and redis are up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done

until nc -z ${REDIS_HOST} ${REDIS_PORT}; do
    echo "$(date) - waiting for redis..."
    sleep 1
done

# Run the service
source /var/nameko/venv/bin/activate
cd /var/nameko/
nameko run --config /var/nameko/config.yml products.service --backdoor 3000
