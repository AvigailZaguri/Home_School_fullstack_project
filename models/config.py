import pymysql
import datetime

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="homeschooldb",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor
# )

connection = pymysql.connect(
    host="localhost",
    user="root",
    # password="",
    password="Az97185Az!",
    db="school",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

print(datetime.timedelta(seconds=32400).seconds/(60*60))



