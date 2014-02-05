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
techFN = raw_input("Technician's First Name: ")
techLN = raw_input("Technician's Last Name: ")
techSpec = raw_input("Technician's Specialty: ")


# insert data statement follows
sql = "insert into techs (FName,LName,Specialty) \
values ('%s','%s','%s')" % (techFN,techLN,techSpec)

print "Updating technician records..."

try:
    cursor.execute(sql)
    db.commit()
    print "Success"
except:
    db.rollback()
    print "Unable to write changes"

db.close()
