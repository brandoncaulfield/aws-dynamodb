# AWS DynamoDB Using the Python SDK

## What is AWS DynamoDB?

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.

## boto3 Python Library

I've used the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) python library to access the AWS DynamoDB tables.

So far I've added the following calls:

- list_tables()
- put_item() - add a row to a table
- create_table()
- table.delete()

more to come...

## Getting Started

To get started with this repo you need an [AWS account](https://aws.amazon.com/) and you need to carefully run through the [boto3 Installation and config](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation).

From there it's relatively straight forward to use the library if you follow the documentation.

## Documentation

- [boto3 Installation and Config](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
- [Python and DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.01)
