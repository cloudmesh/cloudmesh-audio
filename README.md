# Objective

With this project, additional features has been implemented in Cloudmesh (cms) framework to enable users to upload and run any python scripts seamlessly and server-less way using cms command line and thus behind the scene launches the required AWS services like AWS Glue, AWS S3 and AWS lambda script to upload any python scripts and execute user provided ad-hoc method or automated way for any data source update and stores the output to the target S3 folder.

#### Architecture of this workflow in AWS

![Architecture Diagram](./images/cms-scriptrunner.png) 

### Architecture walk-through and cms-scriptrunner demo
[![Watch the video](./images/cms-scriptruner-demo.mp4)]


#### What is AWS Glue?
AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams. AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries. AWS Glue is serverless, so there’s no infrastructure to set up or manage.

AWS Glue is designed to work with semi-structured data. It introduces a component called a dynamic frame, which you can use in your ETL scripts. A dynamic frame is similar to an Apache Spark dataframe, which is a data abstraction used to organize data into rows and columns, except that each record is self-describing so no schema is required initially. With dynamic frames, you get schema flexibility and a set of advanced transformations specifically designed for dynamic frames. You can convert between dynamic frames and Spark dataframes, so that you can take advantage of both AWS Glue and Spark transformations to do the kinds of analysis that you want.

You can use the AWS Glue console to discover data, transform it, and make it available for search and querying. The console calls the underlying services to orchestrate the work required to transform your data. You can also use the AWS Glue API operations to interface with AWS Glue services. Edit, debug, and test your Python or Scala Apache Spark ETL code using a familiar development environment.

#### What is S3?
Amazon Simple Storage Service is storage for the Internet. It is designed to make web-scale computing easier for developers.

Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web. It gives any developer access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of web sites. The service aims to maximize benefits of scale and to pass those benefits on to developers.

This guide explains the core concepts of Amazon S3, such as buckets, access points, and objects, and how to work with these resources using the Amazon S3 application programming interface (API). 

## Prerequisite

python 3.6.9

## Installation

### Create Virtual Environment ENV3

```

python -m venv ENV3

```

In case of multiple version of python, use command 

```

py -3.6 -m venv ENV3

```

This command will create a new ENV3 environment using python 3.6 version.


### Installation of cloudmesh-scriptrunner (to be renamed from cloudmesh-audio to cloudmesh-scriptrunner)

Start from home directory. Activate python virtual environment before installation. 
Command to activate

For Windows:

```

ENV3/Scripts/activate.bat

```

For Linux:

```

source ENV3/bin/activate

```

Create a cm folder 

```

mkdir cm-scriptrunner
cd cm-scriptrunner

```

Run these commands to install cloudmesh-scriptrunner

```
pip install cloudmesh-cmd5
pip install cloudmesh-sys
git clone https://github.com/cloudmesh/cloudmesh-scriptrunner.git (to be renamed)
cd cloudmesh-scriptrunner
pip install -e .

```

```
AWS prerequisite (Important):
    Before executing any cms command, please make sure to validate the below AWS prerequisites:

    1. AWS S3 bucket in a region where you are intend to store and execute Glue jobs.
    2. Make sure following folders created under your S3 bucket:
            example:
                   Bucket Name: cms-s3-bucket
                   Folders: 
                            cms-s3-bucket/scripts  (default locaiton to upload your python scripts)
                            cms-s3-bucket/input-data (default location to store your data (if any) to be processed)
                            cms-s3-bucket/output-data (default location to store your output results (if any) to be saved)
    3. Make sure right access & permissions configurations to secure your S3 bucket and files.
        ## Reference
        * <https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/>
        * <https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html>    
    
    4. Create IAM Role and Policy to allow your IAM user to create/delete/run Glue Jobs
            example:
                IAM role Name : GlueJobRole
                IAM Policy Name: GlueDataAccessPolicyForS3
                IAM Policy (example):
                    {
                        "Version": "2012-10-17",
                        "Id": "abcd-xxx-xxx-xxx-xxx-xxxx",
                        "Statement": [
                                {
                                    "Sid": "GlueDataAccessPermissionsForS3FullAccess",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject",
                                        "s3:PutObject",
                                        "s3:DeleteObject"
                                    ],
                                    "Resource": [
                                        "arn:aws:s3:::<replace-your-s3-bucket>/*"
                                    ]
                                },
                                {
                                    "Sid": "GlueDataAccessPermissionsForS3ListBucket",
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:ListBucket"
                                    ],
                                    "Resource": [
                                        "arn:aws:s3:::<replace-your-s3-bucket>"
                                    ]
                                }
                            ]
                        }
```

Once installation is complete, run help command to check if installation is successful.

```
cms scriptrunner help

```

## Command Line Execution

#### Upload, List and Delete any python scrips through cms command.

#### Try: "cms help scriptrunner" to list the available commands
```
Usage:

      scriptrunner --file=FILE --bucket=BUCKET --upload
      scriptrunner --file=FILE --bucket=BUCKET --delete
      scriptrunner --bucket=BUCKET --list
      scriptrunner --job_name=JOB_NAME --role_name=ROLE_NAME --cmd_name=CMD_NAME --bucket=BUCKET --file=FILE --create_job
      scriptrunner --job_name=JOB_NAME --delete_job
      scriptrunner --job_name=JOB_NAME --run_job

This command does some useful things.
```


#### Upload new python script to S3 bucket under folder "script"
```
scriptrunner --file=<./python-file.py> --bucket=<s3-bucket-name> --upload
```

#### Delete python script uploaded already
```
scriptrunner --file=<./python-file.py> --bucket=<s3-bucket-name> --delete

```

#### Run list of scripts existing S3 bucket under "scripts" folder through cms command

```
scriptrunner --bucket=<s3-bucket-name> --list
```

#### Create AWS Glue Job

```
cms scriptrunner --job_name=<name-of-glue-job> --role_name=<name of IAM Role> --cmd_name=<command_name> --bucket=<name-of-s3-bucket> --file=<'python script'> --create_job
```

#### Delete an existing AWS Glue Job

```
cms scriptrunner --job_name=<name-of-glue-job> --delete_job
```

#### Run an existing AWS Glue Job

```
 cms scriptrunner --job_name=xxdex --run_job
```

