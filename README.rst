clipper
=======
A bare-bones command line program implementing the click package.

Installation
------------
Before installing your CLI, change ``PACKAGE_NAME`` to the name of your package in the following locations:

- ``./README.rst``
- ``./setup.py``
- ``./PACKAGE_NAME/``
- ``./PACKAGE_NAME/__init__.py``

To install your CLI package, run the following command:
::

  $ pip install .

If you want changes to be applied live during development, run the following command:
::

  $ pip install -e .

Adding Commands
---------------
Adding commands to clipper is simple. Command modules are added to the commands folder and then imported to the
__main__.

Create a command
^^^^^^^^^^^^^^^^
Create a command module in ``./PACKAGE_NAME/commands/`` and import click.

Add to the commands package
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add ``from .MODULE_NAME import *`` to ``./PACKAGE_NAME/commands/__init__.py``.

Add command to to __main__
^^^^^^^^^^^^^^^^^^^^^^^^^^
Add ``main.add_command(MODULE_NAME)`` to ``./PACKAGE_NAME/__main__.py``.
