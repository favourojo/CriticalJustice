rm(list = ls()) # clear out the variables from memory to make a clean execution of the code.

# If you want to remove all previous plots and clear the console, run the following two lines.
graphics.off() # clear out all plots from previous work.

cat("\014") # clear the console

#################################################
#### Setup your common libraries
#################################################

# add your libraries here

install.packages("tidyverse")
install.packages("ggplot2")
install.packages("gstat")

library(tidyverse)
library(ggplot2)
library(ggmap)
library(sp)
library(gstat)

update.packages(checkBuilt = TRUE, ask=FALSE)

#Selecting the file
myFile  <- file.choose() # pick the csv filename
police911_Data <- read.csv(myFile) # load the data

myFile2 <- file.choose()
neighborhood_Data <- read.csv(myFile2)

myFile3 <- file.choose()
pennsylvania_Data <- read.csv(myFile3)

myFile4 <- file.choose()
incident_Data <- read.csv(myFile4)

myFile5 <- file.choose()
fireIncident_Data <- read.csv(myFile5)

myFile6 <- file.choose()
police311_Data <- read.csv(myFile6)

myFile7 <- file.choose()
trafficData <- read.csv(myFile7)

myFile8 <- file.choose()
CrimeData <- read.csv(myFile8)

myFile9 <- file.choose()
ShotData <- read.csv(myFile9)

myFile10 <- file.choose()
ShotData2 <- read.csv(myFile10)

#View my data
View(police911_Data)
View(neighborhood_Data)
View(pennsylvania_Data)
View(incident_Data)
View(fireIncident_Data)
View(police311_Data)
view(trafficData)
view(CrimeData)
view(ShotData)
view(ShotData2)

#Selecting Crime Data 
Allegheny_Data <- CrimeData %>% filter(county_name == "Allegheny County, PA") %>% select(county_name,crime_rate_per_100000,AG_ARRST,ARSON,population)
View(Allegheny_Data)

# Wilkinsburg EMS Priority
police911_Wilk <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E1") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk)

police911_Wilk2 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E2") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk2)

police911_Wilk3 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E3") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk3)

police911_Wilk4 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E4") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk4)

# Mount Lebanon EMS Priority
police911_MountL1 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E1") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL1)

police911_MountL2 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E2") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL2)

police911_MountL3 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E3") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL3)

police911_MountL4 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E4") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL4)

#Selecting 311 data
police311_Wilk <- police311_Data %>% filter(NEIGHBORHOOD == "Hazelwood") %>% select(NEIGHBORHOOD, REQUEST_TYPE, DEPARTMENT)
View(police311_Wilk)

#111 Fire incidient type
building_Fire <- fireIncident_Data %>% filter(incident_type == 111) %>% select(incident_type,alarm_time,address,type_description,neighborhood,police_zone,latitude,longitude)                                                                        
view(building_Fire)

#Neighborhood Data for majority Black neighborhood 

#Wilk Home value
Wilk_Home <- neighborhood_Data %>% filter(Municipality == "Wilkinsburg") %>% select(Municipality,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(Wilk_Home)

#111 Fire data for Wilkinsburg
building__Fire_Wilk <- building_Fire %>% filter(neighborhood == "Wilkinsburg") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building__Fire_Wilk)

#Traffic data for Wilkinsburg
Traffic_Wilk <- trafficData %>% filter(NEIGHBORHOOD == "East Hills") %>% select(GENDER,RACE,AGE,CITEDTIME,INCIDENTLOCATION,OFFENSES,NEIGHBORHOOD)
view(Traffic_Wilk)

#Homewood North Home value 
Homewood_value <- neighborhood_Data %>% filter(Pittsburgh_Neighborhood == "Homewood North") %>% select(Municipality,Pittsburgh_Neighborhood,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(Homewood_value)

#111 Fire data for Homewood North 
building_Fire_Home <- building_Fire %>% filter(neighborhood == "Homewood North") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_Home)

