import mysql.connector
def connect():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="eletrcity_analysis"
    )
    return mydb
