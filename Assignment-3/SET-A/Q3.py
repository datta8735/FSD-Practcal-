from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Name: Kiran, Roll Number: 40"

if __name__ == '__main__':
    app.run(debug=True)