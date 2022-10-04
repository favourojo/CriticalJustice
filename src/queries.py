#!/usr/bin/env python3

# load libraries
import sqlite3

# define table attributes
myTable_str = "EMSData"
attribute1_str = "service"
attribute2_str = "priority"
attribute3_str = "priority_desc"

myQuery_str = f"SELECT {attribute1_str}, {attribute2_str}, {attribute3_str} FROM {myTable_str}"

print(f" [+] Running Query:\n {myQuery_str}")

# connect to the database
dbFile_str = "community.sqlite3" # name of the current database
conn = sqlite3.connect(dbFile_str) # open a connection to the base

# Send query to DB
myResult = conn.execute(myQuery_str) # run the query
print(f" [+] Results from query: {myResult}")

# Get result from query
queryInfo_list = myResult.fetchall()
print(f" [+] Fetchall results from query: {queryInfo_list}")

for i in queryInfo_list:
	print(f"\t[+] {i}")

conn.close() # close the database connection
