# -*- coding: utf-8 -*-
"""
This is a script to conduct various data quality checks on data for the final project in ABE 65100.
    No data and gross error checks were deemed to be the most likely errors to occur with this dataset
    created by Justin Meyer
    last edited 2022-04-13
"""
# import required modules
import pandas as pd
import numpy as np

import os
os.chdir("C:/Users/justi/OneDrive/Documents/GitHub/final-project-meyer443")

def ReadData( fileName ):
    
    df = pd.read_csv( fileName, sep=',' ) # read in contents of csv using Pandas
    df = df.set_index('Reading')
    # define and initialize the missing data frame
    colNames = ['Logger','Temperature (C)','Dissolved Oxygen (mg/L)','Depth']
    ReplacedValuesDF = pd.DataFrame(0, index=["1. No Data","2. Gross Error"], columns=colNames)

    return( df, ReplacedValuesDF )

def Check01_RemoveNoDataValues( DataDF, ReplacedValuesDF ):
    #This check replaces the defined No Data value with the NumPy NaN value
    #so that further analysis does not use the No Data values.  Function returns
    #the modified DataFrame and a count of No Data values replaced.
    n = len(DataDF)
    m = n-1

    for i in range (0,m):
        for j in range(0,3):
            if DataDF.iloc[i,j] == " ": #removing any values =-999
                DataDF.iloc[i,j]= np.nan
       
    ReplacedValuesDF.iloc[0,0]=DataDF['Logger'].isna().sum()
    ReplacedValuesDF.iloc[0,1]=DataDF['Temperature (C)'].isna().sum()
    ReplacedValuesDF.iloc[0,2]=DataDF['Dissolved Oxygen (mg/L)'].isna().sum()
    ReplacedValuesDF.iloc[0,3]=DataDF['Depth'].isna().sum()

    return( DataDF, ReplacedValuesDF )
    
def Check02_GrossErrors( DataDF, ReplacedValuesDF ):
    #This function checks for gross errors, values well outside the expected 
    #range, and removes them from the dataset.  The function returns modified 
    #DataFrames with data the has passed, and counts of data that have not 
    #passed the check.
#Loggers
    for i in range (0,len(DataDF)-1):
           if (DataDF['Logger'].iloc[i]<99999) or (DataDF['Logger'].iloc[i]>999999): #Logger IDs are 6-digit numbers
               DataDF['Logger'].iloc[i]= np.nan
#Temperature
    for i in range (0,len(DataDF)-1): #replacing values outside of 0 to 35 range with nan
           if DataDF['Temperature (C)'].iloc[i]< (0) or DataDF['Temperature (C)'].iloc[i] >35:
               DataDF['Temperature (C)'].iloc[i]= np.nan
# DO    
    for i in range (0,len(DataDF)-1): #replacing values outside of 0 to 15 range with nan
           if DataDF['Dissolved Oxygen (mg/L)'].iloc[i]< (0) or DataDF['Dissolved Oxygen (mg/L)'].iloc[i] >15:
               DataDF['Dissolved Oxygen (mg/L)'].iloc[i]= np.nan
#Depth     
    for i in range (0,len(DataDF)-1): # replacing values outside of 0 to 20 range with nan
           if (DataDF['Depth'].iloc[i]<0) or (DataDF['Depth'].iloc[i]>20):
               DataDF['Depth'].iloc[i]= np.nan
               
    ReplacedValuesDF.iloc[1,0]=DataDF['Logger'].isna().sum()-ReplacedValuesDF.iloc[0,0]
    ReplacedValuesDF.iloc[1,1]=DataDF['Temperature (C)'].isna().sum()-ReplacedValuesDF.iloc[0,1]
    ReplacedValuesDF.iloc[1,2]=DataDF['Dissolved Oxygen (mg/L)'].isna().sum()-ReplacedValuesDF.iloc[0,2]
    ReplacedValuesDF.iloc[1,3]=DataDF['Depth'].isna().sum()-ReplacedValuesDF.iloc[0,3]

    return( DataDF, ReplacedValuesDF )

# the following condition checks whether we are running as a script, in which 
# case run the test code, otherwise functions are being imported so do not.
# put the main routines from your code after this conditional check.

if __name__ == '__main__':

    fileName = "allsites_depth.csv"
    DataDF, ReplacedValuesDF = ReadData(fileName)
   
    print("\nRaw data.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check01_RemoveNoDataValues( DataDF, ReplacedValuesDF )
    
    print("\nMissing values removed.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check02_GrossErrors( DataDF, ReplacedValuesDF )
    
    print("\nCheck for gross errors complete.....\n", DataDF.describe())
    
    print("\nAll processing finished.....\n", DataDF.describe())
    print("\nFinal changed values counts.....\n", ReplacedValuesDF)
   

#Read Data
    ReadData('allsites_depth.csv')

#Create copy of raw data
    Raw = pd.read_csv("allsites_depth.csv", delimiter=",")
    Raw = Raw.set_index('Reading')

#Plot Data
    import matplotlib.pyplot as plt
#Logger 
    plt.plot(DataDF.index, Raw['Logger'],'b*', label='Raw Data')
    plt.plot(DataDF.index, DataDF['Logger'],'r*', label='After Data Quality')
    plt.xlabel('Date')
    plt.ylabel('Logger ID Number')
    plt.legend()
    plt.savefig('Logger.png')
    plt.close()

#Temperature (C)
    plt.plot(DataDF.index, Raw['Temperature (C)'],'b*', label='Raw Data')
    plt.plot(DataDF.index, DataDF['Temperature (C)'],'r*', label='After Data Quality')
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.legend()
    plt.savefig('Temp.png')
    plt.close()

#DO
    plt.plot(DataDF.index, Raw['Dissolved Oxygen (mg/L)'],'b*', label='Raw Data')
    plt.plot(DataDF.index, DataDF['Dissolved Oxygen (mg/L)'],'r*', label='After Data Quality')
    plt.xlabel('Date')
    plt.ylabel('Dissolved Oxygen (mg/L)')
    plt.legend()
    plt.savefig('DO.png')
    plt.close()

#Depth
    plt.plot(DataDF.index, Raw['Depth'],'b*', label='Raw Data')
    plt.plot(DataDF.index, DataDF['Depth'],'r*', label='After Data Quality')
    plt.xlabel('Date')
    plt.ylabel('Depth (m)')
    plt.legend()
    plt.savefig('Depth.png', bbox_inches='tight')
    plt.close()


#Write Data to TAB Deliniated Files
    DataDF.to_csv('After_DataQuality.txt', sep='\t', index=True)

    ReplacedValuesDF.to_csv('ReplacedValues.txt', sep='\t', index=True)