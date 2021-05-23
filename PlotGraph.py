from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.ticker as mticker


# Plot bar chart of dataframe
def plotBarChart(df):

    # Reset Index
    #df.reset_index()

    # Define figure size
    fig = plt.figure(figsize=(30, 20))
    fig.set_size_inches(30, 20)

    # Turn off Scientific Notation
    #sn = ax.get_xaxis().get_major_formatter().set_useOffset(False)

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.yaxis.get_major_formatter().set_useOffset(False)

    # Plot dataframe to bar chart
    df.index = df["Service Area"]
    df.plot(kind='barh', figsize=(15, 10), ax=ax)

    # used for Logarithmic comparison
    #df.plot(kind='barh', figsize=(15, 10), logx=True)

    # Define plotting as bar chart
    #df['TotalVals'].plot(x="Service Area", kind='barh')



    # Define grid
    #plt.ticklabel_format(useOffset=False)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
    plt.title("Yearly Council Spending per Service Area")
    plt.xlabel("Spending")
    plt.ylabel("Service Area")



    # Show plotted graph
    plt.show()
