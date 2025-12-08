from flask import  Flask, request, jsonify

app=Flask(__name__)


employees = [
    {
        "name": "Bishal",
        "domain": "AE",
        "email": "b@gmail.com",
    }
]




@app.route('/employees', methods=['GET'])
def list_employees():
    return jsonify(employees), 200


@app.route('/employees',methods=['POST'])
def post_items():
    data=request.get_json()
    employees.append(data)
    return "POST EXECUTED"

@app.route('/employees/<int:index>',methods=['PUT'])
def update_item(index):
    employees[index] = request.get_json()
    return "PUT EXECUTED"


@app.route('/employees/<int:index>',methods=['DELETE'])
def delete_item(index):
    employees.pop(index)
    return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug=True)
