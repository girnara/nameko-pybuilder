#!/bin/bash

# Check if rabbit is up and running before starting the service.

is_ready() {
    eval "curl -I http://${RABBIT_USER}:${RABBIT_PASSWORD}@${RABBIT_HOST}:${RABBIT_MANAGEMENT_PORT}/api/vhosts"
}

i=0
while ! is_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - rabbit still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for rabbit to be ready"
    sleep 3
done

# Run Migrations
cd /var/nameko/
source /var/nameko/venv/bin/activate
export PYTHONPATH=$PYTHONPATH:/var/nameko
alembic upgrade head

# Run Service

nameko run --config /var/nameko/config.yml orders.service --backdoor 3000
