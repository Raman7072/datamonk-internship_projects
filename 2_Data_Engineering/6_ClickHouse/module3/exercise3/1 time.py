from clickhouse_driver import Client
import time

client = Client('localhost')
client.execute("CREATE TABLE IF NOT EXISTS live_insert (id UInt32, value Float32) ENGINE = MergeTree() ORDER BY id;")

i = 0
while True:
    client.execute("INSERT INTO live_insert VALUES", [(i, i*1.1)])
    i += 1
    time.sleep(0.1)
