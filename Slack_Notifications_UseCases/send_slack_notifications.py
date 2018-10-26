#Send slack notifications through lambda function
#TASK1
#The slack_web_hook_url is taken from the slack profile: wew can find web hook over there
#TASK2
#Create lamnda function
#Define the send_slack as the lambda fucntion handler  in PIA: filename.function
#TASK3
#Configure the cloud watch alarm:
#Create a rule which is event pattern type for event source
#ServiceName: EC2 #Event type: EC2 Instance State change notification
#Specific state: Stopped
#Select the lambda function at target part
#TASK4
#Test the lamnda function: Stop the EC2 instance and check the slack profile

from botocore.vendored import requests
#import requests
import json
slack_web_hook_url='https://hooks.slack.com/services/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'

#json method takes the slack message in json format and sends as string
def send_slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instane Stopped'}
    response = requests.post(slack_web_hook_url,data=json.dumps(slack_message))
    return response