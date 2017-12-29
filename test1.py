# -*- coding: utf8 -*-
from google.appengine.ext import ndb


# class DictMixin(ndb.Model):
#     def as_dict(self):
#         return {'foo': 'bar'}


class Entries(ndb.Model):
    title = ndb.StringProperty()
    text = ndb.StringProperty()


entry = Entries(title='title', text='text')
print dir(entry)
print entry.to_dict()
