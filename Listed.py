#select field3 from ListedCompany;
import csv
import sqlite3

con = sqlite3.connect("helloworld.db")
cursor = con.cursor()
request = cursor.execute('select field3 from ListedCompany;')
print("Write Data into CSV")
#SELECT * FROM Pets;

f = open('C:\\ListedCompany.csv', 'w',encoding="utf-8")

#delete from deleteRowDemo where StudentName='' OR StudentName IS NULL;


for rows in request:

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(rows)

# close the file
f.close()
