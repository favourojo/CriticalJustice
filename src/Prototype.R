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
install.packages("ggmap")
install.packages("maptools")
install.packages("rJava")
install.packages("tabulizer")

library(tidyverse)
library(ggplot2)
library(ggmap)
library(maptools)

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


#View my data
View(police911_Data)
View(neighborhood_Data)
View(pennsylvania_Data)
View(incident_Data)
View(fireIncident_Data)
View(police311_Data)
view(trafficData)

#Selecting 911 Police data
police911_Wilk <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E1") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk)

police911_Wilk2 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E2") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk2)

police911_Wilk3 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E3") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk3)

police911_Wilk4 <- police911_Data %>% filter(city_name == "WILKINSBURG", priority == "E4") %>% select(city_name,priority,service, priority_desc,description_short)
View(police911_Wilk4)

police911_Hazel <- police911_Data %>% filter(city_name == "PITTSBURGH", priority == "E1") %>% select(city_name,priority,service, priority_desc,description_short)
view(police911_Hazel)


police911_MountL1 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E1") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL1)

police911_MountL2 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E2") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL2)

police911_MountL3 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E3") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL3)

police911_MountL4 <- police911_Data %>% filter(city_name == "MOUNT LEBANON", priority == "E4") %>% select(city_name,priority,service,priority_desc,description_short)
view(police911_MountL4)

HazelwoodIncident <- incident_Data %>% filter(INCIDENTNEIGHBORHOOD == "Hazelwood") %>% select(INCIDENTLOCATION,INCIDENTNEIGHBORHOOD,INCIDENTHIERARCHYDESC,OFFENSES)
view(HazelwoodIncident)


#registering API key to utllize Google Maps
register_google(key = "AIzaSyBDZJll0yKPZlnjbepZAcWIxoH2VLbHM_k")

# load map of Pennsylvania 
qmap('Pennsylvania')

qmap('15227', zoom = 10, maptype = 'satellite')

head(myData)
# plot the hybrid Google Maps basemap
map <- qmap('Pennsylvania', zoom = 12, maptype = 'hybrid')

library(sp)
# change the crimes data into a SpatialPointsDataFrame



