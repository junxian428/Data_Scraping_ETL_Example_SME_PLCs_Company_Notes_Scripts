import sqlite3
import csv
import sys
import json

con = sqlite3.connect("helloworld.db")
#cur = con.cursor()
#res = cur.execute("SELECT DISTINCT field3 FROM Testing5;")
#print(res.fetchall())
#In this tutorial, you have learned how to remove duplicate rows from a result set using SQLite SELECT DISTINCT clause.

#data = cur.execute("SELECT DISTINCT field1,field3,field10,field16,field17 FROM Testing5")
f = open('C:\\SQLITEPYTHON.csv', 'w',encoding="utf-8")

cursor = con.cursor()
#cursor.execute("SELECT DISTINCT field1,field3,field10,field16,field17 FROM Testing5;")
#request = cursor.execute('SELECT DISTINCT field1,field3,field10,field16,field17 FROM Testing5;')
#req1 = cursor.execute('DELETE FROM Testing5 WHERE EXISTS (SELECT 1 FROM Testing5 p2 WHERE Testing5.field3 = p2.field3 AND Testing5.field1 > p2.field3);')


#DELETE FROM Testing5 WHERE rowid NOT IN (SELECT min(rowid) FROM Testing5 GROUP BY field3);

#delete from Testing5 where (field10='' OR field10 IS NULL) AND (field16='' OR field16 IS NULL) AND (field17='' OR field17 IS NULL)  ;
#delete from Testing5 where (field10='' OR field10 IS NULL) AND (field16='' OR field16 IS NULL OR field16 == '·') AND (field17='' OR field17 IS NULL OR field17 == '·')  ;

request = cursor.execute('SELECT DISTINCT field1,field3,field10,field16,field17 FROM Testing5;')


#DELETE FROM Pets
#WHERE EXISTS (
 # SELECT 1 FROM Pets p2 
 # WHERE Pets.PetName = p2.PetName
 # AND Pets.PetType = p2.PetType
 # AND Pets.rowid > p2.rowid
#);
print("Write Data into CSV")
#SELECT * FROM Pets;


#delete from deleteRowDemo where StudentName='' OR StudentName IS NULL;


for rows in request:

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(rows)

# close the file
f.close()
