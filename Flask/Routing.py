from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask, Your ML API is ready!"

@app.route("/About")
def about():
     return "This is simple example of routing"

@app.route("/Contact")
def contact():
     return "<h2>Contact Us</h2>"

if __name__ == "__main__":
     app.run(debug=True, use_reloader = False)