# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


version = "1.3.dev0"
shortdesc = "bda.basen"
longdesc = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
longdesc += open(os.path.join(os.path.dirname(__file__), "CHANGES.rst")).read()

setup(
    name="bda.basen",
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    keywords="",
    author="BlueDynamics Alliance",
    author_email="dev@bluedynamics.com",
    url=u"",
    license="GNU General Public Licence",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["bda"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools"],
    test_suite="bda.basen.tests.test_suite",
)
