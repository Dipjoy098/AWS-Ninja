Understanding the Problem: Amazon EBS provides different volume types, each designed to cater to specific workload requirements. GP2 volumes offer a balance between performance and cost, while GP3 volumes provide higher performance at a lower price per gigabyte. Converting GP2 volumes to GP3 when appropriate can lead to significant cost savings without sacrificing performance.

Solution Overview: To automate the conversion process, we will utilize the power of AWS CloudWatch Events and Lambda. CloudWatch Events enables us to monitor events within our AWS environment, while Lambda allows us to execute custom code in response to those events. By combining these services, we can seamlessly convert GP2 volumes to GP3 type whenever specific conditions are met.

TABLE OF CONTENTS
📍 INTRODUCTION

📍 HIGH LEVEL DESIGN 📐🖌️

🔹 Create a new IAM role

🔹 Develop the lambda function code

🔹 Create a lambda function

🔹 Configure the lambda function

🔹 Set up a cloud watch event

🔹 Test the lambda function

🔹 Verify the EBS volume conversion

📍 CONCLUSION

📍 RESOURCES TO FOLLOW ALONG BY

📍 Introduction:

1. In this tutorial, we will walk through the process of implementing and executing an AWS Lambda function using a CloudWatch Event. We will convert an EBS volume from gp2 to gp3 using Python and the Boto3 library.

2. Prerequisites: Before starting this tutorial, make sure you have the following prerequisites:

* An AWS account with appropriate permissions to create and manage Lambda functions and CloudWatch events.
Python and Boto3 library installed on your local machine for development.
An understanding of AWS Lambda and basic Python programming.

📍 High-Level Design 📐🖌️:

Behold, a glimpse into the magnificent high-level design of AWS Samurai! The interface, adorned with the essence of our noble warrior, allows you to configure and customize the behavior of Lambda functions. Harness their power to shape the destiny of your AWS governance, ensuring optimal performance, unwavering security, and unparalleled efficiency. The screenshot presented showcases the awe-inspiring AWS Samurai interface, a portal to victory in the realm of AWS governance! 🎨👨‍💻🖥️


🔹 Step 1: Create a new IAM role
1. Go to the IAM service in the AWS Management Console.
2. Click on “Roles” in the left navigation pane.
3. Click “Create role”.
4. Select “AWS service” as the trusted entity and choose “Lambda” as the service.
5. Attach the necessary policies for Lambda execution and EC2 volume modification.
6. Provide a name for the role and create it.
7. Attaching to Policies to the Role:

8. Policies for AWS Lambda:

9. Policies rule for AWS EBS Volume:

🔹 Step 2: Develop the Lambda function code
Set up your development environment with Python and Boto3.
Create a new Python file, e.g., lambda_function.py.
Copy and paste the following code into the file:
import json
import boto3
def convert_volume_to_gp3(volume_arn):
    ec2_client = boto3.client('ec2')
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
def lambda_handler(event, context):
    volume_arn = event['resources'][0]
    volume_id = convert_volume_to_gp3(volume_arn)
    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType = 'gp3',
    )
Save the file.

🔹 Step 3: Create a Lambda function
Go to the Lambda service in the AWS Management Console.
Click “Create function”.
Select “Author from scratch” as the blueprint.
Provide a name for the function and choose Python as the runtime.
Select the IAM role you created in Step 1.
Click “Create function”.
🔹 Step 4: Configure the Lambda function
In the function configuration page, scroll down to the “Function code” section.
Choose “Upload a .zip file” in the “Code entry type” dropdown.
Click on “Upload” and select the lambda_function.py file you created.
Set the “Handler” field to lambda_function.lambda_handler.
Set the “Timeout” according to your requirements.
Click “Save”.
🔹 Step 5: Set up a CloudWatch Event
Go to the CloudWatch service in the AWS Management Console.
Click on “Events” in the left navigation pane.
Click “Create rule”.
Choose “Event pattern” and select the desired event source (e.g., EC2).
Configure the event pattern based on your requirements.
Select the target as “Lambda function” and choose the Lambda function you created in Step 3.
Click “Configure details”.
Provide a name and description for the rule.
Click “Create rule”.
🔹 Step 6: Test the Lambda function
Go back to the Lambda service in the AWS Management Console.
Open the function you created in Step 3.
Click on the “Test” button in the top-right corner.
Select “Create new test event” from the dropdown.
Provide a name for the test event, e.g., “TestEvent”.
Copy and paste the following JSON payload into the event body:
{
  "resources": [
    "arn:aws:ec2:region:account-id:volume/volume-id"
  ]
}
Replace region, account-id, and volume-id with the actual values corresponding to your AWS environment.
Click “Create”.
Click on the “Test” button again to execute the Lambda function with the test event.
Monitor the execution results and check the CloudWatch logs for any error messages.
🔹 Step 7: Verify the EBS volume conversion
Go to the EC2 service in the AWS Management Console.
Navigate to the volume that you specified in the test event.
Check the volume details to verify that it has been converted to gp3.
Ensure that the volume attributes (such as IOPS and throughput) meet your desired configuration.
Created EBS Volume of type GP2:


Modified EBS Volume to type GP3 as per Organization Governance Compliance:


📍 Conclusion:
In this tutorial, we covered the step-by-step process of implementing and executing an AWS Lambda function using a CloudWatch Event. We converted an EBS volume from gp2 to gp3 using Python and the Boto3 library. You can now apply this knowledge to automate various tasks and workflows using Lambda and CloudWatch in your AWS environment.

Remember to properly configure event patterns and IAM permissions to ensure the security and reliability of your serverless applications.
