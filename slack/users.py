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
import slack.http_client

def getPresence(user):
    """
    Returns information about a user's presence.
    """
    params = {
        'token': slack.api_token,
        'user': user,
    }

    return slack.http_client.get('users.getPresence', params)

def info(user):
    """
    Returns information about a team member.
    """
    params = {
        'token': slack.api_token,
        'user': user,
    }

    return slack.http_client.get('users.info', params)


def list():
    """
    Returns a list of all users in the team.
    """
    params = { 'token': slack.api_token }

    return slack.http_client.get('users.list', params)

def setActive():
    """
    Sets the currently authenticated user as currently active
    """
    params = { 'token': slack.api_token }

    return slack.http_client.get('users.setActive', params)

def setPresence(presence):
    """
    Sets the calling user's presence manually
    """
    if presence not in ['auto', 'away']:
        raise ValueError("Expected 'auto' or 'away'")

    params = {
        'token': slack.api_token,
        'presence': presence,
    }

    return slack.http_client.get('users.setPresence', params)
