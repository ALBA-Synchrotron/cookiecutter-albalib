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
"""
.. code-block:: yaml

    devices:
    - class: {{ klass }}
      package: {{ cookiecutter.project_slug }}.simulator
      transports:
      - type: tcp
        url: :5000

A simple *nc* client can be used to connect to the instrument:

    $ nc 0 5000
    *IDN?
    GE,Pace5000,204683,1.01A
"""

from sinstruments.simulator import BaseDevice


class {{ klass }}(BaseDevice):

    def handle_message(self, line):
        pass
