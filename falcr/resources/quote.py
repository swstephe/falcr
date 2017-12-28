from falcr.config import getLogger
from falcr.db import model

log = getLogger(__name__)


class QuoteResource(object):
    def on_get(self, req, resp):
        log.debug("QuoteResource.on_get")
        resp.media = model.get_quote()
