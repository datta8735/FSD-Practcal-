from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to the College Home Page."

@app.route("/student")
def student():
    return "Welcome Student! This is the Student Page."

@app.route("/faculty")
def faculty():
    return "Welcome Faculty! This is the Faculty Page."

if __name__=="__main__":
    app.run(debug=True)