from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
import json

from expenses import *

HOST = '10.20.2.9'
PORT = 1080


app = Flask(__name__)


@app.route("/")
def hello():
    print 'DEBUG'
    return redirect(url_for('static', filename='index2.html'))

@app.route('/miasto')
def miasto():
    try:
        gmina = request.args.get('gmina1', 'unknown')
        gmina2 = request.args.get('gmina2', 'unknown')

        print 'Received', type(gmina), gmina, gmina2

        similar = get_similar_gmina(gmina)

        result = json.dumps(
            {
                "success": "true",
                "payload": {
                    gmina: get_data_for_gmina(gmina),
                    similar: get_data_for_gmina(similar)
            }})
        print result
        return result
    except:
        return json.dumps(
            {
                "success": "false",
                "payload": {}
            });



if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
