<<<<<<< HEAD
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
=======
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
>>>>>>> 958736ba083778456ca41ef88adb3e3c75ef1d70
    print(bucket.name)