# sheldon woodward
# 4/15/18

"""Setup file."""


from setuptools import setup
from os.path import abspath, dirname, join

from PACKAGE_NAME import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

install_requires = [r.rstrip('\n') for r in open('requirements.txt').readlines()]


setup(name='PACKAGE_NAME',
      version=__version__,
      description='A bare-bones command line program.',
      long_description=long_description,
      packages=['PACKAGE_NAME'],
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'PACKAGE_NAME = PACKAGE_NAME.__main__:main'
          ]
      },
      license='MIT',
      keywords='cli')
