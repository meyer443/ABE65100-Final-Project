#!/bin/env python
# This is a script to use descriptive statistics calculated previously to produce presentation-quality graphics
# and save them as PNG files for use in a presentation
#   written by Justin Meyer
#   last edited 2022-05-04
#

# import required modules
import pandas as pd
import matplotlib.pyplot as plt

import os
os.chdir('c:/Users/justi/OneDrive/Documents/GitHub/final-project-meyer443')

def ReadData( fileName ):
    """This function takes a filename as input, and returns a dataframe with
    raw data read from that file in a Pandas DataFrame."""

    # open and read the file
    DataDF = pd.read_csv( fileName, sep=',' )
    return DataDF

def Plot_Oxygen(DataDF, outFileName):
    plt.scatter(DataDF["Date"], DataDF["avg"], marker=".") # plot date vs oxygen
    plt.xlabel('Date')
    plt.xticks([])
    plt.ylabel('Average Daily Dissolved Oxygen (mg/L)')
    plt.savefig('Daily_Oxygen.png', dpi=96) # save the plot as PNG with 96 dpi
    plt.close()



# the following condition checks whether we are running as a script, in which 
# case run the test code, otherwise functions are being imported so do not.
# put the main routines from your code after this conditional check.

if __name__ == '__main__':

    fileName = "Daily_Oxygen_Averages.csv"
    
    DataDF = ReadData( fileName )

# Figure generation
    outPlotName = "Daily_Oxygen.png"
    Plot_Oxygen( DataDF, outPlotName )
