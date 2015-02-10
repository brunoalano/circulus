# Circulus - file synchronization
# Copyright (C) 2015 Bruno Alano Medina <bruno@appzlab.com>
# See LICENSE

"""
circulus file streamer
~~~~~~~~~~~~~~~~~~~~~~~

send the files to external service and store the data
in the local database
"""

from circulus.config import Config
config = Config()
import boto
from boto.s3.key import Key
import math
import os
import sys
from filechunkio import FileChunkIO

def percent_cb(complete, total):
  sys.stdout.write('.')
  sys.stdout.flush()

class Stream:
  """Class responsible to send file to 3rd party services"""

  # Store the connection to Amazon S3
  connection = boto.connect_s3(config.get('access_key', 'aws'), config.get('secret_access_key', 'aws'))

  def __init__(self):
    # Try to create the bucket or connect to some that
    # already exists
    try:
      self.bucket = self.connection.create_bucket(config.get('bucket_name', 'aws'))
    except:
      self.bucket = self.connection.get_bucket(config.get('bucket_name', 'aws'))

  def send_file(self, file):
    # Get file properties
    source_size = os.stat(file).st_size
    source_name = os.path.basename(file)

    # Debug
    print("Upload {} of {} bytes to Amazon S3".format(source_name, source_size))

    # Use a chunk size of 50 MiB
    chunk_size = 52428800
    chunk_count = int(math.ceil(source_size / chunk_size))
    
    if chunk_count <= 1:
      # Do not create a chunked upload
      k = Key(self.bucket)
      k.key = source_name
      k.set_contents_from_filename(file, cb=percent_cb, num_cb=10)
    else:
      # Create a multipart upload request
      mp = self.bucket.initiate_multipart_upload(os.path.basename(file))

      # Send the file parts, using FileChunkIO to create a file-like object
      # that points to a certain byte range within the original file. We
      # set bytes to never exceed the original file size.
      for i in range(chunk_count + 1):
        offset = chunk_size * i
        bytes = min(chunk_size, source_size - offset)
        with FileChunkIO(file, 'r', offset=offset, bytes=bytes) as fp:
          mp.upload_part_from_file(fp, part_num=i + 1)

      # Finish the upload
      mp.complete_upload()