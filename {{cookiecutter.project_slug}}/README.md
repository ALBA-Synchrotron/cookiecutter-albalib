{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% set with_tango = cookiecutter.tango_server != "n" -%}
{% set klass = cookiecutter.project_slug.capitalize() -%}

# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![{{ cookiecutter.project_name }}](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
[![{{ cookiecutter.project_name }} updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.simulator == 'y' %}
Apart from the core library, an optional [simulator](https://pypi.org/project/sinstruments) is also provided.
{% endif %}

{% if with_tango %}
Apart from the core library, an optional [tango](https://tango-controls.org/) device server is also provided.
{% endif %}

## Installation

From within your favorite python environment type:

`$ pip install {{ cookiecutter.project_slug }}`

## Library

The core of the {{ cookiecutter.project_slug }} library consists of {{ klass }} object.
To create a {{ klass }} object you need to pass a communication object.

The communication object can be any object that supports a simple API
consisting of two methods (either the sync or async version is supported):

* `write_readline(buff: bytes) -> bytes` *or*

  `async write_readline(buff: bytes) -> bytes`

* `write(buff: bytes) -> None` *or*

  `async write(buff: bytes) -> None`

A library that supports this API is [sockio](https://pypi.org/project/sockio/)
({{ cookiecutter.project_name }} comes pre-installed so you don't have to worry
about installing it).

This library includes both async and sync versions of the TCP object. It also
supports a set of features like re-connection and timeout handling.

Here is how to connect to a {{ klass }} controller:

```python
import asyncio

from sockio.aio import TCP
from {{ cookiecutter.project_slug }} import {{ klass }}


async def main():
    tcp = TCP("192.168.1.123", 5000)  # use host name or IP
    {{ cookiecutter.project_slug }}_dev = {{ klass }}(tcp)

    idn = await {{ cookiecutter.project_slug }}_dev.idn()
    print("Connected to {} ({})".format(idn))


asyncio.run(main())
```

{% if cookiecutter.simulator == 'y' %}
### Simulator

A {{ klass }} simulator is provided.

Before using it, make sure everything is installed with:

`$ pip install {{ cookiecutter.project_slug }}[simulator]`

The [sinstruments](https://pypi.org/project/sinstruments/) engine is used.

To start a simulator you need to write a YAML config file where you define
how many devices you want to simulate and which properties they hold.

The following example exports a hardware device with a minimal configuration
using default values:

```yaml
# config.yml

devices:
- class: {{ klass }}
  package: {{ cookiecutter.project_slug }}.simulator
  transports:
  - type: tcp
    url: :5000
```

To start the simulator type:

```terminal
$ sinstruments-server -c ./config.yml --log-level=DEBUG
2020-05-14 16:02:35,004 INFO  simulator: Bootstraping server
2020-05-14 16:02:35,004 INFO  simulator: no backdoor declared
2020-05-14 16:02:35,004 INFO  simulator: Creating device {{ klass }} ('{{ klass }}')
2020-05-14 16:02:35,080 INFO  simulator.{{ klass }}[('', 5000)]: listening on ('', 5000) (newline='\n') (baudrate=None)
```

(To see the full list of options type `sinstruments-server --help`)

{% endif %}

{% if with_tango %}

### Tango server

A [tango](https://tango-controls.org/) device server is also provided.

Make sure everything is installed with:

`$ pip install {{ cookiecutter.project_slug }}[tango]`

Register a {{ cookiecutter.tango_server }} tango server in the tango database:
```
$ tangoctl server add -s {{ cookiecutter.tango_server }}/test -d {{ klass }} test/{{ klass.lower() }}/1
$ tangoctl device property write -d test/{{ klass.lower() }}/1 -p address -v "tcp://192.168.123:5000"
```

(the above example uses [tangoctl](https://pypi.org/project/tangoctl/). You would need
to install it with `pip install tangoctl` before using it. You are free to use any other
tango tool like [fandango](https://pypi.org/project/fandango/) or Jive)

Launch the server with:

```terminal
$ {{ cookiecutter.tango_server }} test
```
{% endif %}

## Credits

### Development Lead

* {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

### Contributors

None yet. Why not be the first?
