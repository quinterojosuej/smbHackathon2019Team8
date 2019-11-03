import webapp2
import jinja2
import os
from models import Meme
from models import NightGroup

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
def make_group(in_time, in_contact, in_route, in_number_of_people):
    group = NightGroup(contact = in_contact, time = in_time, number_of_people = in_number_of_people, route = in_route)
    group_key = group.put()
    print("--------------------------------------------------------------------"*2)
    return group_key
    
#*******************************************************************************************        

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())

class MakeGroup(webapp2.RequestHandler):
    def get(self):
        make_group_template = the_jinja_env.get_template('templates/make_group.html')
        self.response.write(make_group_template.render())
        
    def post(self):
        made_group_template = the_jinja_env.get_template('templates/made_group.html')
        in_contact = self.request.get('input_contact')
        in_time = self.request.get('input_time')
        in_route = self.request.get('input_route')
        in_number_of_people = self.request.get('input_number_of_people')
        
        
        key = make_group(in_time, in_contact, in_route, in_number_of_people)
        
        var_dict = {
            "contact": in_contact,
            "time": in_time,
            "route": in_route,
            "num_of_people": in_number_of_people,
            "key": key
        }
        
        self.response.write(made_group_template.render(var_dict))
    
class AllNightWatchers(webapp2.RequestHandler):
    def get(self):
        all_night_watchers = NightGroup.query().fetch()
        
        the_variable_dict = {
            "all_night_watchers": all_night_watchers
        }
        all_night_watchers_template = the_jinja_env.get_template('templates/all_night_watchers.html')
        self.response.write(all_night_watchers_template.render(the_variable_dict))
        

# class NightwatchEdit(webapp2.RequestHandler):
#     def get(self):
        

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/make_group', MakeGroup),
    ('/all_nigh_watchers',AllNightWatchers)
    
], debug=True)


