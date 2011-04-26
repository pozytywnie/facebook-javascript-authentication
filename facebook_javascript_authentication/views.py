from annoying.decorators import ajax_request
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

@never_cache
@csrf_exempt
@ajax_request
def authenticate(request, authenticate=auth.authenticate, login=auth.login):
    access_token = request.POST.get('access_token', None)
    if access_token != None:
        user = authenticate(access_token=access_token)
        if user is not None:
            login(request, user)
            return {'status': 'ok'}
    return {'status': 'error'}
