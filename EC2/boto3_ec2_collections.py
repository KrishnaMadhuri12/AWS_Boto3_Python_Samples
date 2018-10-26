import boto3
ec2 = boto3.resource('ec2')
#a collection of instances
#returns a list of instances
for instance in ec2.instances.all():
    print('Instance ID is {} and Instance Type is {}'.format(instance.instance_id,instance.instance_type))

#filter on collections
#display the instances based on availabiliy zones
for instance in ec2.instance.filter(Filters=[
    {
        'Name':'availability-zone',
        'Values': ['us-east-1c']
    }
]):
    print('Instance ID is {} and Instance Type is {}'.format(instance.instance_id,instance.instance_type))

#get all instances and perform start or stop
#intead of providing the ec2 client method start_instances and stop_instances. through resource we can apply filtersfollowed by.stop() method
ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()

