import os
import time
from datetime import datetime
import Adafruit_DHT
from pprint import pprint
import boto3

# AWS setup
resource = boto3.resource('dynamodb')


# add sensor reading to AWS DynamoDB
def add_sensor_reading(timestamp, date, time, temperature, humidity):

    table = resource.Table('sensor_data')

    # get last record in the table to use to set the next key in the id column

    response = table.put_item(
        Item={
            'timestamp': timestamp,
            'date': date,
            'time': time,
            'temperature': temperature,
            'humidity': humidity
        }
    )
    return response


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

pin = 2

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
date = time.strftime('%d/%m/%y')
time = time.strftime('%H:%M')

# If you want to test this and run it as a script
if __name__ == '__main__':
    sensor_add_reading_resp = add_sensor_reading(
        timestamp, date, time, int(temperature), int(humidity))
    pprint("Success adding sensor reading")
    # pprint(sensor_add_reading_resp, sort_dicts=False)
