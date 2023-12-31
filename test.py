from flask import Flask, jsonify, request

from .model.organization import Organization


app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000 }
]

organizations = [
    {"1" : Organization("1", "Bobs Donuts", None)},
    {"2" : Organization("2", "Garcia Lawn Services", None)},
    {"3" : Organization("3", "Little Lucy's Happy Pets", None)}
]


@app.route("/")
def intro():
    return "SidePursuit service APIs live here"


@app.route('/organizations')
def get_organizations():
    return jsonify(organizations)


@app.route('/organizations/<org_id>')
def get_org_by_id(org_id):
    org = organizations[org_id]
    return jsonify(org)


@app.route('/organizations', method=['POST'])
def add_organization():
    organizations.append(request.get_json())


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

