from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Success!</h1><p>Your Python app is running on Vercel.</p>"

@app.route('/about')
def about():
    return "This is the about page."

# Vercel will look for the 'app' variable
