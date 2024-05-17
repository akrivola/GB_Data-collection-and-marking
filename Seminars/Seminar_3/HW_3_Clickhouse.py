from clickhouse_driver import Client
import json

client = Client('localhost')

client.execute('CREATE DATADATE IF NOT EXISTS town_cary')