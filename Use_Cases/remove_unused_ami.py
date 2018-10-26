#UseCase:  Script to find unused ami and remove them from system
import boto3
ec2Client = boto3.client('ec2')
#TASK1
#get all the instances and image ids
#describe_instances() from there collect all ami ids
instances = ec2Client.describe_instances()
used_amis=[]
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])
print(used_amis)


#TASK2
#Eliminate duplicate Image Ids
def remove_duplicates(amis):
    unique_amis = []
    #loop through amis
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis
unique_amis = remove_duplicates(used_amis)
print(unique_amis)

#TASK3
#Get all the (custom) ami's from the account
#describe_images owner information is important so that it brings all the our amis
#available state
custom_images = ec2Client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
      ],
    Owners=['self']
)
#Respose type we have images
customAmis=[]
for image in custom_images['Images']:
    customAmis.append(image['ImageId'])

#compare the custom ami and used ami
#if custom ami is present in used ami then we dont delete

#TASK4: Delete AMIs
#deregister_images()
for custom_ami in customAmis:
    if custom_ami not in used_amis:
        print("deregistering amis {}".format(custom_ami))
        ec2Client.deregister_image(ImageId=image['ImageId'])
