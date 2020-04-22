import os
import cv2
import shutil
from pathlib import Path
from cloudmesh.common.util import path_expand
import glob
from cloudmesh.common.Shell import Shell
import boto3

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
            # Add boto3 api call to upload file to S3
        except Exception as e:
            print("Error uploading file: " + str(e))

    def list(self, name=None):
        # lists videos and tells us info about them in json format
        # is training
        # images
        # size
        # non = all, if name only that
        # use glob.glob in teh des dir

        # list all files in input folder

        raise NotImplementedError

    def create_glue_job(self):
        # TODO
        # Create glue job

    def removeFile(self,file=None):

        if file is None:
            #remove all video file
            files = os.listdir(self.dest)
            for file in files:
                extn = file.split('.')[-1]
                if extn in self.valid_extn:
                    os.remove(os.path.join(self.dest, file))
        else:
            os.remove(os.path.join(self.dest,file))
    
    def run_script(self, file=None):
        # TODO
        # ?Start glue job



if __name__== "__main__":
    #print(__import__("Video"))
    audio = Audio()
    #v.upload()


