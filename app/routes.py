from app import app
from flask import make_response, jsonify, abort, request, render_template, redirect
from flask_api import status
import yaml
from yaml import load, dump, Loader
import json

path = 'app/db/test.yaml'
db = None
stream = None

def Load():
    global db,stream
    stream = open(path, 'r')
    db=yaml.load(stream, Loader=yaml.FullLoader)
    stream.close()

def Save():
    global db,stream
    stream = open(path, 'w')
    stream.write(yaml.dump(db,default_flow_style=False))
    stream.close()

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 404)

@app.route('/')
@app.route('/index')
def index():
    return make_response(render_template('index.html', title='Home'),200)

@app.route('/recipe/<string:recipe>', methods=['PUT'])
def put_recipe(recipe):
    global db
    if not request.json:
        abort(400)
    else:
        Load()
        #yaml.dump(request.json,default_flow_style=False)
        tmp = dict(**{'recipes': {recipe: request.json}})
        tmps = db

        for i in tmp['recipes']:
            tmps['recipes'].update({i:tmp['recipes'][i]})

        db = tmps
        Save()
        return make_response(jsonify({'putted': recipe}), 201)

@app.route('/recipe/<string:recipe>', methods=['DELETE'])
def delete_recipe(recipe):
    try:
        Load()
        del db ['recipes'][recipe]
        Save()
        return status.HTTP_204_NO_CONTENT
    except KeyError:
        abort(400)
    

@app.route('/recipe/<string:recipe>/get/input-amount', methods=['GET','POST'])
def get_input_amount(recipe):
    try:
        Load()
        return jsonify({'amount': db['recipes'][recipe]['input']['amount']}),200
    except KeyError:
        abort(400)

@app.route('/recipe/<string:recipe>/get/input-amount', methods=['GET','POST'])
def get_output_amount(recipe):
    try:
        Load()
        return jsonify({'amount': db['recipes'][recipe]['output']['amount']}),200
    except KeyError:
        abort(400)

@app.route('/recipe/<string:recipe>/get/shape', methods=['GET','POST'])
def get_shape(recipe):
    try:
        Load()
        return jsonify({'amount': db['recipes'][recipe]['output']['amount']}),200
    except KeyError:
        abort(400)