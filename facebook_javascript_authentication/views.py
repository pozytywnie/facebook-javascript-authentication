import json
import logging

from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.utils.encoding import force_text
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

logger = logging.getLogger(__name__)


class AuthenticateFacebookUser(View):
    def post(self, request, authenticator=auth.authenticate, login=auth.login,
             *args, **kwargs):
        access_token = request.POST.get('access_token', None)
        if access_token is not None:
            user = authenticator(access_token=access_token)
            if user is not None:
                login(request, user)
                data = json.dumps(self._get_response_data(user, request))
                return HttpResponse(data, content_type='application/json')
        return HttpResponse(json.dumps({'status': 'error'}),
                            content_type='application/json')

    @staticmethod
    def _get_response_data(user, request):
        return {
            'status': 'ok',
            'csrf_token': force_text(csrf(request).get('csrf_token', None)),
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username
        }

authenticate = csrf_exempt(never_cache(AuthenticateFacebookUser.as_view()))
