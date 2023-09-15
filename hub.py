from flask import Flask

app = Flask(__name__)


@app.route("/")
def preamble():
    return "<p>Hello, World!</p>"


@app.route("/organizations")
def get_organizations():
    return ("[{'id' : 1, 'name': 'Bobs Donuts', 'address', '1111 Fountain Valley Way, El Paso, TX 99999'}, {'id' : 2, "
            "'name': 'Sandford Lawn Services', 'address', '88 Somewhere Over the Valley, Midland, TX 55555'}]")


@app.route("/organizations/<org_id>")
def get_organization(org_id):
    return ("{'id' : 2, "
            "'name': 'Sandford Lawn Services', 'address', '88 Somewhere Over the Valley, Midland, TX 55555'}")


@app.route("/organizations/<org_id>/customers")
def get_organization_customers(org_id):
    return ("[{'id' : 1, 'name': 'Sam Smith', 'address', '1405 YoMomma Lane, El Paso, TX 25252'}, {'id' : 2, "
            "'name': 'Bethany Williams', 'address', '77 Crossover Ct, Houston, TX 11111'}]")


@app.route("/organizations/<org_id>/customers/<customer_id>")
def get_organization_customer(org_id, customer_id):
    return "{'id' : 2, 'name': 'Bethany Williams', 'address', '77 Crossover Ct, Houston, TX 11111'}"
