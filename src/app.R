#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("Welcome to CriticalJustice"),
  
  # Sidebar with a slider panel tht includes all the datasets 
  sidebarLayout(
    sidebarPanel("Datasets"),
    selectInput("select", label = h3("Choose which dataset to view"),
               choices = list("EMSData" = 1, "FireIncident" = 2, "StatsData" = 3),
               selected = 1,),
    hr(),
    
    fluidRow(
      column(3, 
             verbatimTextOutput("value"))),
  
  
    mainPanel(
      h1("Data Tables", align = "center"),
      img(src = "Logo.png", height = 140, width = 400),
    ) 
  )
  
)
  
  
# Define server logic required to draw a histogram
server <- function(input, output) {

    output$distPlot <- renderPlot({
        # generate bins based on input$bins from ui.R
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = 'darkgray', border = 'white',
             xlab = 'Waiting time to next eruption (in mins)',
             main = 'Histogram of waiting times')
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
