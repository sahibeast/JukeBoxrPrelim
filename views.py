from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from JukeV1.models import Post, Comment
import requests
import json

posts = Blueprint('posts', __name__, template_folder='templates')

def get_venues(address):

    print "venues function exectuing"

    CLIENT_ID = "PZNJGDBGF4O34SXD0NYLMDWQDB1GA0M0WQK0V4SLO2I2A2I5"
    CLIENT_SECRET = "W1GROIHFC45H5WZSZHN023DACEMMTMLNGBF2JSHWBXBKMVWK"

    client = "&limit=10&client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&v=20130907"

    query = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&sensor=false'
    r = requests.get(query)
    json = r.json()
    
    longitude = json["results"][0]["geometry"]["location"]["lng"]
    lat = json["results"][0]["geometry"]["location"]["lat"]

    print "longitude" + str(longitude)
    print "latitude" + str(lat)

    #print "https://api.foursquare.com/v2/venues/search?ll=" + str(lat) + ',' + str(longitude) + client
    #r = requests.get("https://api.foursquare.com/v2/venues/search?ll=34.154413,-118.067415&limit=10&client_id=PZNJGDBGF4O34SXD0NYLMDWQDB1GA0M0WQK0V4SLO2I2A2I5&client_secret=W1GROIHFC45H5WZSZHN023DACEMMTMLNGBF2JSHWBXBKMVWK&v=20130907")
    r =  requests.get("https://api.foursquare.com/v2/venues/search?ll=" + str(lat) + ',' + str(longitude) + client)

    #print r.text()
    json = r.json()
    response = json["response"]["venues"]

    return response


class ListView(MethodView):

    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts)


class DetailView(MethodView):

    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', post=post)

class BusinessView(MethodView):

    def get(self):
        address = request.args.get('address')
        print address
        #return json.dumps(get_venues(address))
        return render_template('user/venues.html', venues=json.loads(json.dumps(get_venues(address))))
        #return get_venues(address)

class StoreChoice(MethodView):

    def post(self):
        content = request.json['choice']
        return "POST endpoint hit " + content


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
posts.add_url_rule('/venues', view_func=BusinessView.as_view('venues'), methods=['GET',])
posts.add_url_rule('/api/userchoice', view_func=StoreChoice.as_view('choice'), methods=['POST',])