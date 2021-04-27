import datetime
import sqlite3
import time
from plyer import notification


month=str(datetime.datetime.now().month)
day=str(datetime.datetime.now().day)

if len(month)==1:
    month="0"+month

if len(day)==1:
    day="0"+day
texte = ""

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""SELECT id, name, date FROM users""")
for row in cursor:
    txt=row[2].split('/')
    if str(txt[0])==day and str(txt[1])==month:
        texte=row[1]

remess=""
if texte=="":
    remess="no"
else:
    remess ="aniv "+ texte


notification.notify(
            #title of the notification,
    title = "birtday for the date of {day}/{month}/{year}".format(day =datetime.datetime.today().day,
        month =datetime.datetime.today().month,
        year =datetime.datetime.today().year),
    message = "{ress}".format(ress=remess),
    timeout  = 50

)
