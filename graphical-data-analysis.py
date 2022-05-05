# -*- coding: utf-8 -*-
"""
This is a script to run graphical data analysis on my final project data.
    Graphical analysis includes a histogram, scatterplots, and a QQ plot to gain a better understanding of the data
    created by Justin Meyer
    Last edited 2022-05-04
"""

# importing modules
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

import os
os.chdir('C:/Users/justi/OneDrive/Documents/GitHub/final-project-meyer443')

def read_data( fileName ):
    df = pd.read_csv( fileName, sep=',' ) # read in contents of csv using Pandas
    
    df = df.assign(Depth = df['Logger']) # create column for depth with duplicate values from Logger column
    
    # replace values in Depth column with recorded depths from Lowrance
    df.loc[df['Logger'] == 638867, 'Depth'] = 6.5
    df.loc[df['Logger'] == 280741, 'Depth'] = 11.0
    df.loc[df['Logger'] == 694855, 'Depth'] = 7.6
    df.loc[df['Logger'] == 704690, 'Depth'] = 5.9
    df.loc[df['Logger'] == 666469, 'Depth'] = 3.9
    df.loc[df['Logger'] == 765378, 'Depth'] = 7.5
    df.loc[df['Logger'] == 753018, 'Depth'] = 4.5
    df.loc[df['Logger'] == 691297, 'Depth'] = 5.5
    df.loc[df['Logger'] == 207032, 'Depth'] = 8.4
    df.loc[df['Logger'] == 195286, 'Depth'] = 5.8
    df.loc[df['Logger'] == 679953, 'Depth'] = 4.3
    df.loc[df['Logger'] == 893976, 'Depth'] = 8.2
    df.loc[df['Logger'] == 151343, 'Depth'] = 7.9
    df.loc[df['Logger'] == 569373, 'Depth'] = 5.6
    df.loc[df['Logger'] == 393808, 'Depth'] = 5.0
    df.loc[df['Logger'] == 977126, 'Depth'] = 10.7
    df.loc[df['Logger'] == 270520, 'Depth'] = 10.8
    df.loc[df['Logger'] == 670871, 'Depth'] = 3.9
    df.loc[df['Logger'] == 207575, 'Depth'] = 11.0
    df.loc[df['Logger'] == 244238, 'Depth'] = 8.5
    df.loc[df['Logger'] == 118921, 'Depth'] = 12.3
    df.loc[df['Logger'] == 886057, 'Depth'] = 3.4
    df.loc[df['Logger'] == 704192, 'Depth'] = 3.2
    df.to_csv(r'C:\Users\justi\OneDrive\Documents\GitHub\final-project-meyer443\allsites_depth.csv', index = None, header = True)
    print(df)
    return df # return for use in ensuing functions    

def read_info( fileName ):
    dataFrame = pd.read_csv( fileName, sep=',') # read in contents of csv using Pandas
    return dataFrame # return for use in ensuing functions
       
def generate_histogram_plot( dataFrame, outFileName ):
    dataFrame.hist(column='Dissolved Oxygen (mg/L)', bins=20, range=(0,14)) # read oxygen data with 20 bins from 0-14 mg/L (realistic range of concentrations)
    plt.title('Histogram of Dissolved Oxygen Measurements')
    plt.xlabel('Dissolved Oxygen (mg/L)')
    plt.ylabel('Frequency')
    plt.savefig( outFileName, bbox_inches='tight') # 
    plt.close() # close pyplot priot to starting next function
 
def generate_kde_plot( dataFrame, outFileName ):
    sns.kdeplot(dataFrame['Dissolved Oxygen (mg/L)'], bw_adjust=0.7, cut=0) # use DO data to generate kde plot, adjusting bin width and cutting off extreme estimates
    plt.title('KDE Plot of Dissolved Oxygen Concentrations')
    plt.xlabel('Dissolved Oxygen (mg/L)')
    plt.ylabel('Density')
    plt.savefig( outFileName, bbox_inches='tight' )
    plt.close()

def generate_lat_long_plot( dataFrame, outFileName ):
    plt.scatter(dataFrame['longitude'], dataFrame['latitude'], s=10) # plot data loggers using coordinates in scatterplot, 's' to manipulate point size
    plt.title('Location of data loggers')
    plt.xlabel('Longitude (degrees)') # x-y axes just like on a map
    plt.ylabel('Latitude (degrees)')
    plt.savefig( outFileName, bbox_inches='tight' )
    plt.close()

def generate_cdf_plot( dataFrame, outFileName ):
    dpth=np.sort(dataFrame['Dissolved Oxygen (mg/L)']) # sort array of depth data for normalization
    cd=np.linspace(0,1,len(dataFrame['Dissolved Oxygen (mg/L)'])) # evenly spaced for plotting
    plt.plot(dpth, cd) # plot depth vs cumulative distribution
    plt.title('Normalized CDF of Dissolved Oxygen Concentrations')
    plt.xlabel('Dissolved Oxygen (mg/L)')
    plt.ylabel('Cumulative Distribution')
    plt.savefig( outFileName, bbox_inches='tight' )
    plt.close()

def generate_scatter_plot( dataFrame, outFileName ):
    plt.scatter(dataFrame['Q'], dataFrame['Dissolved Oxygen (mg/L)'], marker=".") # plot points of q vs oxygen, "." marker to manipulate point size
    plt.title('Relationship between Dissolved Oxygen and Internal Data Quality Reading')
    plt.xlabel('Q')
    plt.ylabel('Dissolved Oxygen (mg/L)')
    plt.savefig( outFileName, bbox_inches='tight' )
    plt.close()

def generate_new_scatter_plot( dataFrame, outFileName ):
    plt.scatter(dataFrame['Depth'], dataFrame['Dissolved Oxygen (mg/L)'], marker=".") # plot points of depth vs oxygen, "." marker to manipulate point size
    plt.title('Relationship between Dissolved Oxygen and Depth')
    plt.xlabel('Depth (m)')
    plt.ylabel('Dissolved Oxygen (mg/L)')
    plt.savefig( outFileName, bbox_inches='tight' )
    plt.close()
    
def generate_quantile_plot( dataFrame, outFileName ): # generate QQ plot
    stats.probplot(dataFrame['Temperature (C)'], dist='norm', plot=plt)
    plt.ylabel('Ordered Values (C)')
    plt.savefig( outFileName, bbox_inches='tight')

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # set input and output file names
    oxygen = 'allsites.csv'
    loggerinfo = 'loggerinfo.csv'
   
    # open and read data files
    dataFrame = read_data( oxygen )
    infoDF = read_info( loggerinfo )
    
    # generate histogram figure
    outHistName = "histogram.png"
    generate_histogram_plot( dataFrame, outHistName )

    # generate kde figure
    outKdeName = "kde.png"
    generate_kde_plot( dataFrame, outKdeName )
    
    # generate lat-long figure
    outLatLongName = "lat-long.png"
    generate_lat_long_plot( infoDF, outLatLongName )

    # generate cdf figure
    outCdfName = "cdf.png"
    generate_cdf_plot( dataFrame, outCdfName )
    
        
    # generate scatter plot figure
    outScatName = "scatter.png"
    generate_scatter_plot( dataFrame, outScatName )
        
    # generate scatter plot figure
    outScatName = "depth-scatter.png"
    generate_new_scatter_plot( dataFrame, outScatName )
    
    # generate quantile figure
    outQuanName = "quantile.png"
    generate_quantile_plot( dataFrame, outQuanName )
  