#111 Fire data for Homewood South
building_Fire_Homes <- building_Fire %>% filter(neighborhood == "Homewood South") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_Homes)

#Homewood South value
Homewood_valueS <- neighborhood_Data %>% filter(Pittsburgh_Neighborhood == "Homewood South") %>% select(Municipality,Pittsburgh_Neighborhood,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(Homewood_valueS)

#Neighborhood Data for majority White neighborhood 

#Bethel Park Home value
Bethel_Home <- neighborhood_Data %>% filter(Municipality == "Bethel Park") %>% select(Municipality,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(Bethel_Home)

#111 Fire data for Bethel Park
building_Fire_Bethel <- fireIncident_Data %>% filter(neighborhood == "Bethel Park") %>% select(incident_type,address,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_Bethel)

#General Fire Data for Squirrel Hill
fire_Squirrel <- fireIncident_Data %>% filter(neighborhood == "Squirrel Hill South") %>% select(incident_type,address,neighborhood,type_description,police_zone,latitude,longitude)
view(fire_Squirrel)

#111 Fire data for Squirrel Hill South 
building_Fire_Squirrel <- building_Fire %>% filter(neighborhood == "Squirrel Hill South") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_Squirrel)

#Squirrel Hill South Home Value
SquirrelS_Home <- neighborhood_Data %>% filter(Pittsburgh_Neighborhood == "Squirrel Hill South") %>% select(Pittsburgh_Neighborhood,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(SquirrelS_Home)

#Squirrel Hill North Home Value
SquirrelN_Home <- neighborhood_Data %>% filter(Pittsburgh_Neighborhood == "Squirrel Hill North") %>% select(Pittsburgh_Neighborhood,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(SquirrelN_Home)


#111 Fire data for Squirrel Hill North 
building_Fire_SquirrelN <- building_Fire %>% filter(neighborhood == "Squirrel Hill North") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_SquirrelN)

#111 Fire data for Squirrel Hill South
building_Fire_SquirrelS <- building_Fire %>% filter(neighborhood == "Squirrel Hill South") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_SquirrelS)

#Traffic data for Banksville
Traffic_Banks <- trafficData %>% filter(NEIGHBORHOOD == "Banksville") %>% select(GENDER,RACE,AGE,CITEDTIME,INCIDENTLOCATION,OFFENSES,NEIGHBORHOOD)
view(Traffic_Banks)



#Upper Saint Clair Home value
UpperSC_Home <- neighborhood_Data %>% filter(Municipality == "Upper St. Clair Twp") %>% select(Municipality,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(UpperSC_Home)

#Banksville Home value
Banks_Home <- neighborhood_Data %>% filter(Pittsburgh_Neighborhood == "Banksville") %>% select(Municipality,Total_Pop,White_Pop_Rate,Black_Pop_Rate,Average_Dispatches_for_Shots_Fired_per_Five_Hundred,Home_Median_Value,Median_Gross_Rent,Level_of_Need)
view(Banks_Home)

#111 Fire data for Banksville
building_Fire_Banks <- building_Fire %>% filter(neighborhood == "Banksville") %>% select(incident_type,address,alarm_time,neighborhood,type_description,police_zone,latitude,longitude)
view(building_Fire_Banks)


## Mapping shots fired data
register_google(key = "AIzaSyBDZJll0yKPZlnjbepZAcWIxoH2VLbHM_k", write = TRUE)

coords <- cbind(longitude = as.numeric(as.character(ShotData$longitude)), latitude
                = as.numeric(as.character(ShotData$latitude)))
shot.pts <- SpatialPointsDataFrame(coords, ShotData, proj4string = CRS("+init=epsg:4326"))
plot(shot.pts, pch = ".", col = "darkred")
qmap(location = "Pittsburgh", zoom = 10, maptype = 'satellite')
head(ShotData)

map + geom_point(data = ShotData, aes(x = latitude, y = longitude),color = "red", size=3, alpha=0.5)








