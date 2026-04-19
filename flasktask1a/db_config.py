import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harsha@28122004",
        database="student_db1"
    )