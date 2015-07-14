from flask import Flask, g, request, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)
#db.drop_all()
db.create_all()





@app.route('/')
def index():
	return "Hello World"




if __name__ == '__main__':
	app.run()


