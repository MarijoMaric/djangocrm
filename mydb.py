import  mysql.connector


dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'lozinka123'
)
#prepare a cursos object
cursorObject = dataBase.cursor()
#Create a database
cursorObject.execute("CREATE DATABASE elderco")
