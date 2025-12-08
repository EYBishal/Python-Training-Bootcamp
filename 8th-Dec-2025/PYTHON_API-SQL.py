from operator import index
import pymysql
import pandas as pd
from flask import  Flask, request, jsonify

app=Flask(__name__)

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)


@app.route('/employee', methods=['GET'])
def list_employees():
    df = pd.read_sql("select * from employee", conn)
    data=df.to_dict(orient='records')
    return jsonify(data)



@app.route('/employee', methods=['POST'])
def post_employee():
    data = request.get_json()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO employee (id, name, salary, email) VALUES (%s, %s, %s, %s)",
        (data.get('id'), data.get('name'), data.get('salary'), data.get('email'))
    )
    conn.commit()
    return "POST EXECUTED"


@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute(
        "UPDATE employee SET name = %s, salary = %s, email = %s WHERE id = %s",
        (data.get("name"), data.get("salary"), data.get("email"), id)
    )
    conn.commit()
    return "PUT EXECUTED"





@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_item(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE id = %s", (id,))
    conn.commit()
    return "DELETE EXECUTED"


if __name__ == "__main__":
    app.run(debug=True)
