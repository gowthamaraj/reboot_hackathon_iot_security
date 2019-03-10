import psutil


from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

print(client.get_list_database())

client.create_database('battery')

print("modified")
print(client.get_list_database())

client.switch_database('battery')

for i in range(20):
    bat=psutil.sensors_battery().percent+i



    json_body = [
    {
        "measurement": "percent",
        "tags": {
            "user": "windows 10",
        },
        "fields": {
            "duration": bat
        }
    }
    ]

    print(client.write_points(json_body))

results=client.query('SELECT * FROM percent')

points = results.get_points(tags={'user': 'windows 10'})
for point in points:
    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
