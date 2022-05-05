from crypt import methods
from flask import Flask,jsonify,request

app = Flask(__name__)

events = []


@app.route("/ev",methods= ['POST'])
def post_events():
    data = request.get_json()
    events.append(data)
    return jsonify(data)

@app.route("events",methods=['GET'])
def get_events():
    return jsonify(events)


if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
#,host="0.0.0.0"





