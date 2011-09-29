#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-javascript-authentication',
    version='1.2',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-annoying',
        'django-component',
        'django-facebook-auth',
        'django-package-installer',
        'facebook-javascript-sdk',
        'javascript-configuration',
    ),
    packages=[
        'facebook_javascript_authentication',
    ],
    package_data={
        'facebook_javascript_authentication': ['static/*/*.*'],
    },
)
