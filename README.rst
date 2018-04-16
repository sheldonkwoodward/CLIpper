clipper
=======
A bare-bones command line program implementing the click and clint package.

clipper uses both click and clint to get the most out of your CLI. click offers useful features when creating your
command structure while clint offers great user interaction features such as colored text and piping.

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

Creating Commands
-----------------
Commands modules are added to ``./PACKAGE_NAME/commands/``. Here is a sample command that prints 'pong' in red:
::

  import click
  from clint.textui import puts, colored


  @click.command()
  def ping():
    puts(colored.red('pong'))

Making Commands Executable
--------------------------
Making commands executable in clipper is simple. Command modules are added to the commands folder and then imported to
__main__.

Add to the commands package
  Add ``from .MODULE_NAME import *`` to ``./PACKAGE_NAME/commands/__init__.py``.

Add command to to __main__
  Add ``main.add_command(MODULE_NAME)`` to ``./PACKAGE_NAME/__main__.py``.

