# from aws_cdk import core as cdk
# from aws_cdk import aws_s3 as _s3
from aws_cdk import(
    core as cdk,
    aws_s3 as _s3,
    aws_iam as _iam
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
# from aws_cdk import core


class FirstOneStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # _s3.Bucket(
        #     self,
        #     id='myS3Bucket',
        #     bucket_name='aws-cdk-bucket-2021',
        #     versioned=False,
        #     encryption=_s3.BucketEncryption.S3_MANAGED,
        #     block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        # )

        # my_bucket = _s3.Bucket(
        #     self,
        #     id='myNewBucket'
        # )

        myIAMGroup = _iam.Group(self, id='IAMGroup-1',
                                group_name='aws-cdk-group')

        # output_1 = cdk.CfnOutput(self, id='my-bucket-output-1',
        #                          value=my_bucket.bucket_name, description='The newly created bucket', export_name='my-bucket-output-1')
