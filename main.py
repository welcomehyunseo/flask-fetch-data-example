from random import randint
from faker import Faker
from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS

app = Flask("My flask app")
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/chart")
def chart():
    return render_template('chart.html')


@app.route("/get_users", methods=["GET"])
def get_users():
    # logic
    fake = Faker()
    data = []

    for i in range(1, 1000):
        data.append(fake.simple_profile())

    return jsonify({
        "success": True,
        "data": data
    })


@app.route("/get_lazer_data", methods=["GET"])
def get_lazer_data():
    random_int = randint(0, 1000)

    return jsonify({
        "success": True,
        "data": {
            "randomInt": random_int
        }
    })


app.run()
