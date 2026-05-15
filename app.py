from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Portfolio is live 🚀"

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    message = request.form.get("message")
    print(name, message)
    return "Message received"

# IMPORTANT: Render entry point
port = int(os.environ.get("PORT", 10000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)