# ***CriticalJustice***
 
![CriticalJustice](images/Logo.png)

## Abstract
This tool will visualize several factors in crime prevention and marginalization that either positively or negatively affect neighborhood development. 
Marginalization is the treatment of a person, group, or concept as insignificant or peripheral. Marginalization can exist in multiple forms, and can occur against 
many groups of people. The three main types of marginalization are social marginalization, economic marginalization, and political marginalization. 
Within the city of Pittsburgh, PA, there are huge difference between 
primarily black and white communities that contribute to neighborhood development. For instance, 
In the city of Pittsburgh, PA, communities where the black population is higher and the white population is lower, there tends to be a 
higher "need" of improvement of specific factors of infrastructure in that certain community. For instance, these factors can either differ from housing,



## Purpose
The purpose of this project is to shed light on the primarily Black communities in the city of Pittsburgh. 
With the use of queries, individuals will now be able to see how some factors such as Average Dispatches Per Shot Fired,  
Home Value, and Amount of Shots Fired, contribute to the marginalization of a certain community in Pittsburgh, PA. 


## References 
[Pittsburgh City Paper: Marginalization](https://www.pghcitypaper.com/pittsburgh/turnout-data-show-marginalized-communities-often-have-quietest-voice-in-allegheny-county-elections/Content?oid=22722946)

[Gun Violence](https://www.wesa.fm/politics-government/2022-07-26/allegheny-county-homicide-report)

## Run Instructions

SQLite3 
```
sqlite3 community.db
```

Query Instructions 
``` 
SELECT column FROM database WHERE condition 
````

Map Visualization
```
python3 shotsMap.py
```

