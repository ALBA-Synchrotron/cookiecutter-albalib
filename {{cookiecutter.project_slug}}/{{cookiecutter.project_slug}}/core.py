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
"""
Core {{ klass }} module.

It can receive an asynchronous connection object. Example::

    from connio import connection_for_url
    from {{ cookiecutter.project_slug }}.core import {{ klass }}

    async def main():
        tcp = connection_for_url("tcp://{{obj}}.acme.org:5000")
        {{ obj }} = {{ klass }}(tcp)

        idn = await {{ obj }}.get_idn()
        print(idn)

    asyncio.run(main())
"""


class {{ klass }}:
    """The central {{ klass }}"""

    def __init__(self, conn):
        self._conn = conn

    # The following code is simply an example. Replace with your own code

    def get_idn(self):
        # example returning the coroutine back to who calling function
        return self._conn.write_readline(b"*IDN?\n")

    async def get_pressure(self):
        # example processing the result
        data = await self._conn.write_readline(b"SENS1:PRES?\n")
        return float(data)

    async def get_pressure_setpoint(self):
        # example processing the result
        data = await self._conn.write_readline(b"PRES1:SP?\n")
        return float(data)

    def set_pressure_setpoint(self, value):
        # example returning the coroutine back to the calling function
        return self._conn.write(f"PRES1:SP {value}\n".encode())

    def turn_on(self):
        # example returning the coroutine back to who calling function
        return self._conn.write(b"SENS1:PRES 1\n")
