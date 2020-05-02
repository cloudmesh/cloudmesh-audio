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
                scriptrunner --jobname=JOBNAME --rolename=ROLENAME --cmdname=CMDNAME --bucket=BUCKET --file=FILE --createjob=CREATEJOB

          This command does some useful things.

          Arguments:
              FILE   a file name
              BUCKET a bucket name
              UPLOAD TRUE
              LIST  TRUE
              DELETE TRUE
              CREATEJOB TRUE
              JOBNAME a glue job name
              ROLENAME a IAM Role used to create AWS GLUE job
              CMDNAME a name of glue job's command

          Options:
              -f      specify the file
              -b      specify the s3 bucket name

        """

        map_parameters(arguments,
                       'upload', 'list', 'delete', 'createjob')

        arguments.FILE = arguments['--file'] or None
        arguments.BUCKET = arguments['--bucket'] or None
        arguments.UPLOAD = arguments['--upload'] or None
        arguments.DELETE = arguments['--delete'] or None
        arguments.LIST = arguments['--list'] or None
        arguments.CREATEJOB = arguments['--createjob'] or None
        arguments.JOBNAME = arguments['--jobname'] or None
        arguments.ROLENAME = arguments['--rolename'] or None
        arguments.CMDNAME = arguments['--cmdname'] or None
        print (args)

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

        if arguments.CREATEJOB is not None:
            print("create Glue JOB")
            gr = GlueRunner.GlueRunner(arguments.BUCKET, arguments.FILE, arguments.JOBNAME, arguments.ROLENAME, arguments.CMDNAME)
            gr.createjob()

        return ""
