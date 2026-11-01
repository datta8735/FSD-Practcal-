from flask import Flask

app = Flask(__name__)

@app.route('/student', methods=['GET'])
def student():
    return "Student Details..! This is a Get Request."

if __name__=='__main__':
    app.run(debug=True)