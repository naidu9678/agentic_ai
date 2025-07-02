import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    """
    Sends an email using Gmail SMTP.
    
    :param subject: Email subject.
    :param body: Email body content.
    :param to_email: Recipient email address.
    """
    from_email = "2024mt03062@wilp.bits-pilani.ac.in"  # Replace with your Gmail address
    from_password = "Anp@9678"  # Use App Password if 2FA enabled

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure connection
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def provision_virtual_machine():
    """
    Launches an EC2 instance with predefined constants and retrieves its public IP, Public DNS, and Login Username.
    
    :return: Dictionary containing the Public IP, Public DNS, and Login Username, or None if an error occurs.
    """
    # Constants for EC2 configuration
    REGION = 'us-east-1'
    AWS_ACCESS_KEY = 'AKIAUYPNA4JPTKMDKU6J'
    AWS_SECRET_KEY = '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'
    INSTANCE_TYPE = 't2.micro'
    IMAGE_ID = 'ami-0df8c184d5f6ae949'
    MIN_COUNT = 1
    MAX_COUNT = 1
    DEFAULT_LOGIN_USERNAME = 'ec2-user'  # Update based on your AMI type

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
        
        # Extract instance ID
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 instance launched successfully! Instance ID: {instance_id}")
        
        # Wait for the instance to be in the running state
        print("Waiting for the instance to be in the 'running' state...")
        ec2_resource = boto3.resource('ec2',
                                       region_name=REGION,
                                       aws_access_key_id=AWS_ACCESS_KEY,
                                       aws_secret_access_key=AWS_SECRET_KEY)
        instance = ec2_resource.Instance(instance_id)
        instance.wait_until_running()
        
        # Refresh instance attributes
        instance.reload()
        
        # Retrieve the public IP and Public DNS
        public_ip = instance.public_ip_address
        public_dns = instance.public_dns_name
        
        print(f"Public IP of instance {instance_id}: {public_ip}")
        print(f"Public DNS of instance {instance_id}: {public_dns}")
        print(f"Default Login Username: {DEFAULT_LOGIN_USERNAME}")
        
        # Send email with the details
        email_subject = "EC2 Instance Provisioned"
        email_body = f"Your EC2 instance (ID: {instance_id}) has been provisioned successfully.\n\n" \
                     f"Public IP: {public_ip}\nPublic DNS: {public_dns}\nLogin Username: {DEFAULT_LOGIN_USERNAME}"
        send_email(email_subject, email_body, "naidu9678@gmail.com")
        
        return {
            'Public IP': public_ip,
            'Public DNS': public_dns,
            'Login Username': DEFAULT_LOGIN_USERNAME
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    result = provision_virtual_machine()
    if result:
        print(f"Provisioned instance details: {result}")
    else:
        print("Failed to provision the instance or retrieve details.")
