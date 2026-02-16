import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#csv filepath
data_path = "C:\\Users\\M\\Documents\\.Data Analytics\\Week 8\\Day 1\\Interim Project\\ipvis\\rby.csv" 

#import csv as pandas dataframe
rby = pd.read_csv(data_path)
#test print
print(rby)
#divider for visual clarity
print("***************************")
#print correlation values
correlation = rby.corr()
print(correlation)

#correlation value as variable for label
relevant_corr = correlation.iloc[1,2]

#create scatterplot / line plot
fig, ax = plt.subplots()
ax.set_facecolor("#2E4352") 
#plt.scatter(rby['years_trading'], rby['total_revenue_for_year'],marker='x',s=200,color="orange")    #comment out for line plot
plt.plot(rby['years_trading'], rby['total_revenue_for_year'],linewidth=5)                            #comment out for scatter plot
plt.title("Years Trading vs Total Revenue Generated (per year)",fontsize=24, pad=20)

#labels size and padding
plt.xlabel('Years Trading',fontsize=20,labelpad=15)
plt.ylabel('Total Revenue ($)',fontsize=20,labelpad=25)
#remove scientific notation
plt.ticklabel_format( axis='both', style='plain')
#tick label size
ax.set_xticklabels(ax.get_xticklabels(), fontsize=20)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=14)
#tick mark size
plt.tick_params(axis='x', length=14, width=2)  
plt.tick_params(axis='y', length=14, width=2)
plt.tick_params(which='minor', axis='x', length=7, width=1)
#add commas as thousands separators
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])  
#add minor ticks to better indicate years
plt.gca().xaxis.set_minor_locator(MultipleLocator(1))
#set grid lines
plt.grid(which='major', color='white', linestyle='-', linewidth=0.5)
plt.grid(which='minor', color='white', linestyle='--', linewidth=0.3)

#create scatterpolt trendline
trendline = np.poly1d(
    np.polyfit(rby['years_trading'], rby['total_revenue_for_year'], 1)
)  

# Plot the trendline
plt.plot(
    rby['years_trading'], 
    trendline(rby['years_trading']),  
    linestyle='--',
    linewidth=3,
    color='green'
)

 
#dynamically display correlation value on scatter
plt.text(
    0.78, 0.95,
     f"Correlation: {relevant_corr:.2f}", #fstring required
    color="#BAEEF0",
    fontweight='bold', 
    fontsize=20,
    transform=ax.transAxes
)


plt.show()

