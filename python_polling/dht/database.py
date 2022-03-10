#!/bin/python3

import psycopg2
from time import sleep

class DhtDatabase:
    def insert_reading(self, temperature, humidity):
        connection = self.__get_connection()
        self.__insert_reading(temperature, humidity, connection)
        connection.close()

    def __insert_reading(self, temperature, humidity, connection):
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO readings (temperature, humidity) VALUES ({temperature}, {humidity})')
        cursor.close()
        connection.commit()
    
    def __get_connection(self):
        try: 
            return psycopg2.connect(
                user="postgres",
                password="test",
                host="dht_db",
                port="5432",
                database="dht_database"
            )
        except Exception as exception:
            print('Failed to connect, fallback and retry ...')
            sleep(1)
            return self.__get_connection()