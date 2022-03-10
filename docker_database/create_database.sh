#!/bin/bash
psql -U postgres -c "CREATE DATABASE temperature;"
psql -U postgres -d temperature -c "CREATE TABLE temperature (
    timestamp timestamp default current_timestamp,
    temperature int
);

CREATE INDEX ON temperature(timestamp);"