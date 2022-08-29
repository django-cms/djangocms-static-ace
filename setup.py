#!/usr/bin/env python
from setuptools import find_packages, setup

from djangocms_static_ace import __version__, __ace__version__

REQUIREMENTS = [
    "Django",
]

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Framework :: Django",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]


setup(
    name="djangocms-static-ace",
    version=__version__,
    author="fsbraun",
    author_email="fsbraun@gmx.de",
    url="https://github.com/fsbraun/djangocms-frontend",
    license="MIT license",
    description=f"Adds ace {__ace__version__} to static files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
