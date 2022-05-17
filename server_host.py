from flask import Flask
from threading import Thread

app = Flask('')
host = '0.0.0.0'
port = 8080

@app.route('/')
def home():
  x = f"I'm alive!<br>Running at host: {host} port: {port}"
  return x

def run():
  app.run(host=host, port=port)

def server():
  t = Thread(target=run)
  t.start()