#!/bin/bash

docker image build -t dht_db ./docker_database/
docker image build -t dht_reader ./python_polling/
docker image build -t dht_grafana ./grafana/
docker create network create temperature

docker container run -d \
    --name dht_db \
    --net temperature \
    -p 5432:5432 dht_db
docker container run -d \
    --name dht_reader \
    --net temperature \
    --device /dev/gpiomem \
    dht_reader
docker container run -d \
    --name dht_grafana \
    --net temperature \
    -p 80:3000 \
    dht_grafana