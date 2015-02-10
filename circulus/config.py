# Circulus - file synchronization
# Copyright (C) 2015 Bruno Alano Medina <bruno@appzlab.com>
# See LICENSE

"""
circulus configuration
~~~~~~~~~~~~~~~~~~~~~~~~

manage the configuration about the current application
of circulus
"""

import configparser # handle INI files configuration
import appdirs # get app directory on machine
import os
import configparser

class Config:
  """Configuration handler class

  This class is responsible for managing the information
  related to the application configuration on the local
  machine.

  Attributes:
    config_file (str): Handle the path to the configuration file
  """

  # Configuration file path
  config_file = os.path.join(appdirs.user_data_dir('circulus', 'appzlab'), 'config.ini')

  # Configuration parser
  config = configparser.ConfigParser()

  def __init__(self):
    """Initializes the configuration handler

    We need check if the configuration file exists, if no,
    we need create it

    """
    if not os.path.exists(appdirs.user_data_dir('circulus', 'appzlab')):
      os.makedirs(appdirs.user_data_dir('circulus', 'appzlab'))

    if not os.path.isfile(self.config_file):
      with open(self.config_file, 'w+') as cfg_file:
        self.config.add_section('circulus')
        self.config.set('circulus', 'sync_path', os.path.expanduser('~/sync'))
        self.config.write(cfg_file)
    else:
      self.config.read(self.config_file)

  def get(self, key, section='circulus'):
    """Return a key from the configuration file"""
    return self.config[section][key]
