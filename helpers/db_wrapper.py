import pymysql


def get_db_handle(command):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="exam")
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    return

