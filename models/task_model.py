

# import pymysql
#
# connection = pymysql.connect(
#    host="localhost",
#    user="root",
#    password="Az97185Az!",
#    db="school",
#    charset="utf8",
#    cursorclass=pymysql.cursors.DictCursor
# )
#
# if connection.open:
#     print("the connection is opened")
#


def find_student_by_name(name):
    with connection.cursor() as cursor:
        query = "select * from student where name_ = '{}'".format(name)
        cursor.execute(query)
        student = cursor.fetchone()
        return student


def get_tasks_by_class_and_date(class_, date):
    with connection.cursor() as cursor:
        query = "select homework from lesson where class = '{}' and date = {}".format(class_, date)
        cursor.execute(query)
        tasks = cursor.fetchall()
        return tasks

