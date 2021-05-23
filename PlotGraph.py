import sys

import matplotlib as mpl
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.ticker as mticker


# Plot bar chart of dataframe
def plotBarChart(df, monthOrYearLabel, yearLabel):

    # Try catch block to ensure Graph plotting fails safely
    try:
        # Change pandas settings
        pd.set_option('display.float_format', lambda x: '%.3f' % x)

        # Define Dataframe index for graphing
        df.index = df["Service Area"]

        # Plot dataframe to bar chart
        ax = df.plot(kind='barh', figsize=(15, 10))

        # Invert Y_Axis so biggest is at the top
        ax.invert_yaxis()

        # Turn off Scientific Notation
        plt.ticklabel_format(style='plain', axis='x')

        # Define grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
        plt.title(monthOrYearLabel + " Council Spending per Service Area " + yearLabel)
        plt.xlabel("Spending £'s")
        plt.ylabel("Service Area")

        # Save current figure for file creation later
        savedPlot = plt.gcf()

        # Show plotted graph
        plt.show()

        # Save plotted graph for later use
        savedPlot.savefig('graphs/standard/' + monthOrYearLabel + '_LCCSpending_' + yearLabel + '.png')

    except Exception as e:
        print("Error: Graph Plotting failed.\n", e)
        sys.exit()


# Plot bar chart of dataframe in logarithmic method (Better for seeing differences in scale)
def plotBarChartLog(df, monthOrYearLabel, yearLabel):

    # Try catch block to ensure Graph plotting fails safely
    try:
        # Change pandas settings
        pd.set_option('display.float_format', lambda x: '%.3f' % x)

        # Define Dataframe index for graphing
        df.index = df["Service Area"]

        # Plot dataframe to bar chart
        # used for Logarithmic comparison
        ax = df.plot(kind='barh', figsize=(15, 10), logx=True)

        # Invert Y_Axis so biggest is at the top
        ax.invert_yaxis()

        # Define grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
        plt.title(monthOrYearLabel + " Council Spending per Service Area (Logarithmic) " + yearLabel)
        plt.xlabel("Spending £'s")
        plt.ylabel("Service Area")

        # Save current figure for file creation later
        savedPlot = plt.gcf()

        # Show plotted graph
        plt.show()

        # Save plotted graph for later use
        savedPlot.savefig('graphs/logs/' + monthOrYearLabel + '_LCCSpending_' + yearLabel + '.png')

    except Exception as e:
        print("Error: Graph Plotting Logs failed.\n", e)
        sys.exit()

def plotLineGraph(df, monthOrYearLabel, yearLabel):

    # Try catch block to ensure Graph plotting fails safely
    try:

        fig, ax = plt.subplots()
        plt.figure(figsize=(15, 10))
        ax.set_xticklabels(df['month'].unique(), rotation=90)

        for name, group in df.groupby('Service Area'):
            ax.plot(group['month'], group['TotalVals'], label=name)

        ax.legend()

        #plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error: Graph Plotting Line failed.\n", e)
        sys.exit()
