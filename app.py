from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<center><h1>Flask Sample Application - Version1</h1></center>"

@app.route("/home")
def home():
  return "<center><h1>This is home page</h1></center>"

@app.route("/products")
def products(): 
  return "<center><h1>This is products page</h1></center>"
app.run(debug=True,host='0.0.0.0',port='5000')

