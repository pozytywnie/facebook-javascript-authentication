#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-javascript-authentication',
    version='1.3.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-annoying',
        'django-facebook-auth',
        'facebook-javascript-sdk',
        'django-javascript-settings',
    ),
    packages=[
        'facebook_javascript_authentication',
    ],
    package_data={
        'facebook_javascript_authentication': ['static/*/*.*'],
    },
)
