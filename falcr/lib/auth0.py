import urllib
import requests

AUTH0_DOMAIN = 'ariftek.auth0.com'
CLIENT_ID = '4N7SUHL1cO8KqRPe84T1OyKarQTH47pp'


def make_url(verb, **kwargs):
    return 'https://{}/{}?'.format(AUTH0_DOMAIN, verb) + urllib.urlencode(kwargs)


def authorize():
    return make_url(
        'authorize',
        response_type='code',
        client_id=CLIENT_ID,
        connection='CONNECTION',
        redirect_uri='',
        state='STATE'
        )


print authorize()