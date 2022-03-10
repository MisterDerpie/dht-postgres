FROM python:3.9-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache postgresql-libs g++ python3-dev postgresql-dev gcc musl-dev \
    && CFLAGS="-fcommon" pip3 install RPi.GPIO \
    && pip3 install psycopg2 adafruit-circuitpython-dht \
    && apk del --no-cache g++ python3-dev postgresql-dev gcc musl-dev \
    && mkdir -p /home/user/dht/
ADD dht /home/user/dht/

ENTRYPOINT ["python3", "/home/user/dht/poll.py"]