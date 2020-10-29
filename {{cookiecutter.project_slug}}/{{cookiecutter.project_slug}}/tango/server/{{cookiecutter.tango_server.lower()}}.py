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
"""Tango server class for {{ klass }}"""

import asyncio
import urllib.parse

from connio import connection_for_url
from tango import GreenMode
from tango.server import Device, attribute, command, device_property

import {{ cookiecutter.project_slug }}.core


def create_connection(address, connection_timeout=1, timeout=1, default_port=5000):
    if address.startswith("tcp://"):
        address = address[6:]
        pars = address.split(":")
        host = pars[0]
        port = int(pars[1]) if len(pars) > 1 else default_port
        conn = TCP(host, port,
                   connection_timeout=connection_timeout,
                   timeout=timeout)
        return conn
    else:
        raise NotImplementedError(
            "address {!r} not supported".format(address))


class {{ klass }}(Device):

    green_mode = GreenMode.Asyncio

    url = device_property(dtype=str)

    async def init_device(self):
        await super().init_device()
        self.connection = connection_for_url(self.url, concurrency="async")
        self.{{ klass.lower() }} = {{ cookiecutter.project_slug }}.core.{{ klass }}(self.connection)

    @attribute(dtype=str, description="Identification")
    def idn(self):
        return self.{{ klass.lower() }}.idn()


if __name__ == "__main__":
    import logging
    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
    logging.basicConfig(level="DEBUG", format=fmt)
    {{ klass }}.run_server()
