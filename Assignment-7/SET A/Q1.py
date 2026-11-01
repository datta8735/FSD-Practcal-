from flask import Flask ,request, jsonify

app = Flask(__name__)

students =[ ]

@app.route('/student',methods=['GET'])
def get_student():
    return jsonify(students)
  
@app.route('/addstudent', methods=['POST'])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify(
        {
            "msg":"Student added sucessfully",
            "student":data
        }
    )

if __name__ == '__main__':
    app.run(debug = True)