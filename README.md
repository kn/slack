# slack

slack is a Python package that provides interface to Slack listed officialy on [slack.com](https://api.slack.com/community).

[![Build Status](https://travis-ci.org/kn/slack.svg?branch=master)](https://travis-ci.org/kn/slack)

## Installation

Install via [pip](https://pip.pypa.io/en/latest/)
```
$ pip install pyslack
```

Install from source:
```
$ git clone git://github.com/kn/slack.git
$ cd slack
$ python setup.py install
```

## Getting Started

You need to get your Slack token from [api.slack.com](https://api.slack.com/).

```
> import slack
> import slack.chat
> slack.api_token = 'your_token'
> slack.chat.post_message('#eng', 'Hello slackers!', username='mybot')

> import slack.users
> slack.users.list()
```

## Available Methods

All methods in [a preview release of Slack API](https://api.slack.com/) are available.
