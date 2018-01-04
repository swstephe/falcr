import falcon
from auth.config import getLogger

log = getLogger(__name__)

class QuoteResource(object):
    def on_get(self, req, resp):
        log.info("QuoteResource.on_get")
        resp.media = {'quote': 'Witty quote here'}
