import random
from google.appengine.ext import ndb
from falcr.config import getLogger

log = getLogger(__name__)


class Quotes(ndb.Model):
    author = ndb.StringProperty()
    quote = ndb.StringProperty()

    @classmethod
    def random_quote(cls):
        key = random.sample(cls.query().fetch(keys_only=True), 1)
        if key:
            return key[0].get().to_dict()


class AppUsers(ndb.Model):
    email = ndb.StringProperty()
    password = ndb.StringProperty()

    @classmethod
    def check_user(cls, email, password):
        user = cls.query(cls.email==email).get()
        if user and user.password == password:
            return user.to_dict()
