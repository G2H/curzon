import sys
sys.path.insert(0, 'libs')

import webapp2
import json
import cgi
from google.appengine.api import users
from curzon_parser import *

class hello(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

class getData(webapp2.RequestHandler):
	def get(self):
		today = 'http://www.google.com/movies?near=london&date=0&tid&q=curzon'
		data = JSONfromURL(today)
		site = createSite(data)
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers['Content-Type'] = 'application/json'   
		# obj = {
		# 	'success': 'success', 
		# 	'payload': '',
		#  } 
		self.response.write(json.dumps(site))

app = webapp2.WSGIApplication([
    ('/whoami', hello),
    ('/getData', getData),
], debug=True)