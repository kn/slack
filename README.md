# slack

slack is a Python package that provides interface to [Slack](https://slack.com/).

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
> slack.post_message('#eng', 'Hello slackers!')
```

## Available Methods

All methods in [a preview release of Slack API](https://api.slack.com/) are available.
