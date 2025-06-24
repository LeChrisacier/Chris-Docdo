
from flask import Flask, render_template, request, jsonify
from scraper import get_world_data, get_country_data
import json

app = Flask(__name__)

# Charger la liste pays/continent
with open("countries.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", countries=countries)

@app.route("/data/<country>")
def data_by_country(country):
    data = get_country_data(country)
    return jsonify(data)

@app.route("/data/world")
def data_world():
    return jsonify(get_world_data())

if __name__ == "__main__":
    app.run(debug=True)
