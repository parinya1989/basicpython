import pymysql.cursors
from utils import *
connection = utils.connectdb.getConnection()
try:
    cursor = connection.cursor()
    # SQL
    sql = "INSERT INTO employee(emp_no,emp_name,emp_salary) VALUES(%s, %s, %s)"
    # Execute sql and pass 3 parameter
    cursor.execute(sql, ('2', 'Parinya', '30000'))
    connection.commit()
    print("Create new employee success")
except pymysql.Error as e:
    print("Error %s" % e.args[1])
finally:
    # ปิดการ connection
    connection.close()