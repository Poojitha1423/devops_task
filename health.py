from flask import Flask
from healthcheck import HealthCheck
app = Flask(__name__)
health = HealthCheck()

@app.route("/")
def hello_world():
 return "<p>Hello</p>"

@app.route("/PJ")
def hello():
 return "<p>POOJ </p>"

health.add_check(hello)
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())