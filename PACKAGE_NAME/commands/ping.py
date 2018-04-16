# sheldon woodward
# 4/15/18

"""The ping command."""


import click


@click.group()
def ping():
    click.echo('pong')
