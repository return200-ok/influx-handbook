# from influxdb_client import InfluxDBClient
# from influxdb_client.client.write_api import ASYNCHRONOUS

# url = '127.0.0.1:8086'
# token = 'owNcFjQ_CYRqF17x8Nlt0ByUdGg4xMar51ziPJ7murTdoptCvy6BBwUYwHWL7JdPmWD7qsc4y1FgKRqGrCrPVw=='
# org = 'mainorg'
# bucket = 'test'

# client = InfluxDBClient(url=url, token=token, org=org)
# data = ["MSFT,stock=MSFT value=62.79"]
# write_api = client.write_api(write_option='SYNCHRONOUS')
# write_api.write(bucket, org, data, write_precision='s')


from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "owNcFjQ_CYRqF17x8Nlt0ByUdGg4xMar51ziPJ7murTdoptCvy6BBwUYwHWL7JdPmWD7qsc4y1FgKRqGrCrPVw=="
org = "mainorg"
bucket = "test"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = "project,project_name=influx id=23"
    write_api.write(bucket, org, data)

