# Objective

With this project, additional features has been implemented in Cloudmeash (cms) framework to enable users to upload and run any python scripts seamlessly in cms command line and thus
behind the scene launches AWS services like AWS Glue and S3 to upload any python scripts and run the job seamlessly and store any output to the S3 target in a serverless mehtod. 


#### Architecure of this workflow in AWS

![Architecture Diagram](images/cms-scriptrunner.png) 


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



