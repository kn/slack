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

import unittest

import slack.http_client
from slack.exception import SlackError, \
                            InvalidAuthError, \
                            NotAuthedError, \
                            AccountInactiveError, \
                            ChannelNotFoundError, \
                            ChannelArchivedError, \
                            NotInChannelError, \
                            RateLimitedError


class TestRaiseErrorClient(unittest.TestCase):
    def test_ok_response(self):
        # does not raise error if response is ok
        slack.http_client._raise_error_if_not_ok({ 'ok': True })

    def test_invalid_auth(self):
        self.assertRaises(InvalidAuthError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'invalid_auth' })

    def test_not_authed(self):
        self.assertRaises(NotAuthedError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'not_authed' })

    def test_account_inactive(self):
        self.assertRaises(AccountInactiveError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'account_inactive' })

    def test_channel_not_found(self):
        self.assertRaises(ChannelNotFoundError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'channel_not_found' })

    def test_is_archived(self):
        self.assertRaises(ChannelArchivedError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'is_archived' })

    def test_not_in_channel(self):
        self.assertRaises(NotInChannelError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'not_in_channel' })

    def test_rate_limited(self):
        self.assertRaises(RateLimitedError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'rate_limited' })

    def test_slack_error(self):
        self.assertRaises(SlackError,
                          slack.http_client._raise_error_if_not_ok,
                          { 'ok': False, 'error': 'unknown_error' })
