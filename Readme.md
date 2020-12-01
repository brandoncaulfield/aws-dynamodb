# AWS DynamoDB, Lambda and SNS Using the Python SDK

## What is AWS DynamoDB?

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.

## What is AWS Lambda?

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

With Lambda, you can run code for virtually any type of application or backend service - all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

## What is AWS SNS(Simple Notification Service)?

Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

## Scenario

Running a python script on a [Raspberry Pi](https://www.raspberrypi.org/) that uses an external temp/humidity sensor ([DHT22 AM2302](https://www.amazon.co.uk/AZDelivery-DHT22-modul-parent/dp/B07Z6JRMCW)) that measures temperature and humidity. Each time the temp/humidity data is read, it is sent to an AWS DynamoDB table. The temp/humidity readings are collected using the [Adafruit_DHT](https://github.com/adafruit/Adafruit_Python_DHT) library.

Each time this happens an event is triggered in the DynamoDB stream (i.e. when an item is added to the table). AWS Lambda subcribes to that event and uses AWS SNS to send an email notification. The cool thing is, you can send almost any type of notification you want, including SMS and push notifications!

## boto3 Python Library

I've used the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) python library to access the AWS DynamoDB tables.

So far, I've added the following calls:

- list_tables()
- put_item() - add a row to a table
- create_table()
- table.delete()

more to come...

## Getting Started

### Create a Table and Add Data to it:

To get started with this repo you need an [AWS account](https://aws.amazon.com/) and you need to carefully run through the [boto3 Installation and config](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation).

You will also need to create a DynamoDB database and create a table (making sure to enable the stream) to send data to.

From there it's relatively straight forward to use the library if you follow the documentation.

### Setting Up an AWS Lambda Function and AWS SNS(Simple Notification Service) Topic and Subscription:

Once you're comfortable adding records to your DynamoDB table you can also setup a Lambda function to be triggered every time something changes in the table stream (i.e. when a record is added). The Lambda function calls the SNS service which sends the email notification.

There's a great [tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html) from AWS that shows you how to achieve this with the AWS CLI. You don't have to use the CLI and can do the same thing in the AWS console manually, just follow the same steps and add the code, permissions where appropriate.

## Documentation

- [Getting Started with Amazon DynamoDB](https://aws.amazon.com/dynamodb/getting-started/)
- [boto3 Installation and Config](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
- [Python and DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.01)
- [Tutorial: Process New Items with DynamoDB Streams and Lambda](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html)
