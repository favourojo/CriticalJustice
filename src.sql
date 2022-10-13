import mysql.connector as msql
from mysql.connector import Error
import pandas as pd

empdata = pd.read_csv('/home/ojof/Documents/COMP/CriticalJustice/data/911_Data.csv', index_col=False, delimiter = ',')
empdata.head()

try:
    conn = msql.connect(host='localhost', user ='favour',
    password ='babies410')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE EMS")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
    