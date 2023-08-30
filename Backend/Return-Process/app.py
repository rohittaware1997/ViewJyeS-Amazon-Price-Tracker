from flask import Flask

app = Flask(__name__)

@app.route("/<name>/<city>/<country>")
def hello_world(name, city, country):
    return f"Hello, " + name +", It is nice meeting with you, I like to hear that you are from such wonderful country " + country + " and such beautiful city " + city + "(This response is generated and returned from different flask process)"
