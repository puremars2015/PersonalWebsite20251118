from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)