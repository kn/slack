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

import requests
import slack
from slack.exception import SlackError, \
                            InvalidAuthError, \
                            NotAuthedError, \
                            AccountInactiveError, \
                            ChannelNotFoundError, \
                            ChannelArchivedError, \
                            NotInChannelError, \
                            RateLimitedError


def get(method, params):
    url = _build_url(method)
    response = requests.get(url, params=params, verify=True)
    return _parse_response(response)

def post(method, data):
    url = _build_url(method)
    response = requests.post(url, data=data, verify=True)
    return _parse_response(response)

def _parse_response(response):
    try:
        response = response.json()
    except ValueError as e:
        response = {'ok': False, 'error': e}
    _raise_error_if_not_ok(response)
    return response

def _build_url(method):
    return '%s/%s' % (slack.api_base_url, method)

def _raise_error_if_not_ok(response):
    if response['ok']:
        return
    if response['error'] == 'invalid_auth':
        raise InvalidAuthError()
    if response['error'] == 'not_authed':
        raise NotAuthedError()
    if response['error'] == 'account_inactive':
        raise AccountInactiveError()
    if response['error'] == 'channel_not_found':
        raise ChannelNotFoundError()
    if response['error'] == 'is_archived':
        raise ChannelArchivedError()
    if response['error'] == 'not_in_channel':
        raise NotInChannelError()
    if response['error'] == 'rate_limited':
        raise RateLimitedError()
    raise SlackError(response['error'])
