#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jonathan Gray'
SITENAME = 'Jonathan Gray'
SITEURL = 'http://www.j0nn.com'

PATH = 'content'
THEME = 'pelican-themes/pelican-hss'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
USER_LOGO_URL = './qb.jpg'
SITEDESCRIPTION = 'DevOps Engineer who likes Automation, Infosec, and all things Linux / Open Source Tech'
TAGLINE = ' DevOps Engineer who likes Automation, Infosec, and all things Linux / Open Source Tech '
PYGMENTS_STYLE = 'monokai'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget

SOCIAL = (('twitter', 'https://twitter.com/j0nn_gray'),
	  ('github',  'https://github.com/j0nn_gray'),
	  ('linkedin', 'https://www.linkedin.com/in/jonathan-gray-071290ab/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
