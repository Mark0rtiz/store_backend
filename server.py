from flask import Flask, request, abort
import json
import random
from data import me
from data import me, catalog 
from flask_cors import CORS
from config import db

app = Flask(__name__)
CORS(app) #disable CORS, anyone can access this API


@app.get("/")
def home():
    return "hello from Flask"

@app.get("/test")
def test():
    return "This is another endpoint"




@app.get("/about")
def about():
    return "Hello, Mark"


#################################################

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


@app.get("/api/test")
def test_api():
    return json.dumps("ok")

@app.get("/api/about")
def about_api():
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    #return list of products
    cursor = db.Products.find({}) # read all products
    results = []
    for prod in cursor:
        prod = fix_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    if not "title" in product:
        return abort(400, "ERROR: Title is required")
    if len(product["title"]) < 5:
        return abort(400, "ERROR: Title must be greater than 5 characters")
    if not "price" in product:
        return abort(400, "ERROR: Price is required")
    if product["price"] < 1:
        return abort(400, "ERROR: Price must be $1 or greater")
    
    db.Products.insert_one(product)
    
    product["_id"] = str(product["_id"])

    return json.dumps(product)

@app.get("/api/product/<id>")
def get_product_by_id(id):
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    return json.dumps("Error: id not found")

@app.get("/api/products/<category>")
def get_products_in_category(category):
    results = []
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)
    return json.dumps(results)

@app.get("/api/count")
def count_api():
    count = len(catalog)
    return json.dumps(count)
    
@app.get("/api/catalog/total")
def catalog_total():
    total = 0
    for prod in catalog:
        total += prod["price"]
    return json.dumps(total)

@app.get("/api/catalog/cheapest")
def lowest_price():
    cheapest = catalog[0]
    for prod in catalog:
        if prod["price"] < cheapest["price"]:
            cheapest = prod
    return json.dumps(cheapest) 
        


# app.run(debug=True)



@app. get("/api/game/<pick>")
def game (pick):

    num = random.randint(0, 2)
    pc = ""
    if num == 0:
        pc = "paper"
    elif num == 1:
        pc = "rock"
    else:
        pc = "scissors"

    winner = ""
    if pick == "paper":
        if pc == "rock":
            winner = "you"
        elif pc == "scissors":
            winner = "pc"
        else:
            winner = "draw"

    elif pick == "rock":
        if pc == "rock":
            winner = "draw"
        elif pc == "scissors":
            winner = "you"
        else:
            winner = "pc"

    elif pick == "scissors":
        if pc == "rock":
            winner = "pc"
        elif pc == "scissors":
            winner = "draw"
        else:
            winner = "you"


    results = {
        "you": pick,
        "pc": pc,
        "winner": winner
    }

    return json.dumps(results)