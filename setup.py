#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-javascript-authentication',
    version='1.0',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-annoying',
        'django-component',
        'django-javascript-configuration',
        'django-package-installer',
        'facebook-javascript-sdk',
    ),
    packages=[
        'facebook_javascript_authentication',
    ],
)
