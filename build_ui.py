#!/usr/bin/env python
import os
import subprocess

"""
Builds GUI files from Qt format into PyQt5 files
"""


def main():
    own_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(os.path.join(own_path, 'app/gui'))
    for filename in os.listdir('.'):
        basename, _, extension = filename.partition('.')
        if extension == 'ui':
            py_file = '{}.py'.format(basename)
            print('Converting "{}" => "{}"'.format(filename, py_file))
            subprocess.check_call(['pyuic5', '-x', filename, '-o', py_file])


if __name__ == '__main__':
    main()
