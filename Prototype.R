rm(list = ls()) # clear out the variables from memory to make a clean execution of the code.

# If you want to remove all previous plots and clear the console, run the following two lines.
graphics.off() # clear out all plots from previous work.

cat("\014") # clear the console

#################################################
#### Setup your common libraries
#################################################

# add your libraries here

library(tidyverse)
library(ggplot2)

#Selecting the file
myFile  <- file.choose() # pick the csv filename
myData <- read.csv(myFile) # load the data

View(myData)

# Filtering the data to select certain variables to test using select()
dat <- myData %>% select(county_name, crime_rate_per_100000, AG_ARRST, AG_OFF, MURDER, RAPE, ROBBERY, BURGLRY,
LARCENY, MVTHEFT, ARSON, population)
