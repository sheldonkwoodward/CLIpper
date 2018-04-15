# sheldon woodward
# 4/15/18

"""Setup file."""


from setuptools import setup

from PACKAGE_NAME import __version__


setup(name='PACKAGE_NAME',
      version=__version__,
      packages=['PACKAGE_NAME'],
      entry_points={
          'console_scripts': [
              'PACKAGE_NAME = PACKAGE_NAME.__main__:main'
          ]
      },
      )
