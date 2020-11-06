{%- set klass = cookiecutter.project_slug.capitalize() -%}
{%- set obj = cookiecutter.project_slug.lower() -%}
{%- set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
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


class {{ klass }}(Device):

    green_mode = GreenMode.Asyncio

    url = device_property(dtype=str)

    async def init_device(self):
        await super().init_device()
        self.connection = connection_for_url(self.url, concurrency="async")
        self.{{ obj }} = {{ cookiecutter.project_slug }}.core.{{ klass }}(self.connection)

    @attribute(dtype=str, label="ID")
    def idn(self):
        return self.{{ obj }}.get_idn()

    @attribute(dtype=float, unit="bar", label="Pressure")
    async def pressure(self):
        # example processing the result
        pressure = await self.{{ obj }}.get_pressure()
        return pressure / 1000

    @attribute(dtype=float, unit="bar", label="Pressure set point")
    async def pressure_setpoint(self):
        # example processing the result
        setpoint = await self.{{ obj }}.get_pressure_setpoint()
        return setpoint / 1000

    @pressure_setpoint.setter
    def pressure_setpoint(self, value):
        # example returning the coroutine back to tango
        return self.{{ obj }}.get_pressure_setpoint(value * 1000)

    @command
    def turn_on(self):
        # example returning the coroutine back to who calling function
        return self.{{ obj }}.turn_on()


if __name__ == "__main__":
    import logging
    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
    logging.basicConfig(level="DEBUG", format=fmt)
    {{ klass }}.run_server()
