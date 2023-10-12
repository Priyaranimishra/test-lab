"""We need to write code that will query the meta data of an instance within AWS or
Azure or GCP and provide a json formatted output.
 """

#import Boto3 and JSON module
import boto3
import json

#Get the metadata from instance_id
def get_instance_metadata(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance_metadata = instance.metadata
    return instance_metadata

def main():
    instance_metadata = get_instance_metadata(instance_id)
    print(json.dumps(instance_metadata, indent=4))

if __name__ == '__main__':
    instance_id = input("Enter the instance ID: ")
    main()
    
