# Circulus - file synchronization
# Copyright (C) 2015 Bruno Alano Medina <bruno@appzlab.com>
# See LICENSE

"""
circulus file system handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

handle events about file modifications
"""

from watchdog.observers import Observer
import watchdog.events
from circulus.stream import Stream
import time

class SyncHandler(watchdog.events.FileSystemEventHandler):
  """File synchronization event handler with 3rd party services

  This class is responsible for analyzing the events
  observed in the directory, sort of file or directory
  operations and then perform the necessary operations to
  synchronize with third party services.

  """

  # File streamer
  stream = Stream()

  # Catch anything
  def on_any_event(self, event):
    """Catch any event occurred in the filesystem
    
    Attributes:
      event (obj): Watchdog

    """
    time.sleep(2) # 2 seconds
    if event.is_directory:
      self.directoryHandler(event)
    else:
      self.fileHandler(event)

  def fileHandler(self, event):
    """Manage file operations
    
    This method is responsible for the actions related to
    system files, since their analysis and their transfer
    to other application sectors.

    """

    # Python switch-like statement
    if isinstance(event, watchdog.events.FileCreatedEvent):
      # Send file path to Streamer to add to database and
      # send to Stream Service
      self.stream.send_file(event.src_path)
    elif isinstance(event, watchdog.events.FileDeletedEvent):
      # File deleted
      print('Deleted')
    elif isinstance(event, watchdog.events.FileMovedEvent):
      # File moved
      print('Moved')
    elif isinstance(event, watchdog.events.FileModifiedEvent):
      # File modified
      print('Modified')

  def directoryHandler(self, event):
    """Manage directory operations
    
    This method is responsible for the actions related to
    system directories, since their analysis and their transfer
    to other application sectors.

    """

    if isinstance(event, watchdog.events.DirCreatedEvent):
      # Directory created
      print('Created')
    elif isinstance(event, watchdog.events.DirDeletedEvent):
      # Directory deleted
      print('Deleted')
    elif isinstance(event, watchdog.events.DirMovedEvent):
      # Directory moved
      print('Moved')
    elif isinstance(event, watchdog.events.DirModifiedEvent):
      # Directory modified
      print('Modified')


  