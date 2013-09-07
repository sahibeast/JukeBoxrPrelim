import pymongo
import requests

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "JukeBoxr"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from JukeV1.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

@app.route("/")
def hello():
    return "Hello World!"

"""@app.route("/ll")
def getLL():

	address = request.args.get('address')

	query = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&sensor=false'
	r = requests.get(query)
	json = r.json()

	longitude = json["results"][0]["geometry"]["location"]["lng"]
	lat = json["results"][0]["geometry"]["location"]["lat"]

	return "hi"""

if __name__ == "__main__":
    app.run()