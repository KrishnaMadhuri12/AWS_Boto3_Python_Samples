#usecase: send email notification when a specific instance(s)
# stops in the production environment
#Ec2->event(Stip)->lambda->snstopic->subscribers
#TASK1: Configure the lambda function to sns topic
#TASK2: Trigger from cloud watch rule
#TASK3: can make it specific instances of the prd_server
import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    topic_arn = 'arn:aws:sns:us-east-1:260147304029:prod_alerts'
    message = 'Prd server stopped please look into it'
    sns_client.publish(TopicArn=topic_arn, Message=message)