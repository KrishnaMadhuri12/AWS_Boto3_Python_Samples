#get the boto3 library
import boto3
#store the ec2Client
ec2Client =  boto3.client('ec2')
   
#Starting the instance id using the start_instances
responseStart = ec2Client.start_instances(
        InstanceIds=['i-03a25d83c28d7788e'],
        DryRun=False)
#the method start_instances returns a dict of StartingInstances
#print the responseStart instanceid
for instance in responseStart['StartingInstances']:
    print("----START-----")
    print("The instance with id {} started".format(instance['InstanceId']))

#Stop the running instance in aws management console
responseStop = ec2Client.stop_instances(
	InstanceIds=['i-03a25d83c28d7788e'],
	DryRun=False,
	Force=False)
#the above call returns the json object with stopping instance information
for instance in responseStop['StoppingInstances']:
    print("----STOP-----")
    print("The instance with id {} stopped".format(instance['InstanceId']))
    
#Terminate the instance: use method terminate_instances
#Shuts down one or more instances. idempotent,
#if you terminate an instance more than once, each call succeeds.
responseTerminate = ec2Client.terminate_instances(
        InstanceIds=['i-03a25d83c28d7788e'],
        DryRun=False)
#the method terminate_instances returns a dict of TerminatingInstances
#print the reponseTerminate instanceid
for instance in responseTerminate['TerminatingInstances']:
    print("----TERMINATE-----")
    print("The instance with id {} terminated".format(instance['InstanceId']))

