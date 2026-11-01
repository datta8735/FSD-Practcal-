from flask import Flask
app = Flask(__name__)

@app.route("/employee")
def employee():
    return "Welcome to the Employee Page."

@app.route("/department")
def department():
    return "Welcome to the Department Page."

@app.route("/contact")
def contact():
    return "Welcome to the Contact Page."

if __name__=="__main__":
    app.run(debug=True)