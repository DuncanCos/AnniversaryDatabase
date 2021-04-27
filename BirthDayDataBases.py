import sqlite3
import os


def newLine():
    nom = input("name of the personn : ")
    date = input("day of birth (DD/MM/YYYY) : ")
    cursor.execute("""
    INSERT INTO users(name, date) VALUES(?, ?)""", (nom, date))
    #cursor.close()


def showTab():
    cursor.execute("""SELECT id, name, date FROM users""")
    for row in cursor:
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    #cursor.close()

def reset():
    cursor.execute("DROP TABLE users")
    conn.commit()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name VARCHAR(20),
         date VARCHAR(20)
    )
    """)
    conn.commit()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name VARCHAR(20),
     date VARCHAR(20)
)
""")

clear = lambda: os.system('cls')
choice=0
while choice!='4':
    print("what do you want to do ?")
    print("1/ add birthday")
    print("2/ show birthday")
    print("3/ reset database")
    print("4/ save and quit")

    choice = input("choice")

    if(choice=='1'):
        clear()
        newLine()
    elif(choice=='2'):
        clear()
        showTab()
    elif(choice=='3'):
        clear()
        reset()
    else:
        print("put a good number")

conn.commit()
