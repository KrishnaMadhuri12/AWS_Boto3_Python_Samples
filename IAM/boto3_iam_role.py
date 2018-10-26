#sample on updating IAM roles, retrieval
import boto3
iamClient =  boto3.client('iam')
response = iamClient.get_user(
    UserName = 'krishna_united'
)
account_summary = iamClient.get_account_summary()
print(account_summary)