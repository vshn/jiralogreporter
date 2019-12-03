import sys
import click
from . import __version__
from .reporter import print_log


@click.command()
@click.version_option(version=__version__)
def main():
    print_log()