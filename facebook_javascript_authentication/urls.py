from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.core.urlresolvers import reverse

urlpatterns = patterns('facebook_javascript_authentication.views',
    url(r'^authenticate$', 'authenticate'),
)

def javascript_settings():
    return {
        'authenticate': reverse('facebook_javascript_authentication.views.authenticate')
    }
