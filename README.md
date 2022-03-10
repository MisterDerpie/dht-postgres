# DHT Temperature Reader

This is a small project to poll a DHT11/DHT22 temperature sensor and store the results in a PostgreSQL database.
Docker must be installed.
To build the containers, run `create_temperature_setup.sh`.

The script will create

- 2 Docker images `temperature_pg_db` and `dht_reader`
- 1 Docker network `temperature`
- 2 Docker containers `temperature_pg_db` and  `dht_reader`

## Change Sensor and Pin

Depending on the wiring and sensor, change `python_polling/dht/dhtsensor.py` on line 23.