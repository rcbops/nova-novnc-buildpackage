import os
import shutil
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dst = 'debian/nova-novnc/var/lib/nova/'
os.system('rm -rf %s' % dst)
shutil.copytree('nova-novnc', '%s/noVNC' % dst)

requirements = ['httplib2']
if sys.version_info < (2,6):
    requirements.append('simplejson')

setup(
    name = "nova-novnc",
    version = "0.2",
    description = "",
    long_description = read('README.md'),
    url = 'http://github.com/sleepsonthefloor/noVNC/',
    license = 'Apache 2.0',
    author = 'Anthony Young',
    author_email = 'sleepsonthefloor@gmail.com',
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,
    tests_require = ["nose", "mock"],
    test_suite = "nose.collector",
)
