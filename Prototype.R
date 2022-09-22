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


library(tidyverse)
library(ggplot2)
library(ggmap)
library(maptools)


#Selecting the file
myFile  <- file.choose() # pick the csv filename
myData <- read.csv(myFile) # load the data

View(myData)
register_google(key = "AIzaSyBDZJll0yKPZlnjbepZAcWIxoH2VLbHM_k")

# load map of Pennsylvania 
qmap('Pennsylvania')

qmap('15227', zoom = 10, maptype = 'satellite')

head(myData)
# plot the hybrid Google Maps basemap
map <- qmap('Pennsylvania', zoom = 12, maptype = 'hybrid')

library(sp)
# change the crimes data into a SpatialPointsDataFrame



