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

class SlackError(Exception):
    """
    Generic exception raised when Slack API returns an error.
    """
    pass

class InvalidAuthError(SlackError):
    """
    Raised when authentication token is invalid.
    """
    pass

class NotAuthedError(SlackError):
    """
    Raised when authentication token is not given.
    """
    pass

class AccountInactiveError(SlackError):
    """
    Raised when authentication token is for a deleted user.
    """
    pass

class ChannelNotFoundError(SlackError):
    """
    Raised when channel is not found.
    """
    pass

class ChannelArchivedError(SlackError):
    """
    Raised when channel is archived.
    """
    pass

class NotInChannelError(SlackError):
    """
    Raised when caller is not a member of the channel.
    """
    pass

class RateLimitedError(SlackError):
    """
    Raised when application has posted too many messages.
    """
    pass
