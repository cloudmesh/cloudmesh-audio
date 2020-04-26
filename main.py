import os
import cv2
import shutil
from pathlib import Path
from cloudmesh.common.util import path_expand
import glob
from cloudmesh.common.Shell import Shell
import boto3
import logging

class ScriptRunner:

    valid_extn = ["py"]

    def __init__(self, dest="~/.cloudmesh/audio"):
        # if none put it
        # in cwd/dest
        self.dest = path_expand(dest)
        # dir_path = os.path.dirname(path)
        Shell.mkdir(dest)
        print("dest Path:", self.dest)
        glue = boto3.client("glue")
        s3 = boto3.client("s3")


    def upload(self, filepath=None, kind="upload"):
        file = os.path.basename(filepath)
        try:
            pass
            #TODO:
            s3 = boto3.resource('s3')
            file_name = "/Users/psenthil/Desktop/MS/2020/CloudComputing-E-516/glue/dog.txt"
        
            """Upload a file to an S3 bucket

            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
            """

            # If S3 object_name was not specified, use file_name
            if object_name is None:
                object_name = file_name.split('/')[-1]

            s3.meta.client.upload_file(file_name, bucket, object_name)
            print("Uploaded file successfully")
            return True

        except Exception as e:
            print("Error uploading file: " + str(e))

    def list(self, name=None):
        s3 = boto3.resource('s3')
        """List a file to an S3 bucket

        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        try:
            my_bucket = s3.Bucket(bucket)
            for file in my_bucket.objects.all():
                print(file.key)
            # list all files in input folder
            list_file('demo0001')
        except Exception as e:
            print("Error uploading file: " + str(e))
        raise NotImplementedError

    def removeFile(self,file="my_File"):
        try:
            s3 = boto3.resource("s3")
            obj = s3.Object("aniketbucketpython", file)
            obj.delete()
        except:
            print("Unabled to Delete a file: " + str(e))
        raise NotImplementedError
      
    def create_glue_job(self):
        # TODO
        # Create glue job
        response = client.create_job(
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
        response = client.delete_job(
            JobName='string'
        )


    def run_script(self, file=None):
        # TODO
        # ?Start glue job
        response = client.start_job_run(
            JobName='string'
        )

if __name__== "__main__":
    #print(__import__("Video"))
    audio = Audio()
    #v.upload()


