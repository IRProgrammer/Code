import MySQLdb

# open a db connection

db = MySQLdb.connect("localhost","root","","test")

# we'll be using the cursor method for most of this

cursor = db.cursor()

cursor.execute("drop table if exists TECHS")

sql = """CREATE TABLE TECHS (
        TechID INT,
        FName CHAR(20) NOT NULL,
        LName CHAR(20),
        Specialty CHAR(30))"""

cursor.execute(sql)

db.close()
