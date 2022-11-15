# Installing the Library
## python3 -m pip install influxdb
# Making a Connection
client = InfluxDBClient(host='localhost', port=8086)
client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
client.create_database('pyexample')
client.get_list_database()
client.switch_database('pyexample')
# Inserting Data
json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-30T8:02:00Z",
        "fields": {
            "duration": 129
        }
    }
]

client.write_points(json_body)
# Querying Data
client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')
results.raw
points = results.get_points(tags={'user':'Carol'})
for point in points:
    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
brush_usage_total = 0
for point in points:
    brush_usage_total = brush_usage_total + point['duration']
if brush_usage_total > 350:
    print("You've used your brush head for %s seconds, more than the recommended amount! Time to replace your brush head!" % brush_usage_total)
 