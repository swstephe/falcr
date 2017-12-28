from google.appengine.ext import ndb
import falcon


class Entries(ndb.Model):
    title = ndb.StringProperty()
    text = ndb.StringProperty()


class EntriesResource:
    def on_get(self, req, resp):
        resp.media = dict(
            entries=[
                dict(
                    id=str(entry.key.id()),
                    title=entry.title,
                    text=entry.text
                )
                for entry in Entries.query().fetch()
            ]
        )

    def on_post(self, req, resp):
        print '---on_post called---'
        try:
            print req.media
            entry = Entries(title=req.media.get('title'), text=req.media.get('text'))
            print 'entry', entry
            entry.put()
            resp.media = dict(
                id=entry.key.id()
            )
        except Exception as e:
            print "exception:", repr(e)


api = application = falcon.API()
api.add_route('/entries', EntriesResource())
