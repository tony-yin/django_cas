from view import *
urlpatterns = [
    url(r'^accounts/login$', cas_login, name='cas_ng_login'),
]
