# ***CriticalJustice: Visualizing the Impact of Crime Prevention in Neighborhood Development***
 
![CriticalJustice](images/newLogo.png)

## Abstract

CriticalJustice visualizes factors in the determinants of crime and the relationship with infrastructure that affect neighborhood development. This research investigates the relationship of police dispatches to these community neighborhoods. This will be carried out specifically by speculating that increasing infrastructure investment has a disproportionate yield. In predominantly Black communities, there appears to be an excess need for neighborhood development. Ergo, the attention desperately needed for neighborhood investment slowly starts to shift towards crime prevention. However, factors of a community, such as lack of infrastructure and over-policing, relate to why there is a difference in a demand of need between primarily Black and white communities.

## Purpose

The purpose of this propose is to raise awareness of neighborhood development challenges that are harming Pittsburgh's largely Black areas. The relationships and correlations between the downloaded datasets may be seen with the help of SQLite3. In addition, people will be able to observe how variables like __Average Dispatches Per Shot Fired__, __Fire Incidents__, and __Level of Need__ may contribute to the marginalization of a particular community in Pittsburgh, PA, and a greater level of crime, with the use of queries. Those who reside in suburban areas of Pittsburgh, Pennsylvania, where there is a lower rate of crime and a lesser need for services, sometimes disregard these variables because they do not experience these problems.

## Run Instructions in Terminal

### SQLite3 command:

```SQL
sqlite3 community.db
```

To successfully run this command, the user would need to navigate to the `src` directory that contains each of the datasets. Once this command has been run, the program will switch to the SQLite3 command line shell.

![SQL Command Shell](images/src.png)

After switching to the SQLite3 command line shell, the user can utilize the

```SQL
.tables
```

command to check that all tables are present within the SQLite3 database.

![.tables command](images/tables.png)

If the user wishes to view the factors that will be discussed of each dataset, the

```SQL
.schema
```

command to view the columns in each of the tables are present in the database.

![.schema command](images/schema1.png)

![.schema command2](images/schema2.png)

![.schema command3](images/schema3.png)

Query Command:

```SQL
SELECT "column" FROM "database" WHERE "condition"
```
With this query command, users will be able to view the connections or correlations between the datasets. Also, the users will be able to view
how specific neighborhoods in Pittsburgh, PA differ based on some key factors such as __Average Dispatches Per Shot Fired__, __Median Home Value__, and __Level of Need__.

# Map Visualization:

```python
python shotsMap.py
```

By running this command, a Folium map will be generated in the `index.html` file. The Folium map will contain an zoomed-in interactive map of the city of Pittsburgh, Pennsylvania. In the city of Pittsburgh, there will be markers that represents __Shots Fired Data__ that is located in the `shots.csv` file and __Fire Incident Data__ that is located in the `FireIncident.csv` file. Also, on the map there is a legend to indicate which color represents which data point and also a compass rose to indicate orientation. 

![Interactive Map](images/map.png)
