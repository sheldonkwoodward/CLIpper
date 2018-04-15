# sheldon woodward
# 4/15/18


from setuptools import setup

from clipper import __version__

setup(name='clipper',
      version=__version__,
      packages=['clipper'],
      entry_points={
          'console_scripts': [
              'clipper = clipper.__main__:main'
          ]
      },
      )
