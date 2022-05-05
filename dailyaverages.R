###
# This is a script to generate daily average temperature concentrations for individual loggers from an input file,
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

loggers <- read.csv("allsites_depth.csv", na.strings = c("","NA"), header=TRUE)
View(loggers)

as_tibble(loggers) # convert to tibble for datetime conversion

data <- loggers %>% 
  unite("datetime", Date, Time, sep = " ") %>% 
  mutate(datetime = mdy_hm(datetime)) # convert to usable format

# function to get daily averages
dailyaverage <- data %>% 
  mutate(day = floor_date(datetime, "Temperature (C)")) %>%
  group_by(day, Logger) %>% # organize data by logger by day
  rename(Temp = Temperature (C)) %>%
  summarize(avg = mean(Dissolved.Oxygen..mg.L.)) # get daily averages
  
View(dailyaverage)
write.csv(dailyaverage, 'Daily_Temperature_Averages.csv') # save as csv
