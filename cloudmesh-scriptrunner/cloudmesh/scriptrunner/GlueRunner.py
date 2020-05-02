import os
# import shutil
# from pathlib import Path
from cloudmesh.common.util import path_expand
from cloudmesh.common.Shell import Shell
import boto3
# import logging
s3 = boto3.client('s3')


class GlueRunner:
    valid_extn = ["py"]

    def __init__(self, file=None, bucket=None):
        if file is not None:
            self.file = path_expand(file)
        self.bucket = bucket
        # dir_path = os.path.dirname(path)
        self.glue = boto3.client("glue")
        self.s3 = boto3.client("s3")

    def upload(self, kind="upload"):
        try:
            pass
            s3 = boto3.resource('s3')

            """Upload a file to an S3 bucket

            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
            """

            # If S3 object_name was not specified, use file_name
            if self.file is not None:
                file_name = self.file.split('/')[-1]

            s3.meta.client.upload_file(Filename=self.file, Bucket=self.bucket, Key="scripts/"+file_name)
            print("Uploaded file successfully")
            return True

        except Exception as e:
            print("Error uploading file: " + str(e))

    def list(self, kind="list"):
        """List a file to an S3 bucket

        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        try:
            response = s3.list_objects_v2(
                Bucket=self.bucket,
                Delimiter='/',
                Prefix='scripts/'
            )
            print (response)
            if "Contents" in response:
                for key in response["Contents"]:
                    print (key["Key"])
            # list all files in input folder
        except Exception as e:
            print("Error uploading file: " + str(e))

    def delete(self, kind="delete"):
        """List a file to an S3 bucket

        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        try:
            if self.file is not None:
                file_name = self.file.split('/')[-1]

            response = s3.delete_object(
                Bucket=self.bucket,
                Key="scripts/"+file_name
            )
            print (response)

        except Exception as e:
            print("Unable to Delete a file: " + str(e))

    def create_glue_job(self):
        # TODO
        # Create glue job
        response = self.glue.create_job(
            Name='CMSJOB',
            Role='GlueDataLakeServiceLinkRole',
            Command={
                'Name': 'CommandNAME',
                'ScriptLocation': 's3://demo0001/dog/glue/cms.py',
                'PythonVersion': '3'
            }
        )

    def delete_glue_job(self):
        # TODO
        # Create glue job
        response = self.glue.delete_job(
            JobName='string'
        )

    def run_script(self, file=None):
        # TODO
        # ?Start glue job
        response = self.glue.start_job_run(
            JobName='string'
        )


if __name__ == "__main__":
    pass
    # sr = GlueRunner("ScriptRunner.py", "demo0001")
    # sr.upload()
    # print(__import__("Video"))
    # audio = Audio()
    # v.upload()
