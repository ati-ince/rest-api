import mysql.connector

ENDPOINT="database-ati.c9axqirfrvzk.eu-central-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="eu-central-1c"
DBNAME="the_db"
PASSWRD = "19881988.MySql"

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PASSWRD ,port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
    print('hellllooooo !!!!!!!!!!!!!')
except Exception as e:
    print("Database connection failed due to {}".format(e))     