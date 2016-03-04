#!/usr/bin/env python
from setuptools import setup

setup(
    name='facebook-javascript-authentication',
    version='3.2.0',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django>=1.8',
        'django-facebook-auth>=2.7.4',
        'django-javascript-settings',
    ),
    packages=[
        'facebook_javascript_authentication',
    ],
    package_data={
        'facebook_javascript_authentication': ['static/*/*.*'],
    },
)
