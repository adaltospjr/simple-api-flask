from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <strong>Hello World</strong>
    <h1> Adalto</h1>
    """

app.run(debug=True)