from flask import Flask, render_template

#  FLASK APP 
app = Flask(__name__)

# render home page
@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug = True)