from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, Resource


app = Flask(__name__)
app.debug = True
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///report.db'
db = SQLAlchemy(app)
#db.drop_all()
#db.create_all()


class Report(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	author = db.Column(db.String(100))
	content = db.Column(db.String(900))
	
	def __init__(self, title, author, content):
		self.title = title
		self.author = author
		self.content = content

	@property
	def to_json(self):
		return {
			"id": self.id,
			"title": self.title,
			"author": self.author,
			"content": self.content,
		}



class ReportsResource(Resource):
	def get(self):
		reports = Report.query.all()
		return jsonify({"reports" : [r.to_json for r in reports] })


api.add_resource(ReportsResource, '/api/reports', methods=['GET'])



@app.route('/')
def index():
	return jsonify(root="Public Report Api. Manage your reports.")





if __name__ == '__main__':
	app.run()


