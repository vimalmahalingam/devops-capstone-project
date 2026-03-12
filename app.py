from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, DevOps Capstone Project!"

if __name__ == "__main__":
    # Run a web server that keeps the container alive
    app.run(host="0.0.0.0", port=8080)
