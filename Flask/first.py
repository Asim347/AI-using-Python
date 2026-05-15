from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask, Your ML API is ready!"

if __name__ == "__main__":
     app.run(debug=True, use_reloader = False)