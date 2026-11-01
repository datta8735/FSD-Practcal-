from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student_marks():

    students = {
        "Gaurav":[85,45,87],
        "Rohit":[45,55,65],
        "Rehan": [56,78,67],
        "Rahul": [78,98,67]
    }


    result = []
    for name, marks in students.items():
        total = sum(marks)
        average = total / len(marks)
        highest = max(marks)
        lowest = min(marks)
        result.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "highest": highest,
            "lowest": lowest
        })
    return render_template("student.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)