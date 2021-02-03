# ALBA python library cookiecutter

Use it to bootstrap an ALBA python software project.

Actually, it is institute agnostic so it can be used for any python library.
It is just an extension of the well known cookiecutter pypackage with options to create
tango server structure, simulator and a base core class with a connection object.

Don't take this as a hard structure to which all your code should abide. Software design
is a creative process. You should feel free to change whatever comes out of the bootstrap
to fit your needs.

## Installation

First, make sure cookiecutter is installed in your python environment:
```console
$ pip install cookiecutter
```

## Usage

To create a new python project do:
```console
$ cookiecutter gh:alba-synchrotron/cookiecutter-albalib
```

The script is interactive and should look something like this:

```console
full_name [ALBA controls team]:
email [controls@cells.es]:
github_username [alba-synchrotron]:
project_name [ALBA Python Boilerplate]: Demo lib
project_slug [test3_lib]: demo
project_short_description [Demo lib with optional tango server and simulator]:
pypi_username [alba-synchrotron]:
use_pypi_deployment_with_travis [n]:
version [0.1.0]:
use_pytest [y]:
add_pyup_badge [y]:
Select command_line_interface:
1 - No command-line interface
2 - Click
3 - Argparse
Choose from 1, 2, 3 [1]:
tango_server [Demo]:
simulator [y]:
Select open_source_license:
1 - GNU General Public License v3
2 - MIT license
3 - BSD license
4 - ISC license
5 - Apache Software License 2.0
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

Notice that we only need to type a few values. for most options we try to have a sane default value.

This will create the directory structure:

```console

$ tree
.
├── CONTRIBUTING.md
├── demo
│   ├── core.py
│   ├── __init__.py
│   ├── simulator.py
│   └── tango
│       ├── __init__.py
│       ├── __main__.py
│       └── server
│           ├── demo.py
│           └── __init__.py
├── docs
│   ├── conf.py
│   ├── ...
│   └── usage.rst
├── HISTORY.md
├── LICENSE
├── Makefile
├── MANIFEST.in
├── README.md
├── requirements_dev.txt
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_demo.py
└── tox.ini
```
