import click


@click.group()
def cli():
    '''Command line interface for the weather-bot package.'''
    pass

from .stations import get_stations_command
cli.add_command(get_stations_command)

from .version import print_version_command
cli.add_command(print_version_command)
