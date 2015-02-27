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


def history(channel, **kwargs):
    """
    Returns a portion of messages/events from the
    specified private group.
    """
    params = {
        'token':    slack.api_token,
        'channel':  channel,
    }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('groups.history', params)

def list(**kwargs):
    """
    Returns a list of groups in the team that the caller is in and
    archived groups that the caller was in.
    """
    params = { 'token': slack.api_token }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('groups.list', params)
