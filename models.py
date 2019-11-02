from google.appengine.ext import ndb

class Meme(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    img_choice = ndb.StringProperty(required=False)
    
    def get_meme_url(self):
        if self.img_choice == 'old-class':
            url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
        elif self.img_choice == 'college-grad':
            url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
        elif self.img_choice == 'thinking-ape':
            url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
        elif self.img_choice == 'coding':
            url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
        return url

class NightGroup(ndb.Model):
    contact = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    route = ndb.StringProperty(required=True)
    number_of_people = ndb.StringProperty(required=True)
