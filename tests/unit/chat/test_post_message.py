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

from mock import patch
import json
import unittest

import slack
import slack.chat
import slack.http_client


slack.api_token = 'my_token'


class TestChatPostMessage(unittest.TestCase):
    @patch.object(slack.http_client, 'post')
    def test_post_message(self, http_post_mock):
        slack.chat.post_message('#python', 'slackers!')
        http_post_mock.assert_called_with('chat.postMessage', {
            'token': 'my_token',
            'channel': '#python',
            'text': 'slackers!',
        })

    @patch.object(slack.http_client, 'post')
    def test_post_message_with_attachments(self, http_post_mock):
        attachment = {
            'fallback': 'slackers!',
            'text': 'slackers!',
            'fields': [{
                'from': 'me',
                'to': 'you',
            }],
        }
        slack.chat.post_message(
            '#python', 'slackers!', attachments=[attachment])
        http_post_mock.assert_called_with('chat.postMessage', {
            'token': 'my_token',
            'channel': '#python',
            'text': 'slackers!',
            'attachments': json.dumps([attachment]),
        })
