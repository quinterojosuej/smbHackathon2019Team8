import webapp2
import jinja2
import os
from models import NightGroup
from models import ReportPost

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
def make_group(in_time, in_contact, in_route, in_number_of_people):
    group = NightGroup(contact = in_contact, time = in_time, number_of_people = in_number_of_people, route = in_route)
    group_key = group.put()
    print("--------------------------------------------------------------------"*2)
    print(group_key)
    return group_key
    
def make_report(in_name, in_street, in_time, in_date, in_description):
    report = ReportPost(name = in_name, street = in_street, time = in_time, date = in_date, description = in_description)
    report_key = report.put()
    print("########################################################################")
    print(report_key)
    return 
    
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
            "all_night_watchers": all_night_watchers,
        }
        all_night_watchers_template = the_jinja_env.get_template('templates/all_night_watchers.html')
        self.response.write(all_night_watchers_template.render(the_variable_dict))
       
       
class MakingReport(webapp2.RequestHandler):
    def get(self):
        making_report_template = the_jinja_env.get_template('templates/making_report.html')
        self.response.write(making_report_template.render())
    
    def post(self):
        made_report_template = the_jinja_env.get_template('templates/display_report.html')
        in_name = self.request.get('name')
        in_street = self.request.get('street')
        in_time = self.request.get('time')
        in_date = self.request.get('date')
        in_description = self.request.get('description')
        
        
        key = make_report(in_name, in_street, in_time, in_date, in_description)
        
        var_dict = {
            "name": in_name,
            "street":in_street,
            "time": in_time,
            "date": in_date,
            "description":in_description,
            "key": key
        }
        
        self.response.write(made_report_template.render(var_dict))

class DisplayAllReports(webapp2.RequestHandler):
    def get(self):
        print("*****************************************************")
        all_reports = ReportPost.query().fetch()
        report = all_reports[0]
        print(report)
        the_id = report.key.id()
        the_instance = ReportPost.get_by_id(the_id)
        print("THIS IS THE INSTANCE")
        print(the_instance)
        
        the_variable_dict = {
            "all_reports": all_reports
        }
        all_reports_template = the_jinja_env.get_template('templates/all_reports.html')
        self.response.write(all_reports_template.render(the_variable_dict))
        
################################################
class NightwatchEdit(webapp2.RequestHandler):
    def get(self):
        get_edit_template = the_jinja_env.get_template("templates/get_edit.html")
        self.response.write(get_edit_template.render())
        
class DoNightEdit(webapp2.RequestHandler):
    def post(self):
        in_key = self.request.get('input-key')
        in_to_change = self.request.get('to_change')
        in_new_text = self.request.get('new_text')
        
        print(in_to_change)
        print("*************************************************")
        
        some_string = "Successfully edited"
        if(in_key.isnumeric()):
            if(NightGroup.get_by_id(int(in_key))):
                if(in_to_change=="contact"):
                    instance = NightGroup.get_by_id(int(in_key))
                    instance.contact = str(in_new_text)
                    instance.put()
                elif(in_to_change=="time"):
                    instance = NightGroup.get_by_id(int(in_key))
                    instance.time = str(in_new_text)
                    instance.put()
                elif(in_to_change=="route"):
                    instance = NightGroup.get_by_id(int(in_key))
                    instance.route = str(in_new_text)
                    instance.put()   
                elif(in_to_change=="num_of_people"):
                    instance = NightGroup.get_by_id(int(in_key))
                    instance.number_of_people = str(in_new_text)
                    instance.put()
            else:
                some_string = "Please try again."
        else:
            some_string = "Please try again."
            
        the_dict = {
            "some_string": some_string
        }
        # instance = NightGroup.get_by_id(int(in_key))
        # print("THIS IS AN INSTANCE")
        # print(instance)
        # print(in_key)
        # instance.in_to_change=in_new_text
        # instance.put()
        # print(instance)
        
        get_editing_template = the_jinja_env.get_template("templates/doing_edit.html")
        self.response.write(get_editing_template.render(the_dict))
        
###########################################
        
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/make_group', MakeGroup),
    ('/all_nigh_watchers',AllNightWatchers),
    ('/making_report',MakingReport),
    ('/show_report',DisplayAllReports),
    
    ('/night_watch_edit',NightwatchEdit),
    ('/night_watch_edited',DoNightEdit)
    
], debug=True)


