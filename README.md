# ***CriticalJustice***
 
![CriticalJustice](images/Logo.png)

## Abstract
Throughout history, marginalization has affected society by making it a less equal, stable, and enjoyable place to live in, whether it be economic, social, or political
marginalization. Marginalization is the treatment of a person, group, or concept as insignificant or peripheral. It can exist in multiple forms, and can 
occur against many groups of people. An aspect of marginalization individuals are not aware of is how it drives the crime rate in communities. With the combination 
of marginalization and crime in a society, the need for crime prevention differs between primarily black communities and primarily white communities. In primarily 
black communities, there is an excess need for neighborhood development, but it is overshadowed by the assumption that crime prevention should be the focus because 
of the high number of police dispatches in these communities compared to primarily white communities. The tool, CriticalJustice, will visualize several factors in 
crime prevention and marginalization that either positively or negatively affect neighborhood development. 


## Purpose
The purpose of this project is to shed light on the issues that are affecting primarily black communities in the city of Pittsburgh. 
With the use of queries, individuals will now be able to see how some factors such as __Average Dispatches Per Shot Fired__, __Median Home Value__, 
and __Level of Need__, contribute to the marginalization of a certain community in Pittsburgh, PA. These factors tend to be overlooked by individuals
that live in the suburban communities of Pittsburgh, PA because they do not face these issues. 


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

