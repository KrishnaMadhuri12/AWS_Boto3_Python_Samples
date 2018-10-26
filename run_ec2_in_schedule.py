<<<<<<< HEAD
#UseCase: Schedulling ec2 instances, start instance at 9am and stop them by 6am
#Conditiom: Instances with tag key="Type" and Value="Scheduled"
#Condition: Monday to Friday
#conditios are usually applied as filters on ec2 instances
#IAM Role for lambda: EC2 instance(permissions on ec2 start, stop), cloud watch logds
#Create lambda function
#Task1:
#Create ec2 instances with the tag value

#Task2: Schedule this lambad function
#schedule can be from lambda or also from cloud watch console
#Using Cron expression: 0 9 ? * MON-FRI *

#Explanation for stop ec2 instance
#for stop create a new cron expression to stop the instances
#matching the tag conditions

import boto3

# schedule ec2 istances
ec2 = boto3.resource('ec2')


def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:Type',
            'Values': ['Scheduled']
        }
    ]
    # We need decriber insances permission to apply the filter
    instances = ec2.instances.filter(Filters=filter)

    for instance in instances:
        instance.start()
    return 'Hello'
=======
#UseCase: Schedulling ec2 instances, start instance at 9am and stop them by 6am
#Conditiom: Instances with tag key="Type" and Value="Scheduled"
#Condition: Monday to Friday
#conditios are usually applied as filters on ec2 instances
#IAM Role for lambda: EC2 instance(permissions on ec2 start, stop), cloud watch logds
#Create lambda function
#Task1:
#Create ec2 instances with the tag value

#Task2: Schedule this lambad function
#schedule can be from lambda or also from cloud watch console
#Using Cron expression: 0 9 ? * MON-FRI *

#Explanation for stop ec2 instance
#for stop create a new cron expression to stop the instances
#matching the tag conditions

import boto3

# schedule ec2 istances
ec2 = boto3.resource('ec2')


def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:Type',
            'Values': ['Scheduled']
        }
    ]
    # We need decriber insances permission to apply the filter
    instances = ec2.instances.filter(Filters=filter)

    for instance in instances:
        instance.start()
    return 'Hello'
>>>>>>> 958736ba083778456ca41ef88adb3e3c75ef1d70
