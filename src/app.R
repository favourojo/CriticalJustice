#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(shiny)

# Define UI for application that displays datasets
if (interactive()) {
ui <- fluidPage(
  
  # Application title
  titlePanel("Welcome to CriticalJustice"),
  
  # Sidebar with a slider panel that includes all the data sets 
  sidebarLayout(
    
    #Sidebar panel that 
    sidebarPanel("Datasets"),
    sliderInput("select", label = h3("Choose which dataset to view"),
               choices = list("EMSData" = 1, "FireIncident" = 2, "StatsData" = 3),
               selected = 1,),
    hr(),
    fluidRow(column(3,verbatimTextOutput("value")))
  

    ) 
  )
  
  
server <- function(input, output) {
      output$value <- renderPrint({input$select})
  
  }
}
# Run the application 
shinyApp(ui = ui, server = server)
