from flask import Flask, render_template, url_for
from data import motorcycles

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/motorcycles/')
def motos():
  return render_template('motorcycles.html', motorcycles=motorcycles)

if __name__ == "__main__":
  app.run(debug=True)