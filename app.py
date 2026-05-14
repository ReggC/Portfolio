from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    message = request.form.get("message")

    print("New Message Received")
    print("Name:", name)
    print("Message:", message)

    return f"""
    <h1>Thank You, {name}!</h1>
    <p>Your message has been received.</p>
    <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)