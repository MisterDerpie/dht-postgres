#!/bin/bash

docker image build -t dht_db ./docker_database/
docker image build -t dht_reader ./python_polling/
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