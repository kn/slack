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


def all(query, **kwargs):
    """
    Searches both messages and files.
    """
    params = {
        'token':        slack.api_token,
        'query':        query,
    }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('search.all', params)

def messages(query, **kwargs):
    """
    Returns messages matching a search query.
    """
    params = {
        'token':        slack.api_token,
        'query':        query,
    }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('search.messages', params)

def files(query, **kwargs):
    """
    Returns files matching a search query.
    """
    params = {
        'token':        slack.api_token,
        'query':        query,
    }

    for key, value in kwargs.items():
        params[key] = value

    return slack.http_client.get('search.files', params)
