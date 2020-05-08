import os
# import shutil
# from pathlib import Path
from cloudmesh.common.util import path_expand
from cloudmesh.common.Shell import Shell
import boto3
# import logging
s3 = boto3.client('s3')
glue = boto3.client('glue')

class GlueRunner:
    valid_extn = ["py"]

    def __init__(self, file=None, bucket=None, glue_job=None, glue_role=None, cmd_name=None):
        if file is not None:
            self.file = path_expand(file)
        self.bucket = bucket
        self.glue_job = glue_job
        self.glue_role = glue_role
        self.cmd_name = cmd_name
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
            #print (response) (use cloudmesh print fun)
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
        except Exception as e:
            print("Unable to Delete a file: " + str(e))

    def create_job(self, kind="create_job"):
        """Create AWS Glue Job based on python script located at S3 bucket

        :param job_name: Name of Glue Job
        :param iam_role: IAM Role created with required permission
        :param script_location: S3 bucket where python script uploaded
        :return: True if file was uploaded, else False
        """
        try:
            # Create glue job
            if self.file is not None:
                file_name = self.file.split('/')[-1]
            response = glue.create_job(
                Name=self.glue_job,
                Role=self.glue_role,
                GlueVersion='1.0',
                Command={
                    'Name': "testcmd",
                    'ScriptLocation': "s3://"+self.bucket+"/scripts/"+file_name,
                    'PythonVersion': '2'
                }
            )

        except Exception as e:
            print("Unable to create a AWS Glue job: " + str(e))

    def delete_job(self, kind="delete_job"):
        """Delete an existing AWS Glue Job based on python script located at S3 bucket

                :param job_name: Name of Glue Job
                """
        try:
            # Delete glue job
            response = glue.delete_job(
                JobName=self.glue_job
            )
        except Exception as e:
            print("Unable to Delete a AWS Glue job: " + str(e))

    def run_job(self, file="run_job"):
        """Run an existing AWS Glue Job based on python script located at S3 bucket

        :param job_name: Name of Glue Job
        """
        try:
            # Run glue job
            response = glue.start_job_run(
                JobName=self.glue_job
            )
        except Exception as e:
            print("Unable to execute/run a AWS Glue job: " + str(e))


if __name__ == "__main__":
    pass

