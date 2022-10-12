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



