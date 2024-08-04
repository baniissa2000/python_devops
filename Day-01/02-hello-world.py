import boto3
import json

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots(OwnerIds=['self'])

for snapshot in response['Snapshots']:
    volume_id = snapshot.get('VolumeId')
    print(snapshot['SnapshotId'], snapshot['Description'], snapshot['VolumeId'], snapshot['VolumeSize'] )
