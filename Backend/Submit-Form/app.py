from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        name = request.form.get('Name')
        city = request.form.get('City')
        country = request.form.get('Country')
        url = "http://52.53.124.215:5000/"
        hostUrl = url + name+ "/" +city+"/"+country
        print(hostUrl)
        res = requests.get(hostUrl)
        print(res.text)
        return res.text
