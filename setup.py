import re
from os import path
from setuptools import setup

__here__ = path.abspath(path.dirname(__file__))

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

# get the dependencies and installs
with open(path.join(__here__, 'requirements.txt'), encoding='utf-8') as f: all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if 'git+' not in x] # set the install requirements
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')] # set the dependency link urls

setup(
    name = "ConnectIt",
    version = "1.0.0",
    author = "Ridley Nelson",
    author_email = "ridley.nelson17@gmail.com",
    description = ("Add_description_here"),
    license = "",
    keywords = ["ridley-nelson17"],
    url = "https://github.com/ridley-nelson17/ConnectIt",
    packages=['root'],
    package_data={'root': ['dist/*', 'libs/*', 'test/*', 'bin/*']},
    package_dir={'': path.dirname(path.abspath(__file__))},
    long_description="",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
