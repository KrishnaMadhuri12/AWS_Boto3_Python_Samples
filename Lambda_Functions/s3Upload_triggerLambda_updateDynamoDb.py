# UseCase: When the file uploads in s3 bucket. Trigger lambda function to read the data and update the dynamno db table
# Task1: Read the Data from the event.
# Pull the bucketname, filename from the event object
# Task2: Read the json object from s3 bucket
# Task3: Update Dynamo DB


import boto3
import json

def lambda_handler(event, context):
    # TASK1
    # we convert event to string and convert it
    print(str(event))
    # the below line will fetch the bucket name from the event dictionary
    bucket = event['Records'][0]['s3']['bucket']['name']
    # getfile name
    filename = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(filename)

    # TASK2
    s3Client = boto3.client('s3')
    jsonObject = s3Client.get_object(Bucket=bucket, Key=filename)
    # Body Stream Reader
    jsonFileReader = jsonObject['Body'].read()
    # Json module loads method takes the reader and converts into a file
    jsonDict = json.loads(jsonFileReader)
    # jsonDict is the dictionary. we pass to dynamo db

    # TASK3
    dynamodb = boto3.resource('dynamodb')
    #Set the table name
    table = dynamodb.Table('employees')
    #put_item expects a jsob object as item value.
    table.put_item(Item=jsonDict)
    print('check the dynamo db')
    #Refer aws boto3 docs for more detailed information about the methods used here
    return 'Test_version'


