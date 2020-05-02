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
# test

class ScriptrunnerCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_scriptrunner(self, args, arguments):
        """
        ::

          Usage:
                scriptrunner --file=FILE --bucket=BUCKET --upload=UPLOAD
                scriptrunner --bucket=BUCKET list

          This command does some useful things.

          Arguments:
              FILE   a file name
              BUCKET a bucket name
              UPLOAD TRUE

          Options:
              -f      specify the file
              -b      specify the s3 bucket name

        """

        map_parameters(arguments,
                       'upload')

        map_parameters(arguments,
                       'list')

        arguments.FILE = arguments['--file'] or None
        arguments.BUCKET = arguments['--bucket'] or None
        arguments.UPLOAD = arguments['--upload'] or None
        arguments.LIST = arguments['--list'] or None


        VERBOSE(arguments)

        m = Manager()

        if arguments.UPLOAD:
            print("option upload")
            gr = GlueRunner.GlueRunner(arguments.FILE, arguments.BUCKET)
            gr.upload()

        # if arguments.FILE:
        #     print("option a")
        #     m.list(path_expand(arguments.FILE))

        elif arguments.LIST:
            print("option list")
            gr = GlueRunner.GlueRunner(arguments.FILE, arguments.BUCKET)
            gr.list()
        #     m.list("just calling list without parameter")

        return ""
