# dbAddJob.py
# 26 Jul 12, Robert Bills
"""Take user input and write it to a work order database.
"""
import MySQLdb
# open a db connection

db = MySQLdb.connect("localhost","root","","test")

# we'll be using the cursor method for most/all of this

cursor = db.cursor()

# get some information to write to db
myCust = raw_input("What is your name? ")
myBld = raw_input("What building has the problem? ")
myRoom = raw_input("What room? ")
myJobDesc = raw_input("What is a brief problem description? ")

# insert data statement follows
sql = "insert into jobs (Bld,Room,Cust,JobDesc) \
values ('%s','%s','%s','%s')" % (myBld,myRoom,myCust,myJobDesc)

print "Writing request to database..."

try:
    cursor.execute(sql)
    db.commit()
    print "Success"
except:
    db.rollback()
    print "Unable to write changes"

db.close()
