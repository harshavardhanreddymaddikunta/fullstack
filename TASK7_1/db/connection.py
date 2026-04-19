import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harsha@28122004",   
        database="university_db"
    )

    return conn