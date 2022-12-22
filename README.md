# ***CriticalJustice***
 
![CriticalJustice](images/Logo.png)

## Abstract

CriticalJustice visualizes factors in the determinants of crime and the relationship with infrastructure that affect neighborhood development. In predominantly Black communities, there appears to be an excess need for neighborhood development, but it is overshadowed by the assumption that crime prevention should be the focus because of the high number of police dispatches in these communities compared to primarily white communities. Ergo, the attention desperately needed for neighborhood investment slowly starts to shift towards crime prevention. However, factors of a community, such as lack of infrastructure and over-policing, relate to why there is a difference in a demand of need between primarily Black and white communities.


## Purpose

The purpose of this project is to shed light on the issues that are affecting primarily black communities in the city of Pittsburgh. With the use of queries, individuals will now be able to see how some factors such as __Average Dispatches Per Shot Fired__, __Median Home Value__, and __Level of Need__, contribute to the marginalization of a certain community in Pittsburgh, PA. These factors tend to be overlooked by individuals that live in the suburban communities of Pittsburgh, PA because they do not face these issues.


## Run Instructions in Terminal

SQLite3 command:

```
sqlite3 community.db
```

To successfully run this command, the user would navigate to hte `data` directory that contains each of the datasets. Once this command has been run, the program will switch to the SQLite3 command line shell.

![SQL Command Shell](images/SQL.png)

Query Instructions:

``` 
SELECT column FROM database WHERE condition 
````

Map Visualization:

```
python3 shotsMap.py
```
