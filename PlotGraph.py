import sys
import pandas as pd
import matplotlib.pyplot as plt


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


# Plot line graph showing top 5 spending departments in LCC per month over the year
def plotLineGraph(df, monthOrYearLabel, yearLabel):

    # Try catch block to ensure Graph plotting fails safely
    try:
        # Plot subplots on line graph
        fig, ax = plt.subplots(figsize=(15, 10))

        # Set months on X axis
        ax.set_xticklabels(df['month'].unique(), rotation=90)

        # Show lines by service area
        for name, group in df.groupby('Service Area'):
            ax.plot(group['month'], group['TotalVals'], label=name)
        ax.legend()

        # Turn off Scientific Notation
        plt.ticklabel_format(style='plain', axis='y')

        # Define grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
        plt.title(monthOrYearLabel + " Council Spending per Service Area " + yearLabel)
        plt.xlabel("Months")
        plt.ylabel("Spending £'s")

        # Save current figure for file creation later
        savedPlot = plt.gcf()

        # Show plotted graph
        plt.show()

        # Save plotted graph for later use
        savedPlot.savefig('graphs/standard/' + monthOrYearLabel + '_LCCSpending_' + yearLabel + '_LineGraph.png')

    except Exception as e:
        print("Error: Graph Plotting Line failed.\n", e)
        sys.exit()
