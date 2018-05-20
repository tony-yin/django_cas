from django_cas_ng import views as baseviews
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cas_login(request, **kwargs):
    r = baseviews.login(request, **kwargs)
    if not request.user.is_anonymous():
	token = get_token(request)
        if token:
            r.set_cookie('token', token)
        else:
            print 'Get token error'
    else:
        print('User is anonymous')
    return r

def get_token(request, *args, **kwargs):
    user = request.user
    try:
        request_hash = AuthToken.get_request_hash(request)
        try:
            token = generate_token()    # function used to geneate token, this place won't show more detail codes
            token.refresh()
        except IndexError:
            pass
    except Exception as e:
        print e
        return False
    return token.key
