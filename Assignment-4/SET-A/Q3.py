from flask import Flask
app = Flask(__name__)

@app.route("/course/<course_name>")
def course(course_name):
    return f"Course Name: {course_name}<br>course information is displayed here."
    
if __name__=="__main__":
    app.run(debug=True)