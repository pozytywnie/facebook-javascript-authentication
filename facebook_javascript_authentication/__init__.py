from component import JavaScriptComponent
from django.conf.urls.defaults import patterns, include
import javascript_configuration
from package_installer import Package


class FacebookJavaScriptAuthenticationPackage(Package):
    INSTALL_APPS = ('facebook_javascript_authentication',)
    REQUIRE = (
        'facebook_auth',
        'facebook_javascript_sdk',
        'javascript_configuration',
    )

    def get_urls(self):
        return patterns('',
            ('^facebook_javascript_authentication/', include('facebook_javascript_authentication.urls'))
        )

class FacebookJavaScriptAuthentication(JavaScriptComponent):
    REQUIRE = (javascript_configuration.JavaScriptConfiguration,)
    JAVASCRIPT_FILES = (
        'facebook_javascript_authentication/script.js',
    )

PACKAGE = FacebookJavaScriptAuthenticationPackage()
