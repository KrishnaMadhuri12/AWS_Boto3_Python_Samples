#UseCase: part of disaster recovery plan, create images on a regular schedule
# and copy those images to different region
#when one fails we can pull up the other region
#FollowUP:
#we can schedule this task using a lamabda function
import boto3

#TASK1: CREATE IMAGES
source_region = 'us-east-1'
ec2_resource = boto3.resource('ec2', region_name=source_region)

instances = ec2_resource.instances.filter(InstanceIds=['i-0b5a5b1c83290df03'])

image_ids=[]

for instance in instances:
    image = instance.create_image(Name='Demo BOTO3- '+instance.id,Description="Demo Boto3"+instance.id)
    image_ids.append(image.id)
print("Images to be copied are {}".format(image_ids))

#TASK2: WAIT FOR IMAGES TO BE AVAILABLE
#Get waiter to make the program wait
#the waiter here calls the describe_images multiple times for every 15 seconds
#if the image isnt created then an error is returned

ec2_client = boto3.client('ec2',region_name=source_region)
waiter = ec2_client.get_waiter('image_available')

#Wait for the image to be ready
waiter.wait(Filters=[
    {
        'Name':'image-id',
        'Values':image_ids
    }
])

#TASK3: COPY THOSE IMAGES
#copy to different region

destination_region = 'us-west-1'
client2 = boto3.client('ec2', region_name=destination_region)
for image_id in image_ids:
    client2.copy_image(Name='Boto3 Copy'+image_id,SourceImageId=image_id,SourceRegion=source_region)

#output: Images to be copied are ['ami-01b6e311c367182a8']


