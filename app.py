from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Azure App Service! Practical work, cloud PaaS."

@app.route("/about")
def about():
    return "This is a simple Flask app deployed to PaaS."

if __name__ == "__main__":
    app.run()