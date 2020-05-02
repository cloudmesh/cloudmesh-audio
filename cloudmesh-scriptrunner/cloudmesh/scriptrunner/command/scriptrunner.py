from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.scriptrunner.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.scriptrunner import GlueRunner
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters


class ScriptrunnerCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_scriptrunner(self, args, arguments):
        """
        ::

          Usage:
                scriptrunner --file=FILE --bucket=BUCKET --upload=UPLOAD
                scriptrunner --file=FILE --bucket=BUCKET --delete=DELETE
                scriptrunner --bucket=BUCKET --list=LIST
                scriptrunner --job_name=JOB_NAME --role_name=ROLE_NAME --cmd_name=CMD_NAME --bucket=BUCKET --file=FILE --create_job=CREATE_JOB
                scriptrunner --job_name=JOB_NAME --delete_job=DELETE_JOB
                scriptrunner --job_name=JOB_NAME --run_job=RUN_JOB

          This command does some useful things.

          Arguments:
              FILE   a file name
              BUCKET a bucket name
              UPLOAD TRUE
              LIST  TRUE
              DELETE TRUE
              CREATE_JOB TRUE
              DELETE_JOB TRUE
              RUN_JOB TRUE
              JOB_NAME a glue job name
              ROLE_NAME a IAM Role used to create AWS GLUE job
              CMD_NAME a name of glue job's command

          Options:
              -f      specify the file
              -b      specify the s3 bucket name

        """

        map_parameters(arguments,
                       'upload', 'list', 'delete', 'create_job')

        arguments.FILE = arguments['--file'] or None
        arguments.BUCKET = arguments['--bucket'] or None
        arguments.UPLOAD = arguments['--upload'] or None
        arguments.DELETE = arguments['--delete'] or None
        arguments.LIST = arguments['--list'] or None
        arguments.CREATE_JOB = arguments['--create_job'] or None
        arguments.DELETE_JOB = arguments['--delete_job'] or None
        arguments.RUN_JOB = arguments['--run_job'] or None
        arguments.JOB_NAME = arguments['--job_name'] or None
        arguments.ROLE_NAME = arguments['--role_name'] or None
        arguments.CMD_NAME = arguments['--cmd_name'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.UPLOAD:
            print("option upload")
            gr = GlueRunner.GlueRunner(arguments.FILE, arguments.BUCKET)
            gr.upload()

        if arguments.DELETE:
            print("option delete")
            gr = GlueRunner.GlueRunner(arguments.FILE, arguments.BUCKET)
            gr.delete()

        if arguments.LIST:
            print("option list")
            gr = GlueRunner.GlueRunner(arguments.FILE, arguments.BUCKET)
            gr.list()

        if arguments.CREATE_JOB is not None:
            print("create Glue JOB")
            gr = GlueRunner.GlueRunner(arguments.BUCKET, arguments.FILE, arguments.JOB_NAME, arguments.ROLE_NAME, arguments.CMD_NAME)
            gr.create_job()

        if arguments.DELETE_JOB is not None:
            print("Delete Glue JOB")
            gr = GlueRunner.GlueRunner(glue_job=arguments.JOB_NAME)
            gr.delete_job()

        if arguments.RUN_JOB is not None:
            print("Run Glue JOB")
            gr = GlueRunner.GlueRunner(glue_job=arguments.JOB_NAME)
            gr.run_job()

        return ""
