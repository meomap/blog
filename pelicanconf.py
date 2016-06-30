#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'htl'
SITENAME = 'FML Blog'
SITEURL = 'http://blog.fml.vn'

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'vn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('FML Group', 'http://fml.vn/'),
         ('FAMILUG', 'http://www.familug.org'))

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/pyfml'),
          ('Github', 'https://github.com/fmlvn'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Additional configuration

DEFAULT_DATE = 'fs'

THEME = 'pelican-blueidea'

DISPLAY_AUTHOR_ON_POSTINFO = True

STATIC_PATHS = ['images']
