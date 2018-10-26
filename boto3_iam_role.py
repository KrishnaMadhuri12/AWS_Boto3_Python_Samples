<<<<<<< HEAD
#sample on updating IAM roles, retrieval
import boto3
iamClient =  boto3.client('iam')
response = iamClient.get_user(
    UserName = 'krishna_united'
)
account_summary = iamClient.get_account_summary()
=======
#sample on updating IAM roles, retrieval
import boto3
iamClient =  boto3.client('iam')
response = iamClient.get_user(
    UserName = 'krishna_united'
)
account_summary = iamClient.get_account_summary()
>>>>>>> 958736ba083778456ca41ef88adb3e3c75ef1d70
print(account_summary)