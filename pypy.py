import sqlite3



def newLine():
    nom = input("nom de la personne ?")
    date = input("date de naissance?")
    cursor.execute("""
    INSERT INTO users(name, date) VALUES(?, ?)""", (nom, date))


def showTab():
    cursor.execute("""SELECT id, name, date FROM users""")
    for row in cursor:
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))


conn = sqlite3.connect('C:/Users/foxlo/OneDrive/Documents/code/date.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name VARCHAR(20),
     date VARCHAR(20)
)
""")
conn.commit()

choice=0
while choice!='3':
    print("what do you want to do ?")
    print("1/ add anniv")
    print("2/ show anniv")
    print("3/ quit")

    choice = input("choice")

    if(choice=='1'):
        newLine()
    elif(choice=='2'):
        showTab()
    else:
        print("put a good number")





print("salut")
