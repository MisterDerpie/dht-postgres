#!/bin/bash
psql -U postgres -c "CREATE DATABASE dht_database;"
psql -U postgres -d dht_database -c "CREATE TABLE readings (
    timestamp TIMESTAMP DEFAULT current_timestamp,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL
);

CREATE INDEX ON readings(timestamp);"