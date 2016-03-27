import sys
sys.path.insert(0, 'libs')

import webapp2
import json
import cgi
from google.appengine.api import users
from curzon_parser import *

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

class getData(webapp2.RequestHandler):
	def get(self):
		site = createSite(data)
		self.response.headers['Content-Type'] = 'application/json'   
		obj = {
			'success': 'success', 
			'payload': '',
		 } 
		self.response.write(json.dumps(site))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getData', getData),
], debug=True)