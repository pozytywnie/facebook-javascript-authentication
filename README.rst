facebook-javascript-authentication
==================================

facebook-javascript-authentication is a Django application that
manages user authentication via Facebook using the JavaScript
Facebook SDK and django-facebook-auth application ( https://github.com/pozytywnie/django-facebook-auth )

Installation
------------

Package
_______

facebook-javascript-authentication can be installed as a normal Python package.

Example instalation for pip::

    $ pip install facebook-javascript-authentication


Configuration
-------------

settings.py
___________

Set USE_TZ = True

Add facebook_javascript_authentication to INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'facebook_javascript_authentication',
        ...
    )

Add javascript authentications urls to application urls::

    urlpatterns = patterns('',
        ...
        url(r'^facebook_javascript_authentication/', include('facebook_javascript_authentication.urls')),
        ...
    )

Add script.js in html template head::

    ...
    <script type="text/javascript" src="{{ STATIC_URL }}facebook_javascript_authentication/script.js"></script>
    ...

Add updating isAuthenticated variable on facebook user status change to FB.init block::

    {% load facebook_javascript_sdk %}
    {% fb_init_block %}
        ...
        updateIsAuthenticatedOnFBStatusChanged();
        ...
    {% endblock %}


Usage
-----

loginDialog
___________

To show user login dialog with email permissions::

    loginDialog(successCallback, 'email')

isAuthenticated variable
________________________

Variable isAuthenticated is set to current user status on each facebook 'auth.statusChange' event.


Custom login source
___________________
If you have a user access token then you can try authenticate him by calling::

    login(access_token, successCallbackFunction)
