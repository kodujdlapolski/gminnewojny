from flask import Flask
from flask import request
import json


HOST = '10.20.2.9'
PORT = 1080


app = Flask(__name__)

def get_data_for_gmina(gmina):
    return {'A1': 'V1', 'A2': 'V2'}

def get_similar_gmina(gmina):
    return 'Gmina2'


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/miasto')
def miasto():
    gmina = request.args.get('gmina1', 'unknown')
    gmina2 = request.args.get('gmina2', 'unknown')

    print 'Received', gmina, gmina2

    similar = get_similar_gmina(gmina)

    return json.dumps({
        gmina: get_data_for_gmina(gmina),
        similar: get_data_for_gmina(similar)
    })


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
