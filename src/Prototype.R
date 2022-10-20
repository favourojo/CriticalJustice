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
install.packages("shiny")

library(tidyverse)
library(ggplot2)
library(ggmap)

~/shinyapp
|-- app.R
library(shiny)

#Define UI for Community Data Exploration ----
ui <- pageWithSidebar(
  
  # App title -----
  headerPanel("Community Data Exploration"),
  
  # Sidepar panel for inputs ---
  sidebarPanel(),
  
  #Main panel for displaying outputs ---
  mainPanel()
)

# Define server logic to plot various variables against mpg ----
server <- function(input, output) {
  
}
shinyApp(ui, server)

runApp("~/shinyapp")

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

#Fire data
building_Fire <- fireIncident_Data %>% filter(incident_type == 111) %>% select(incident_type,address,type_description,neighborhood,police_zone,latitude,longitude)                                                                        
view(building_Fire)

building__Fire_Wilk <- building_Fire %>% filter(neighborhood == "Wilkinsburg") %>% select(incident_type,address,neighborhood,type_description,police_zone,latitude,longitude)
view(building__Fire_Wilk)

#Neighborhood Data for majority Black neighborhood 

## Carrick
neighborhood_Carrick <- neighborhood_Data %>% filter(Pittsburgh.Neighborhood == "Carrick")



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



