from google.appengine.ext import ndb


class NightGroup(ndb.Model):
    contact = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    route = ndb.StringProperty(required=True)
    number_of_people = ndb.StringProperty(required=True)

class ReportPost(ndb.Model):
    name = ndb.StringProperty(required=True)
    street = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)