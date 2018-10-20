#Task1: Get all ec2 instanex and take ebs snapshot.
#Pulling up the instances with tag 'backup's as yes
#Task2: send an email to the respective users with ebs snapshots
import boto3

ec2Resource = boto3.resource('ec2')
sns_Client = boto3.client('sns')

#Select the instances with tag:  BackUp and values as yes
backup_filter=[
    {
        'Name':'tag:BackUp',
        'Values':['yes']
    }
]
#to store all the snapshots in a listobject
snapshot_ids=[]
#returns list of ec2 instanes: loop through them
#instance object collection called volumes return volume class
for instance in ec2Resource.instances.filter(Filters = backup_filter):
    for vol in instance.volumes.all():
        #storing the return snapshot resource of create_snapshot method informatio into a variable
        snapshot = vol.create_snapshot(Description='Created by boto3')
        #take all the snapshot id into a list
        print('Snapshot information {}'.format(snapshot.snapshot_id))
        snapshot_ids.append(snapshot.snapshot_id)

#In the aws management console:
# create a new topic(examples'snapshot') and add email subscribers to the topic
#Topic ARN,subject, body of the email

#converting the snapshot_ids list into string and sending it in message
sns_Client.publish(
    TopicArn = 'arn:aws:sns:us-east-1:260147304029:Snapshots',
    Subject = 'EBS Snapshots Info',
    Message = str(snapshot_ids)
)

#Output through print: Snapshot information snap-07288d27364281d5b