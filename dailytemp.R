###
# This is a script to generate daily average oxygen concentrations for individual loggers from an input file,
# used as part of my final project in ABE 65100
# written by Justin Meyer
# last edited 2022-05-04
#####

# load packages
library(dplyr)
library(lubridate)
library(tidyr)

# clear R memory
rm(list = ls())

setwd("C:/Users/justi/OneDrive/Documents/GitHub/final-project-meyer443")

loggers <- read.csv("allsites_depth.csv", na.strings = c("","NA"), header=TRUE) # read file
View(loggers)

as_tibble(loggers) # convert to tibble for date conversions

# join loggers and convert datetime format
data <- loggers %>% 
  unite("datetime", Date, Time, sep = " ") %>% 
  mutate(datetime = mdy_hm(datetime))

# function to get daily averages
dailytemp <- data %>% 
  mutate(day = floor_date(datetime, "day")) %>%
  group_by(day, Logger) %>%
  rename(Date = day) %>%
  summarize(temp = mean(Temperature..C.)) # get daily mean for each logger
  
View(dailytemp)
write.csv(dailytemp, 'Daily_Temperature_Averages.csv') # save file as csv
