import pymysql.cursors
from utils import *
connection = utils.connectdb.getConnection()
try:
    cursor = connection.cursor()
    # SQL Read
    sql = "SELECT * FROM employee"
    cursor.execute(sql)

    # Loop
    for row in cursor:
        print(row)

    connection.commit()
    print("Read employee success")
except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ connection
    connection.close()
