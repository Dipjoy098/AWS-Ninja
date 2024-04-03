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
