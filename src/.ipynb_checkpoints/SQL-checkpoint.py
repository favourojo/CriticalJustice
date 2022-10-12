#!/usr/bin/env python3

# load libraries
import mysql.connector
from mysql.connector import Error
import pandas as pd

empdata = pd.read_csv('/home/ojof/Documents/COMP/CriticalJustice/data/911_Data.csv', index_col=False, delimiter = ',')
empdata.head()

"""
def create_connection(host_name, user_name, user_password, db_name):
	try: 
		conn = mysql.connector.connect(
            host='localhost',
            user='favourojo',
            passwd='babies410',
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE community")
            print("Database is created")
	except Error as e:
		print(f"The error '{e}' occured")
	
	return connection 

connection = create_connection("localhost", "root", "", "comm_app")


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE comm_app"
create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_EMSData_table = 
CREATE TABLE IF NOT EXISTS EMSData (
    geoid INT AUTO_INCREMENT,
    service VARCHAR NOT NULL,
    priority VARCHAR NOT NULL,
    priority_desc VARCHAR NOT NULL,
    call_year INTEGER NOT NULL,
    description_short VARCHAR NOT NULL,
    city_name VARCHAR NOT NULL,
    PRIMARY KEY (geoid)
) ENGINE = InnoDB


execute_query(connection, create_EMSData_table)

create_NeighborhoodData_table = 
CREATE TABLE IF NOT EXISTS NeighborhoodData (
    GEOID INTEGER NOT NULL,
    Municipality VARCHAR NOT NULL,
    Pittsburgh Neighborhood VARCHAR NOT NULL,
    Total Pop 2014-2018 INTEGER NOT NULL,
    White Pop Rate 2014-2018 INTEGER NOT NULL,
    Black Pop Rate 2014-2018 INTEGER NOT NULL,
    His or Lat Pop Rate 2014-2018 INTEGER NOT NULL,
    Family Poverty Rate 2014-2018 INTEGER NOT NULL,
    Rate of Single Mothers 2014-2018 INTEGER NOT NULL,
    Rate of those 25 and up without at least Bachelor's 2014-2018 INTEGER NOT NULL,
    Average 911 Dispatches for Shots Fired per 500 INTEGER NOT NULL,
    Median Home Value 2014-2018 INTEGER NOT NULL,
    Level of Need VARCHAR NOT NULL,
    FOREIGN KEY fk_GEOID (GEOID) REFERENCES EMSDATA(geoid)
    PRIMARY KEY (geoid)
) ENGINE = InnoDB

execute_query(connection, create_NeighborhoodData_table)


create_EMSDATA = 
INSERT INTO 
`EMSData` (`service`, `priority`, `priority_desc`, `call_year`, `description_short`, `city_name`, `geoid`)
VALUES
('EMS', 'E2', 'EMS Standard Advanced Life Support response', 2020, 'Removed', 'PITTSBURGH', 420035631002037)



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


    select_EMSData = "SELECT * FROM EMSData"
    EMSD = execute_read_query(connection, select_EMSData)
"""
    