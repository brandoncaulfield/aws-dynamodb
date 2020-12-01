"use strict";
var AWS = require("aws-sdk");
var sns = new AWS.SNS();

exports.handler = (event, context, callback) => {
  event.Records.forEach((record) => {
    console.log("Stream record: ", JSON.stringify(record, null, 2));

    if (record.eventName == "INSERT") {
      const date = JSON.stringify(record.dynamodb.NewImage.date.S);
      const time = JSON.stringify(record.dynamodb.NewImage.time.S);
      const temperature = JSON.stringify(
        record.dynamodb.NewImage.temperature.N
      );
      const humidity = JSON.stringify(record.dynamodb.NewImage.humidity.N);
      var params = {
        Subject: "A new sensor reading has been added to AWS",
        Message:
          "Date: " +
          date +
          "\n\n " +
          "Time: " +
          time +
          "\n\n " +
          "Temp: " +
          temperature +
          "\n\n " +
          "Humidity: " +
          humidity +
          "\n\n ",
        TopicArn: "arn:aws:sns:eu-west-2:576477103328:dynamodb",
      };
      sns.publish(params, function (err, data) {
        if (err) {
          console.error(
            "Unable to send message. Error JSON:",
            JSON.stringify(err, null, 2)
          );
        } else {
          console.log(
            "Results from sending message: ",
            JSON.stringify(data, null, 2)
          );
        }
      });
    }
  });
  callback(null, `Successfully processed ${event.Records.length} records.`);
};
