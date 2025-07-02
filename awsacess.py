#Python Program for creating a connection
import boto3

ec2 = boto3.client('ec2',
				'us-east-1',
				aws_access_key_id='AKIAUYPNA4JPTKMDKU6J',
				aws_secret_access_key='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')

#This function will describe all the instances
#with their current state 
response = ec2.describe_instances()
print(response)
