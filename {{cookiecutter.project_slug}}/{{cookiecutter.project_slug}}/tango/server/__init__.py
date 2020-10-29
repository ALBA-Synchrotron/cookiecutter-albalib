{% set klass = cookiecutter.project_slug.capitalize() -%}
{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# -*- coding: utf-8 -*-
#
# This file is part of the {{ cookiecutter.project_name }} project
#
# Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}
{% if is_open_source -%}
# Distributed under the {{ cookiecutter.open_source_license }}. See LICENSE for more info.
{% endif %}
"""Tango server module for {{ cookiecutter.project_name }}."""

from .{{ cookiecutter.tango_server.lower() }} import {{ klass }}


def main():
    import sys
    import logging
    import tango.server
    args = ['{{ cookiecutter.tango_server }}'] + sys.argv[1:]
    fmt = '%(asctime)s %(threadName)s %(levelname)s %(name)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=fmt)
    tango.server.run(({{ klass }},), args=args, green_mode=tango.GreenMode.Asyncio)
