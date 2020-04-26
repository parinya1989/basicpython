import pymysql.cursors
# Function connect db and return conection


def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1989',
                                 db='pythontestdb',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# print(getConnection())
