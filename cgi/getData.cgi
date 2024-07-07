#!C:/Users/aman/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\r\n\r\n");

import cgi, json
import mysql.connector

parameter = cgi.FieldStorage()
query = parameter.getvalue("sel_Query")
queryTerm = parameter.getvalue("queryTerm")

conn = mysql.connector.connect(user='root', password='',  host='localhost', database='rare_disease')
cursor = conn.cursor()
def disdata(dis):
    sql_query = "SELECT * FROM disease_data WHERE Disease = '%s'" % (dis)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

def variantDisData(dis):
    sql_query = "SELECT * FROM variant_data WHERE Disease = '%s'" % (dis)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

def disGeneData(gene):
    sql_query = "SELECT * FROM `disease_data` WHERE `Gene` REGEXP '%s'" % (gene)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

def genData(gene):
    sql_query = "SELECT * FROM annotation_data WHERE Gene = '%s'" % (gene)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

def variantData(variant):
    sql_query = "SELECT * FROM `variant_data` WHERE Variant = '%s'" % (variant)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

result = {'disease': list(), 'variant': list()}
if "disease" in query:
    # Disease Data
    for i in disdata(queryTerm):
        result['disease'].append(i)
    
    # variant Data
    for i in variantDisData(queryTerm):
        result['variant'].append(i)
elif "gene" in query: 
    # Gene Data
    # result = list()
    # for i in genData(queryTerm):              #Get the gene data from annotation table
    #     result.append(i)
    # print(json.dumps(result))
    
    # Disease Data
    disLst = list()
    for i in disGeneData(queryTerm):
        result['disease'].append(i)
        disLst.append(i[0])
    
    # variant Data
    for i in disLst:
        for j in variantDisData(i):
            result['variant'].append(j)
elif "variant" in query:
    # variant Data
    disLst = list()
    for i in variantData(queryTerm):
        disLst.append(i[0])
        result['variant'].append(i)
        
    # Disease Data
    for i in disLst:
        for j in disdata(i):
            result['disease'].append(j)
print(json.dumps(result))