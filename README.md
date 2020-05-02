# Objective

With this project, additional features has been implemented in Cloudmeash (cms) framework to enable users to upload and run any python scripts seamlessly in cms command line and thus
behind the scene launches AWS services like AWS Glue and S3 to upload any python scripts and run the job seamlessly and store any output to the S3 target in a serverless mehtod. 

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

mkdir cm
cd cm

```

Run these commands to install cloudmesh-seechi

```
pip install cloudmesh-cmd5
pip install cloudmesh-sys
git clone https://github.com/cloudmesh/cloudmesh-scriptrunner.git (to be renamed)
cd cloudmesh-scriptrunner
pip install -e .

```

Once installation is complete, run help command to check if installation is successful.

```
cms scriptrunner help

```

## Command Line Execution

### Commands To Run Prediction

#### Upload, List and Delete any python scrips through cms command.

This is the file on which prediction would run.

For upload, run command

```
cms scriptrunner --upload=TRUE --file=./pythonjob.py --bucket=<s3bucketname>
```

For delete, run command 

```
cms scriptrunner --delete=TRUE --file=./pythonjob.py --bucket=<s3bucketname>
```

#### Run list through cms command

```
cms scriptrunner --list=TRUE --file=./pythonjob.py --bucket=<s3bucketname>
```


This graph is saved under root folder as 'ab.png'.


#### Architecure of this workflow in AWS


![Architecture Diagram](image/abc.png) 

