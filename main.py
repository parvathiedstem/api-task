from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        api = {"main": "Hello World"}
        return jsonify(api)


@app.route('/parvathi', methods=['GET'])
def Details():
    if request.method == 'GET':
        biodata = {"name": "Parvathi", "age": 23, "place": "Athalur"}
        return jsonify(biodata)


if __name__ == '__main__':
    app.run(debug=True)
