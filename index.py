from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Python is running on Vercel!"

# Vercel needs the 'app' variable to be available
