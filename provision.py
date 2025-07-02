import boto3

def provision_virtual_machine():
    """
    Launches an EC2 instance with predefined constants.
    
    :return: Response from the AWS API
    """
    # Constants for EC2 configuration
    REGION = 'us-east-1' 
    AWS_ACCESS_KEY = 'AKIAUYPNA4JPTKMDKU6J' 
    AWS_SECRET_KEY = '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'
    INSTANCE_TYPE = 't2.micro'
    IMAGE_ID = 'ami-0df8c184d5f6ae949'
    MIN_COUNT = 1
    MAX_COUNT = 1

    try:
        # Connect to EC2
        ec2 = boto3.client('ec2',
                           region_name=REGION,
                           aws_access_key_id=AWS_ACCESS_KEY,
                           aws_secret_access_key=AWS_SECRET_KEY)
        
        # Launch the instance
        response = ec2.run_instances(
            InstanceType=INSTANCE_TYPE,
            MaxCount=MAX_COUNT,
            MinCount=MIN_COUNT,
            ImageId=IMAGE_ID
        )
        
        print("EC2 instance launched successfully!")
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    result = provision_virtual_machine()
    print(result)