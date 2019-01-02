'''
Evan Harry

Prints app version.
'''
import click

from weather import __version__


def print_version():
    print('weather-bot version-%s' % __version__)


@click.command('version')
def print_version_command():
    '''Prints app version.'''
    print_version()
