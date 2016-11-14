#!/usr/bin/env python
# coding: utf-8
#
# Copyright 2016 Wecatch
#
# Licensed under the MIT License; you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     https://opensource.org/licenses/MIT
#

"""Markdown css tools."""

from __future__ import absolute_import, division, print_function, with_statement
from collections import defaultdict
import cssutils

# version is a human-readable version number.

# version_info is a four-tuple for programmatic comparison. The first
# three numbers are the components of the version number.  The fourth
# is zero for an official release, positive for a development branch,
# or negative for a release candidate or beta (after the base version
# number has been incremented)
version = "0.0.2"
version_info = (0, 0, 2, 0)


def parse_style(css):
    html_attr = defaultdict(lambda:'')
    s = cssutils.parseString(css)

    # map all selector
    for r in s:
        selector = r.selectorText.strip()
        if selector !='*':
            if selector.find(',') >= 0:
                [html_attr[i.strip()] for i in selector.split(',')]
            else:
                html_attr[selector]

    def append_all_selector(style):
        for k in html_attr.keys():
            html_attr[k] += style

    for r in s:
        style = r.style.cssText.replace('\n', '').strip()
        selector = r.selectorText.strip()
        if not style.endswith(';'):
            style += ';'

        # element, element
        selector_list = []
        if selector.find(',') >= 0:
            selector_list = selector.split(',')
        # *
        if selector == '*':
            append_all_selector(style)

        for i in selector_list:
            html_attr[i.strip()] += style

        # element
        if not selector_list:
            html_attr[selector] += style

    return html_attr
