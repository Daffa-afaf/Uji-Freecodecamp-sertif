import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend line to year 2050
    years_extended = pd.Series(range(1880, 2051))
    line1 = intercept + slope * years_extended
    ax.plot(years_extended, line1, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (using data from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Extend second line from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    line2 = intercept2 + slope2 * years_recent
    ax.plot(years_recent, line2, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()