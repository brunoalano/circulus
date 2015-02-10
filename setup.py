from setuptools import setup, find_packages
import circulus
setup(
  # Project
  name = 'circulus',
  version = circulus.__version__,
  url = 'http://github.com/brunoalano/circulus/',
  license = 'Apache Software License',

  # Author
  author = 'Bruno Alano Medina',
  author_email = 'bruno@appzlab.com',

  # Details
  packages = find_packages(),
  install_requires=[],
  description = '',
  platforms = 'any'
)