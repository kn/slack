# Copyright (c) 2014 Katsuya Noguchi
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import slack
import slack.users
import slack.http_client


def history(channel, **kwargs):
    """
    Returns a portion of messages/events from a specified channel.
    """
    params = {
        'token':    slack.api_token,
        'channel':  channel,
    }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('channels.history', params)

def mark(channel, ts):
    """
    Moves the read cursor in a channel.
    """
    data = {
        'token':    slack.api_token,
        'channel':  channel,
        'ts':       ts,
    }

    return slack.http_client.post('channels.mark', data)

def create(name):
    """
    Creates a new channel.
    """
    params = {
        'token': slack.api_token,
        'name': name,
    }
    return slack.http_client.post('channels.create', params)

def invite(channel, user):
    """
    Invites a user to a channel.
    """
    params = {
        'token': slack.api_token,
        'channel': channel,
        'user': user,
    }
    return slack.http_client.post('channels.invite', params)

def list(**kwargs):
    """
    Returns a list of all channels in the team.
    """
    params = { 'token': slack.api_token }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('channels.list', params)
