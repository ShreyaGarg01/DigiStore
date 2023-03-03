from flask import Flask, render_template
from pymongo import MongoClient

#  FLASK APP 
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db

# render home page
@ app.route('/')
def home():
    title = 'Home'
    return render_template('dash.html', title=title)

if __name__ == '__main__':
    app.run(debug = True)