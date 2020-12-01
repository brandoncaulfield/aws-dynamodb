import boto3
from pprint import pprint

# Get the service resource
resource = boto3.resource('dynamodb')


# Create a table
def create_table():
    table = resource.create_table(
        TableName='sensor_data',
        KeySchema=[
            {
                'AttributeName': 'timestamp',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'date',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='sensor_data')

    # Print out some data about the table.
    print(table.item_count)


# Delete a table
def delete_table(table_name):
    table = resource.Table(table_name)
    response = table.delete()
    pprint(response)


if __name__ == '__main__':
    # Execute only if run as a script
    # delete_table('my_new_table')
    create_table()
