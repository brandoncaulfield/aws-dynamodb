# Access an AWS Dynamo DB using Boto3
import boto3

from pprint import pprint

s3 = boto3.resource('s3')
client = boto3.client(
    'dynamodb')
resource = boto3.resource(
    'dynamodb')

# Use the client object ot get a list of tables
dynamodb_tables = client.list_tables()
print(dynamodb_tables)


# add sensor reading to AWS DynamoDB
def add_sensor_reading(timestamp, date, time, temperature, humidity):
    # Wasn't working at the time for some reason
    # if not resource:
    #     resource = boto3.resource('dynamodb')

    table = resource.Table('sensor_data')

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


if __name__ == '__main__':
    sensor_read_add_resp = add_sensor_reading(
        '301120201325', '30/11/2020', '13:25', '25.1', '51%')
    pprint("Success adding sensor reading")
    pprint(sensor_read_add_resp, sort_dicts=False)
