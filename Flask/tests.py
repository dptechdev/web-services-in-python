import unittest
from flask import Flask
from flask.ext.testing import TestCase
from app import app, db


@app.route("/template")
def template():
	return render_template("template.html")

class MyTest(TestCase):

	def create_app(self):
		test_app = app
		#test_app = Flask(__name__)
		#test_app.config['TESTING'] = True
		#return test_app
		return test_app		


	def test_that_site_works(self):
		response = self.client.get("/")
		self.assertEquals("Hello World", response.data)	


	def test_that_templates_work(self):
		response = self.client.get("/template")
		self.assertEquals("<html><body><h1>Hello World</h1></body></html>", response.data)
		

if __name__ == '__main__':
	unittest.main()

