# -*- coding: utf-8 -*-

"""Main module."""

import sys
from atenvironment import environment
from slackclient import SlackClient

@environment('SLACK_TOKEN')
def pipe(channel, slack_token):
    sc = SlackClient(slack_token)
    msg = sys.stdin.read()
    sc.api_call("chat.postMessage", text=msg, channel=channel)
