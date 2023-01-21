from flask import Flask
import flask
from random import randint
from play import server_play 
from play import stateless_server_play

app = Flask(__name__)
function = server_play 

@app.route("/move/<number>")
def play_move(number):
    global function 
    result, function = function(50, int(number))
    print(result)
    response = flask.jsonify({'x': result//9, "y": result%9}) 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/moves/<move_list>")
def stateless_play_move(move_list):
    moves = list(map(int, move_list.split(",")))
    result = stateless_server_play(50, moves)
    print(result)
    response = flask.jsonify({'x': result//9, "y": result%9}) 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/refresh")
def refresh():
    global function
    function = server_play
    response = flask.jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
