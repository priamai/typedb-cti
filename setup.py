import os
from setuptools import setup, find_packages
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "typedbcti",
    version = "0.1.0",
    author = "Paolo Di Prodi",
    author_email = "paolo@priam.ai",
    description = ("Package for using CTI with TypeDB "),
    license = "Apache License 2.0",
    keywords = "stix2.1",
    url = "https://github.com/typedb-osi/typedb-cti",
    packages=find_packages(where='.',include=['typedbcti*']),
    #package_dir = {'':'typedbcti'},
    # trying to add files...
    include_package_data = True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
   install_requires=['typedb-client==2.9.0', 'networkx[default]', 'tabulate','pandas'], #external packages as dependencies
   scripts=[
            'typedbcti/scripts/migrate.py',
            'typedbcti/scripts/explorer.py',
            'typedbcti/scripts/downloader.py'
           ]
)