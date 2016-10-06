#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DLClouds CLI

Assemble, Train and Deploy Deep Neural Nets in AWS

"""

from __future__ import unicode_literals
from __future__ import division

import sys

CLI_COMMANDS = [
    'init',
    'start',
    'deploy',
    'pull',
    'shutdown',
]

class DLCloudsCLI(object):

    # DLClouds settings
    dlclouds_settings = None

    def handle(self):
        pass

def handle(): # pragma: no cover
    """
    Main program execution handler.
    """

    try:
        cli = DLCloudsCLI()
        sys.exit(cli.handle())
    except SystemExit as e: # pragma: no cover
        sys.exit(e.code)

    except KeyboardInterrupt: # pragma: no cover
        sys.exit(130)
    except Exception as e:
        click.echo("Oh no! An " + click.style("error occurred", fg='red', bold=True) + "! :(")
        sys.exit(-1)

if __name__ == '__main__': # pragma: no cover
    handle()
