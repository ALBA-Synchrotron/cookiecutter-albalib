#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path), ignore_errors=True)

if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.tango_server }}' == 'n':
        tango_dir = os.path.join('{{ cookiecutter.project_slug }}', 'tango')
        remove_dir(tango_dir)

    if '{{ cookiecutter.simulator }}' != 'y':
        sim_file = os.path.join('{{ cookiecutter.project_slug }}', 'simulator.py')
        remove_file(sim_file)
