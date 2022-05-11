from flask import Flask

app = Flask('myapp')

@app.route('/')
def blahblah():
  return '<p> This works </p> <br/> <br/> <a href="www.pikachu.com"> Pika Pika </a> '

@app.route('/sum/<a>/<b>')
def mysum(a, b):
  return str(int(a) + int(b))

app.run(host="0.0.0.0")
