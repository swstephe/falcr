from peewee import *
from playhouse.db_url import connect
from falcr.config import getLogger, DATABASE

log = getLogger(__name__)
database = connect(DATABASE)


class BaseModel(Model):
    @property
    def as_dict(self):
        return dict(
            (unicode(f), getattr(self, f))
            for f in self._meta.fields
            if f not in ('password',)
        )

    class Meta:
        database = database


class Quotes(BaseModel):
    author = CharField(100)
    quote = TextField()


class AppUsers(BaseModel):
    email = CharField(256)
    password = CharField(100)


def get_quote():
    for quote in Quotes.select().order_by(fn.Rand()).limit(1):
        return quote.as_dict


def check_user(email, password):
    for user in AppUsers.select().where(AppUsers.email == email):
        if user.password == password:
            return user.as_dict
