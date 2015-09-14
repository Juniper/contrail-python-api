from setuptools import setup, find_packages

setup(name='pycontrail',
      version='2.20.b64',
      author='Hampapur Ajay',
      author_email='hajay@juniper.net',
      url='http://www.opencontrail.org',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],)
