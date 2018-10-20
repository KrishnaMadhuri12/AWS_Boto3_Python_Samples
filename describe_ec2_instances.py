import boto3
#Retrieve the ec2 client
ec2Client =  boto3.client('ec2')
#Describes one or more of your instances
#If we specify an instanceID that is not valid, an error is returned
#If we do not own the instance then it is not included in the returned results
responseDescribe = ec2Client.describe_instances(
    InstanceIds=[
                'i-0ec5d809365edb494',
                'i-03a25d83c28d7788e'
                ],
    DryRun=False,
    )

#Response Object is parsed to view the instances information as output
for instance in responseDescribe['Reservations']:
    print("{}".format(instance['Instances']))

#if we want to print only the instance public IP address
#double for loop

for reservation in responseDescribe['Reservations']:
    for instance in reservation['Instances']:
        print("The public IP address is {} .".format(instance.get('PublicIpAddress')))

#---Filters-----
#calling the filters on top of the repsonseObject

response = ec2Client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['stopped']
}])
    
for reservation in responseDescribe['Reservations']:
    for instance in reservation['Instances']:
        print("The public IP address is {} .".format(instance.get('InstanceId0')))

#Filter through tags on ec2 instances
