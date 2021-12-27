#!/usr/bin/env python
"""Python module for multilinear algebra and tensor factorizations"""

import os
import sys

DISTNAME = 'scikit-tensor-py3'
VERSION = '0.4.1'
DESCRIPTION = """Python module for multilinear algebra and tensor factorizations"""
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Evert Rol'
MAINTAINER_EMAIL = 'evert.rol@gmail.com'
URL = 'http://github.com/evertrol/scikit-tensor-py3'
LICENSE = 'GPLv3'
DOWNLOAD_URL = URL
PACKAGE_NAME = 'sktensor'
EXTRA_INFO = dict(
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)

try:
    import setuptools  # If you want to enable 'python setup.py develop'
    EXTRA_INFO.update(dict(
        zip_safe=False,   # the package can run out of an .egg file
        include_package_data=True,
    ))
except:
    print('setuptools module not found.')
    print("Install setuptools if you want to enable 'python setup.py develop'.")


def setup_package():
# Call the setup function
    metadata = dict(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        download_url=DOWNLOAD_URL,
        long_description=LONG_DESCRIPTION,
        version=VERSION,
        python_requires=">=3.5",
        install_requires=[
            'numpy>=1.16',
            'scipy>=1.3',
        ],
        **EXTRA_INFO
    )


    from setuptools import setup
    metadata['version'] = VERSION


    setup(**metadata)

if __name__ == "__main__":
    setup_package()
