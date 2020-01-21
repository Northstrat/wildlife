import json
import wikipedia
import flask
from Animals import Mammal
from Animals import Category
from Animals import Animals
from Animals import Bird

from flask_cors import CORS, cross_origin

mammals_path = 'mammals2.json'
birds_path = 'birds.json'
animals = Animals()

with open(mammals_path) as json_file:
    data = json.load(json_file)
    for category in data:
        for animal in data[category]:
            for a in animal:
                animals.addMammal(category,Mammal(animal['name'],animal['status']))

with open(birds_path) as bird_file:
    data = json.load(bird_file)
    for c1 in data:
        for c2 in data[c1]:
            for c3 in data[c1][c2]:
                brds = data[c1][c2][c3]
                for b in brds:
                    animals.addBird(c1,c2,c3,Bird(b['name'],c1,c2,c3))

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/mammals', methods=['GET'])
@cross_origin()
def getMammals():
    return animals.getMammals()
    #return flask.jsonify([c.serialize() for c in categories])

@app.route('/birds', methods=['GET'])
@cross_origin()
def getBirds():
    return animals.getBirds()

app.run()