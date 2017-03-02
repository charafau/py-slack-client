import os

from slackclient import SlackClient

_token = os.environ['SLACK_API_TOKEN']

slack_client = SlackClient(_token)
