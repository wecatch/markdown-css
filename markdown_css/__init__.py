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

from __future__ import (
    absolute_import, division, print_function, with_statement)

import logging
from collections import defaultdict
from cssutils import CSSParser
from cssutils.css import CSSComment


# version is a human-readable version number.

# version_info is a four-tuple for programmatic comparison. The first
# three numbers are the components of the version number.  The fourth
# is zero for an official release, positive for a development branch,
# or negative for a release candidate or beta (after the base version
# number has been incremented)
version = "0.0.6"
version_info = (0, 0, 6, 0)


def to_inline_style(style):
    as_list = []
    for k in style.keys():
        v = style.getPropertyValue(k)
        p = style.getPropertyPriority(k)
        if p:
            as_list.append('%s:%s !%s' % (k, v, p))
        else:
            as_list.append('%s:%s' % (k, v))

    return ';'.join(as_list) + ';'


def parse_style(cssText):
    element_dict = defaultdict(lambda: '')
    # inline style not support pseudo-selector, write into <style> tag
    pseudo_selector_list = []
    parser = CSSParser(loglevel=logging.CRITICAL)
    cssStyle = parser.parseString(cssText)

    # init all selector
    for r in cssStyle:
        if isinstance(r, CSSComment):
            continue

        # skip * selector
        if r.selectorText.find('*') >= 0:
            continue

        # skip pseudo-selector like a:hover
        if r.selectorText.find(':') >= 0:
            continue

        for selector in r.selectorList:
            element_dict[selector.selectorText]

    def append_all_selector(style):
        for k in element_dict.keys():
            element_dict[k] += style

    element_list = []
    for r in cssStyle:
        if isinstance(r, CSSComment):
            continue

        if r.selectorText.find('*') >= 0 and r.selectorText.find(':') < 0:
            append_all_selector(to_inline_style(r.style))
            continue

        if r.selectorText.find(':') >= 0:
            pseudo_selector_list.append(r.cssText)
            continue

        for selector in r.selectorList:
            element_list.append(selector.selectorText)
            element_dict[selector.selectorText] += to_inline_style(r.style)

    return element_list, element_dict, pseudo_selector_list
