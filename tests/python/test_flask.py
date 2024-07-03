from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<h1>Hello, World!</h1>"

@app.route('/api/generate-borders', methods=['POST'])
def generate_borders():
    return jsonify({'message': 'Object borders generated successfully', 'object_borders': [10,20,30]})