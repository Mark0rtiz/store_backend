from flask import Flask
import json
from data import me

app = Flask(__name__)



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




@app.get("/api/test")
def test_api():
    return json.dumps("ok")

@app.get("/api/about")
def about_api():
    return json.dumps(me)

app.run(debug=True)