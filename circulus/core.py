# Circulus - file synchronization
# Copyright (C) 2015 Bruno Alano Medina <bruno@appzlab.com>
# See LICENSE

"""
core
~~~~~~

this module implements the basic functions to the
application, invoked by the binary and the __main__
file
"""

import circulus.fs
from circulus.config import Config

def main():
  """Main function

  This function initializes the project user interface and
  sync the directory with configured services
  """

  # Get configuration
  config = Config()

  # Monitor a directory based on the configuration
  circulus.fs.monitor(config.get('sync_path'))