#Python Program for creating a connection
import boto3

#Function for connecting to EC2 
ec2 = boto3.client('ec2',
				'us-east-1',
				aws_access_key_id='AKIAUYPNA4JPTKMDKU6J',
				aws_secret_access_key='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')

#Function for running instances
conn = ec2.run_instances(InstanceType="t2.micro",
						MaxCount=1,
						MinCount=1,
						ImageId="ami-0df8c184d5f6ae949")
print(conn)
