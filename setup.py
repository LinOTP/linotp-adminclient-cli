#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#    LinOTP - the open source solution for two factor authentication
#    Copyright (C) 2010 - 2019 KeyIdentity GmbH
#
#    This file is part of LinOTP admin clients.
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public
#    License, version 3, as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the
#               GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#    E-mail: linotp@keyidentity.com
#    Contact: www.linotp.org
#    Support: www.keyidentity.com
#


from setuptools import setup, find_packages

import os
import sys

from linotpadminclientcli import __version__

# Taken from kennethreitz/requests/setup.py
package_directory = os.path.realpath(os.path.dirname(__file__))

yubico_requirements = [
    'pyusb',
    'yubico',
]


def get_file_contents(file_path):
    """Get the context of the file using full path name."""
    content = ""
    try:
        full_path = os.path.join(package_directory, file_path)
        content = open(full_path, 'r').read()
    except:
        print("### could not open file %r" % file_path, file=sys.stderr)
    return content

setup(
    name='LinOTPAdminClientCLI',
    version=__version__,
    description='LinOTP command-line client',
    author='KeyIdentity GmbH',
    author_email='linotp@keyidentity.com',
    url='https://www.linotp.org',
    packages=['linotpadminclientcli'],
    extras_require={
        'yubico': yubico_requirements,
    },
    data_files=[('share/man/man1', ["man/man1/linotpadm.1"])],
#    data_files=[('/usr/lib/python2.6/site-packages/',['linotp2-client.pth']),
#       ],
    license='AGPLv3, (C) KeyIdentity GmbH',
    long_description=get_file_contents('README.md'),
    entry_points={
        'console_scripts': [
            'linotpadm = linotpadminclientcli.cli:main',
        ],
    },
)
