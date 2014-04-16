import datetime
import json
import logging

from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.utils.encoding import force_text
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

FALLBACK_EXPIRES_IN_SECONDS = 900

@never_cache
@csrf_exempt
def authenticate(request, authenticate=auth.authenticate, login=auth.login):
    access_token = request.POST.get('access_token', None)
    token_expiration_date = _get_token_expiration_date(request)
    if access_token != None:
        user = authenticate(access_token=access_token,
                            token_expiration_date=token_expiration_date)
        if user is not None:
            login(request, user)
            data = json.dumps({'status': 'ok',
                               'csrf_token': force_text(csrf(request).get('csrf_token', None)),
                               'user_id': user.id,
                               'first_name': user.first_name,
                               'last_name': user.last_name,
                               'email': user.email,
                               'username': user.username})
            return HttpResponse(data, content_type='application/json')
    return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json')


def _get_token_expiration_date(request):
    token_expiration_date = None
    if 'token_expires_in' in request.POST:
        token_expires_in = request.POST['token_expires_in']
        try:
            expires_in_seconds = int(token_expires_in)
        except ValueError:
            logger.warning('Invalid token_expires_in',
                           extra={'token_expires_in': token_expires_in,
                                  'request': request})
            expires_in_seconds = FALLBACK_EXPIRES_IN_SECONDS
        expires_in = datetime.timedelta(seconds=expires_in_seconds)
        token_expiration_date = timezone.now() + expires_in
    return token_expiration_date
