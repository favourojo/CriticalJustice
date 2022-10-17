#!/usr/bin/python
# load libraries
import sqlite3
from sqlite3 import Error
import pandas as pd
import csv
import sys

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


create_EMSData_table = """
CREATE TABLE IF NOT EXISTS EMSData (
    geoid INTEGER NOT NULL,
    service VARCHAR NOT NULL,
    priority VARCHAR NOT NULL,
    priority_desc VARCHAR NOT NULL,
    call_year INTEGER NOT NULL,
    description_short VARCHAR NOT NULL,
    city_name VARCHAR NOT NULL
);
"""

execute_query(connection, create_EMSData_table)


create_NeighborhoodData_table = """
CREATE TABLE IF NOT EXISTS NeighborhoodData (
    GEOID INTEGER NOT NULL,
    Municipality VARCHAR NOT NULL,
    Pittsburgh Neighborhood VARCHAR NOT NULL,
    Total Pop INTEGER NOT NULL,
    White Pop Rate REAL NOT NULL,
    Black Pop Rate REAL NOT NULL,
    His Pop Rate REAL NOT NULL,
    Family Poverty Rate REAL NOT NULL,
    Rate of Single Mothers REAL NOT NULL,
    Average Dispatches for Shots Fired per Five Hundred REAL NOT NULL,
    Median Home Value INTEGER NOT NULL,
    Level of Need VARCHAR NOT NULL
);
"""

execute_query(connection, create_NeighborhoodData_table)

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


create_EMSData = """
INSERT INTO 
    EMSData (service, priority, priority_desc, call_year, description_short, city_name, geoid)
VALUES
    ('EMS','E2','EMS Standard Advanced Life Support response', 'Removed', 'PGH', 'PITTSBURGH', 420035631002037),
    ('EMS','E2','EMS Standard Advanced Life Support response', 'SICK', 'PGH', 'PITTSBURGH', 420031803002005),
    ('EMS','E1','EMS Advanced Life Support life threatening response','ABDOMINAL PAIN','PGH','PITTSBURGH',420032503001002),
    ('EMS','E1','EMS Advanced Life Support life threatening response','STROKE','SWS','SWISSVALE',420035154011012),
    ('EMS','E1','EMS Advanced Life Support life threatening response','FALL','CLA','CLAIRTON',420034927001021);
"""

create_NeighborhoodData = """
INSERT INTO 
    NeighborhoodData(GEOID, Municipality, Pittsburgh Neighborhood, Total Pop, White Pop Rate, Black Pop Rate, Hispanic Pop Rate, Family Poverty Rate)


"""




execute_query(connection, create_EMSData)


    


def main():
    # database file input
    con = sqlite3.connect(sys.argv[1])
    cur = con.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS)