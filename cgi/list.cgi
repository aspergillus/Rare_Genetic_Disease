#!C:/Users/aman/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\r\n\r\n");

import cgi, json
import os
import mysql.connector

parameter = cgi.FieldStorage()
query = parameter.getvalue("sel_query")

result = list()
if "disease" in query:
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='rare_disease')
    cursor = conn.cursor()
    cursor.execute("SELECT Disease FROM `disease_data`") # Get the list of all disease
    query = cursor.fetchall()
    conn.close()
    for i in query:
        result.append(i)
elif "gene" in query:
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='rare_disease')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Gene FROM `annotation_data` ") # Get the list of all genes
    query = cursor.fetchall()
    conn.close()
    for i in query:
        result.append(i)
else:
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='rare_disease')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Variant FROM `variant_data` WHERE Variant IS NOT NULL") # Get the list of all variant
    query = cursor.fetchall()
    conn.close()
    for i in query:
        result.append(i)
print(json.dumps(result))
