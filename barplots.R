# This is a script to generate summary statistic figures for a dissolved oxygen database
      # written to satisfy the final project in ABE 65100
  # by Justin Meyer
  # last edited 2022-05-04

rm(list = ls()) # clear environment

library(ggplot2) # load required package

setwd("C:/Users/justi/OneDrive/Documents/GitHub/final-project-meyer443") # set working directory

# read in csv
oxy <- read.csv("TimeSpent.csv") # read in and view csv
View(oxy)

# bar graphs for 2 and 4.5 mg/l
ggplot(oxy, aes(x=Site, y=Hours_two)) + # 2.0 mg/L threshold
  geom_bar(stat="identity", fill="aquamarine") +
  xlab("Site") + ylab("Hours") +
  ggtitle("Time spent <= 2.0 mg/L") +
  geom_text(aes(label=Site), vjust=1.6, color="black", size=3.5) + # label bars by site number
  # discrete x axis to separate out bars to independent sites
  scale_x_discrete(breaks=0:22,
                     labels=c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "18", "19", "20", "21", "23", "24", "26"))
ggsave("2time.png") # save to directory

ggplot(oxy, aes(x=Site, y=Hours_four)) + # 4.5 mg/L threshold
  geom_bar(stat="identity", fill="aquamarine") +
  xlab("Site") + ylab("Hours") +
  ggtitle("Time spent <= 4.5 mg/L") +
  geom_text(aes(label=Site), vjust=1.1, color="black", size=3.5) +
  # sites 17 and 22 had their data loggers flood, no data available
  scale_x_discrete(breaks=0:22,
                   labels=c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "18", "19", "20", "21", "23", "24", "26"))
ggsave("4time.png") # save to directory

