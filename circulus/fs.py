# Circulus - file synchronization
# Copyright (C) 2015 Bruno Alano Medina <bruno@appzlab.com>
# See LICENSE

"""
circulus file system monitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

this module monitor the directory and check for changes
when verify if the file has changed, added or moved
"""

import os
import time
from watchdog.observers import Observer
from circulus.handler import SyncHandler

def monitor(path):
  """monitor changes in a specified path"""

  # Create a new observer
  observer = Observer()

  # Setup the observer destination
  observer.schedule(SyncHandler(), os.path.expanduser(path), recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

  