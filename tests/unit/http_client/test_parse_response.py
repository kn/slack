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

import json
import mock
import unittest

import slack.http_client
from slack.exception import SlackError


class TestParseResponseClient(unittest.TestCase):
    def _get_mock_response(self, response):
        return mock.Mock(json=lambda: json.loads(response))

    def test_invalid_json(self):
        invalid_response = self._get_mock_response('')
        self.assertRaises(SlackError,
                          slack.http_client._parse_response,
                          invalid_response)

    def test_bad_response(self):
        bad_response = self._get_mock_response(
            json.dumps({'ok': False, 'error': 'unknown_error'}))
        self.assertRaises(SlackError,
                          slack.http_client._parse_response,
                          bad_response)

    def test_ok_response(self):
        # does not raise
        ok_response = self._get_mock_response(json.dumps({'ok': True}))
        slack.http_client._parse_response(ok_response)
