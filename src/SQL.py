#!/usr/bin/python
# load libraries

import sqlite3
from sqlite3 import Error
import pandas as pd
import csv
import os

def create_connection(path):
    connection = None 
    try: 
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("E:\\community.sqlite")


def execute_query(connection, query):
    cursor = connection.cursor()
    try: 
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try: 
        cursor.execute(query)
        result = cursor.fetchall()
        return result 
    except Error as e:
        print(f"The error '{e}' occurred")


select_EMSdata = "SELECT * from EMSData"
EMSdata = execute_read_query(connection, select_EMSdata)

for EMS in EMSdata:
    print(EMS)

select_EMS_Stats = """
SELECT



"""

"""
select_StatsData = "SELECT * from StatsData"
StatsData = execute_read_query(connection, select_StatsData)

for stats in StatsData:Median
    print(stats)
"""


create_EMSData_table = """
CREATE TABLE IF NOT EXISTS EMSData (
    geoid INTEGER PRIMARY KEY NOT NULL,
    service VARCHAR NOT NULL,
    priority VARCHAR NOT NULL,
    priority_desc VARCHAR NOT NULL,
    call_year INTEGER NOT NULL,
    description_short VARCHAR NOT NULL,
    city_name VARCHAR NOT NULL,
    FOREIGN KEY (GEOID)
        REFERENCES StatsData (GEOID)
);
"""

execute_query(connection, create_EMSData_table)


create_StatsData_table = """
CREATE TABLE IF NOT EXISTS StatsData (
    GEOID INTEGER PRIMARY KEY NOT NULL,
    Municipality VARCHAR NOT NULL,
    Pittsburgh_Neighborhood VARCHAR NOT NULL,
    Total_Pop INTEGER NOT NULL,
    White_Pop_Rate REAL NOT NULL,
    Black_Pop_Rate REAL NOT NULL,
    His_Pop_Rate REAL NOT NULL,
    Family_Poverty_Rate REAL NOT NULL,
    Rate_of_Single_Mothers REAL NOT NULL,
    Average_Dispatches_for_Shots_Fired_per_Five_Hundred REAL NOT NULL,
    Home_Median_Value INTEGER NOT NULL,
    Median_Gross_Rent INTEGER NOT NULL,
    Level_of_Need VARCHAR NOT NULL
);
"""

execute_query(connection, create_StatsData_table)

create_TrafficData_table = """
CREATE TABLE IF NOT EXISTS TrafficData (
    GENDER VARCHAR NOT NULL,
    RACE VARCHAR NOT NULL,
    AGE VARCHAR NOT NULL,
    INCIDENTLOCATION VARCHAR NOT NULL,
    OFFENSES VARCHAR NOT NULL,
    NEIGHBORHOOD VARCHAR NOT NULL
);
"""

execute_query(connection, create_TrafficData_table)

create_FireIncident_table = """
CREATE TABLE IF NOT EXISTS FireIncident (
    call_no VARCHAT NOT NULL,
    incident_type INTEGER NOT NULL,
    type_description VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    alarm _time VARCHAR NOT NULL,
    neighborhood VARCHAR NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);
"""

execute_query(connection, create_FireIncident_table)





    

