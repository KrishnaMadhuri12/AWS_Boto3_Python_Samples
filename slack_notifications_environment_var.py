<<<<<<< HEAD
#UseCase: To sent a slack notification on EC2 instance stop status
#Environment variables to send the web_hook_url of slack to the method
#encyrption on the environment variables

import botocore
#requests is not provided directly get it from botocore.vendored
from botocore.vendored import requests
import json
import os
import boto3
from base64 import b64decode

#slack_web_hook_url='https://hooks.slack.com/services/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'
#os module helps the function to fetch the environment variables passed/configured
slack_web_hook_url = os.environ['SLACK_WEBHOOK']

ENCRYPTED = os.environ['SLACK_WEBHOOK']
# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

slack_web_hook= DECRYPTED
#json method takes the slack message in json format and sends as string
def send_slack(event, context):
    print(str(event))
    print(DECRYPTED)
    slack_message = {'text': 'EC2 Instane Stopped'}
    response = requests.post(slack_web_hook,data=json.dumps(slack_message))
=======
#UseCase: To sent a slack notification on EC2 instance stop status
#Environment variables to send the web_hook_url of slack to the method
#encyrption on the environment variables

import botocore
#requests is not provided directly get it from botocore.vendored
from botocore.vendored import requests
import json
import os
import boto3
from base64 import b64decode

#slack_web_hook_url='https://hooks.slack.com/services/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'
#os module helps the function to fetch the environment variables passed/configured
slack_web_hook_url = os.environ['SLACK_WEBHOOK']

ENCRYPTED = os.environ['SLACK_WEBHOOK']
# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

slack_web_hook= DECRYPTED
#json method takes the slack message in json format and sends as string
def send_slack(event, context):
    print(str(event))
    print(DECRYPTED)
    slack_message = {'text': 'EC2 Instane Stopped'}
    response = requests.post(slack_web_hook,data=json.dumps(slack_message))
>>>>>>> 958736ba083778456ca41ef88adb3e3c75ef1d70
    return response.text