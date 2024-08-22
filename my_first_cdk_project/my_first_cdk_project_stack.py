from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self, 
            id="bucket123", 
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            bucket_name="wits-moe-977864" # Use a globally unique bucket name
        )