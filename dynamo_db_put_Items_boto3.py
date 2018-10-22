#Load the boto3 nodule
import boto3

def first_method():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('employees')
    #inset Item into the tabale employees
    table.put_item(
        Item={
            'emplid':'2',
            'empl_name':'Krishna',
            'salary':2000
        }
    )
    print('Inserted a new record into the table employees')

first_method()