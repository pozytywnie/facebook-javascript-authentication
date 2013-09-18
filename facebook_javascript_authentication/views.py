import datetime
import json

from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

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
            return HttpResponse(json.dumps({'status': 'ok'}))
    return HttpResponse(json.dumps({'status': 'error'}))

def _get_token_expiration_date(request):
    token_expiration_date = None
    if 'token_expires_in' in request.POST:
        expires_in_seconds = int(request.POST['token_expires_in'])
        expires_in = datetime.timedelta(seconds=expires_in_seconds)
        token_expiration_date = datetime.datetime.now() + expires_in
    return token_expiration_date

def _update_token_expiration_date(request, user):
    token_expiration_date = None
    if 'token_expires_in' in request.POST:
        expires_in_seconds = int(request.POST['token_expires_in'])
        expires_in = datetime.timedelta(seconds=expires_in_seconds)
        token_expiration_date = datetime.datetime.now() + expires_in
    facebook_user = user.facebookuser
    facebook_user.access_token_expiration_date = token_expiration_date
    facebook_user.save()
