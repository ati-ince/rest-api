from click import password_option
import mysql.connector
import sys
import boto3
import os

ENDPOINT="database-ati.c9axqirfrvzk.eu-central-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="eu-central-1c"
DBNAME="the_db"

passwrd = "19881988.MySql"

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=passwrd ,port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))     