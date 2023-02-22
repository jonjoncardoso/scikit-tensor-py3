#!/usr/bin/env python
"""Python module for multilinear algebra and tensor factorizations"""

from setuptools import setup, find_packages

setup(
    name = 'scikit-tensor-py3',
    version = '0.4.2' ,
    description = """Python module for multilinear algebra and tensor factorizations""",
    maintainer = 'Jonathan Cardoso-Silva',
    maintainer_email = 'jonathan.car.silva@gmail.com',
    url = 'http://github.com/jonjoncardoso/scikit-tensor-py3',
    license = 'GPLv3',
    py_modules=["sktensor"],
    download_url = 'http://github.com/jonjoncardoso/scikit-tensor-py3',
    package_name = 'sktensor',
    packages=find_packages(),
    install_requires=[
        "numpy < 1.20",
        "scipy >= 0.19.1"],
    python_requires=">=3",
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
