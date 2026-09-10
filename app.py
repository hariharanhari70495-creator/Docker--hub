from flask import flask
app = Flask(_namae_)
@app.route("/")
def home():
return"Hello from Dockere!My first container is running."
if_name_=="_main_":
app.run(host="0.0.0.0"'port=5000)
