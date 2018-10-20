import boto3
ec2Client = boto3.client('ec2')
#review the aws ec2 documentation
#run_instances(**kwargs) helps in launching the specified instances using an AMI
#bunch of arguments, instance type, mandatory fields-->min and max count
response = ec2Client.run_instances(ImageId='ami-0ff8a91507f77f867',
			InstanceType='t2.micro',
			MinCount=1,
			MaxCount=1)
#creates new ec2 instance in aws management console
#access instances returned in the dic stored in var response
#Dictionary gives key and pair, Instances is the key and we are trying
#pull the instance id
for instance in response['Instances']:
	print(instance['InstanceId'])
