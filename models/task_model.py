
from models.config import connection
from datetime import date, timedelta



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




def get_student_tasks_by_name(name):
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    with connection.cursor() as cursor:
        query = "select id, homework, date(date_) as date_  from task join student_task "\
            "on student_task.task_id = task.id " \
            "where student_task.name_ = '{}' " \
            "and task.date_ <= curdate() and student_task.is_done = 0 " \
            "order by date_ desc ".format(name)
        cursor.execute(query)
        tasks = cursor.fetchall()
        for task in tasks:
            if task['date_'] == today:
                task['date_'] = 'today'
            elif task['date_'] == yesterday:
                task['date_'] = 'yesterday'
        return tasks


# change name to get from cookie
def update_student_task_is_done(task_id, is_done):
    with connection.cursor() as cursor:
        query = "update student_task " \
                "set student_task.is_done = {} " \
                "where student_task.task_id = {} and student_task.name_ = 'Shira Levi' ".format(is_done, task_id)
        cursor.execute(query)
        connection.commit()

