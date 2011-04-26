#!/usr/bin/env python
from distutils.core import setup

setup(
    name='FacebookJavaScriptAuthentication',
    version='0.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-annoying',
        'django-component',
        'django-package-installer',
        'facebook-javascript-sdk',
    ),
    packages=[
        'facebook_javascript_authentication',
    ],
)
