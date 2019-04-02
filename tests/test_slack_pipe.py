#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `slack_pipe` package."""


import unittest
from click.testing import CliRunner

from slack_pipe import slack_pipe
from slack_pipe import cli


class TestSlack_pipe(unittest.TestCase):
    """Tests for `slack_pipe` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'slack_pipe.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
