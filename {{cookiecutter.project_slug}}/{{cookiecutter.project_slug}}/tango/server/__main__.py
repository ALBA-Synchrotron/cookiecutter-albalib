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
"""Tango server main"""

from . import main

main()
