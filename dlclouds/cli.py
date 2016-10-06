#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DLClouds CLI - Assemble, Train and Deploy Deep Neural Nets in AWS

"""

from __future__ import unicode_literals
from __future__ import division

import click
import sys
import argparse
import pkg_resources
import json

CLI_COMMANDS = [
    'init',
    'start',
    'deploy',
    'pull',
    'shutdown',
]

class DLCloudsCLI(object):
    dlclouds_settings = None

    def version(self):
        version = pkg_resources.require("dlclouds")[0].version
        print(version)

    def handle(self, argv=None):
        help_message = "Please supply a command to execute. Can be one of: {}".format(', '.join(x for x in sorted(CLI_COMMANDS)))

        parser = argparse.ArgumentParser(description='DLClouds - Assemble, Train and Deploy Deep Neural Nets in AWS.\n')
        parser.add_argument('command', metavar='U', type=str, nargs='*', help=help_message)
        parser.add_argument('-version', nargs='?', help='print version')

        args = parser.parse_args()

        if args.version:
            self.version()
            sys.exit(0)

        command = args.command[0]

        if command not in CLI_COMMANDS:
            print("Command '{}' is not recognized. {}".format(command, help_message))
            return

        if command != 'init':
            try:
                self.load_settings()
            except ValueError as e:
                print("Error: {}".format(e.message))
                sys.exit(-1)

        if command == 'init':
            print 'init'
        if command == 'deploy':
            print 'deploy'
        elif command == 'push':
            print 'push'
        elif command == 'pull':
            print 'pull'
        elif command == 'shutdown':
            print 'shutdown'

    def load_settings(self, file_name="dlclouds_settings.json"):
        with open(file_name) as json_file:
            try:
                self.zappa_settings = json.load(json_file)
            except ValueError:
                raise ValueError("Unable to load the dlclouds_settings.json ")

def handle():
    try:
        cli = DLCloudsCLI()
        sys.exit(cli.handle())
    except SystemExit as e:
        sys.exit(e.code)

    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        click.echo(click.style("error occurred: {}".format(e), fg='red', bold=True))
        sys.exit(-1)

if __name__ == '__main__':
    handle()
