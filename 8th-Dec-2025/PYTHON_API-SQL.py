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
---------------------------------------------
---------------------------------------------

from operator import index
from flask import Flask, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)

# ----------------------------------------------------
# LOGGING CONFIG
# ----------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

# ----------------------------------------------------
# DB CONNECTION
# ----------------------------------------------------
def get_db():
    logging.debug("Attempting DB connection...")
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password123!",
            database="company"
        )
        logging.debug("DB connection successful.")
        return db
    except Exception as e:
        logging.error(f"DB connection failed: {e}")
        raise

# ----------------------------------------------------
# GET EMPLOYEES
# ----------------------------------------------------
@app.route("/employees", methods=["GET"])
def get_employees():
    logging.debug("GET /employees called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing SELECT query")
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500

# ----------------------------------------------------
# POST EMPLOYEE
# ----------------------------------------------------
@app.route("/employees", methods=["POST"])
def add_employee():
    logging.debug("POST /employees called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)"
        logging.debug(f"Executing INSERT: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"]))
        db.commit()
        db.close()

        logging.debug("POST completed")
        return "POST EXECUTED"
    except Exception as e:
        logging.error(f"Error in POST: {e}")
        return "POST ERROR", 500

# ----------------------------------------------------
# PUT EMPLOYEE
# ----------------------------------------------------
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    logging.debug(f"PUT /employees/{id} called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "UPDATE employees SET name=%s, role=%s, salary=%s WHERE id=%s"
        logging.debug(f"Executing UPDATE: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"], id))
        db.commit()
        db.close()

        logging.debug("PUT completed")
        return "PUT EXECUTED"
    except Exception as e:
        logging.error(f"Error in PUT: {e}")
        return "PUT ERROR", 500

# ----------------------------------------------------
# DELETE EMPLOYEE
# ----------------------------------------------------
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    logging.debug(f"DELETE /employees/{id} called")
    try:
        db = get_db()
        cursor = db.cursor()

        sql = "DELETE FROM employees WHERE id=%s"
        logging.debug(f"Executing DELETE: {sql}")

        cursor.execute(sql, (id,))
        db.commit()
        db.close()

        logging.debug("DELETE completed")
        return "DELETE EXECUTED"
    except Exception as e:
        logging.error(f"Error in DELETE: {e}")
        return "DELETE ERROR", 500

# ----------------------------------------------------
# RUN
# ----------------------------------------------------
if __name__ == "__main__":
    logging.debug("Starting Flask server...")
    app.run(debug=True)
