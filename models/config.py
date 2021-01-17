import pymysql
import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Az97185Az!",
    db="school",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

print(len('https://www.adamtsair.co.il/%d7%94%d7%97%d7%91%d7%a8-%d7%94%d7%9b%d7%99-%d7%98%d7%95%d7%91-%d7%a9%d7%9c%d7%99-%d7%a4%d7%a8%d7%a7-1/'))