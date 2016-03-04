from django.conf.urls import url
from django.core.urlresolvers import reverse

from facebook_javascript_authentication import views

urlpatterns = [
    url(r'^authenticate$', views.authenticate, name='facebook_javascript_authenticate'),
]

def javascript_settings():
    return {
        'authenticate': reverse('facebook_javascript_authenticate')
    }
