# -*- coding: utf-8 -*-

"""Console script for slack_pipe."""
import sys
import click
import atenvironment
from slack_pipe.pipe import pipe

@click.command()
@click.option('-c', '--channel', required=True, type=str, help='Slack channel to use')
def main(channel):
    try:
        pipe(channel)
        return 0
    except atenvironment.EnvironMiss as m:
        click.echo("Please provide your Slack token as an environment variable")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
