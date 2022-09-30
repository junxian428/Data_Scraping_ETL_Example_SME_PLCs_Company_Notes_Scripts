#select field3 from ListedCompany;
import csv
import sqlite3

con = sqlite3.connect("helloworld.db")
cursor = con.cursor()
#Listed_request = cursor.execute('select field3 from ListedCompany;')
#Batu_request = cursor.execute('select field3 from ListedCompany;')

request = cursor.execute('SELECT Testing5.field3 As batupahat_name, ListedCompany.field3 AS listed_name FROM Testing5 JOIN ListedCompany ON Testing5.field3 LIKE ListedCompany.field3;')
#request = cursor.execute('select field3 from ListedCompany;')
#SELECT
#  product.name AS product_name,
#  category.name AS category_name
#FROM product
#JOIN category ON product.category_id=category.id;
#print("Write Data into CSV")
#SELECT * FROM Pets;

#f = open('C:\\ListedCompany.csv', 'w',encoding="utf-8")

#delete from deleteRowDemo where StudentName='' OR StudentName IS NULL;


for rows in request:

    print(rows)
