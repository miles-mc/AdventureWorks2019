import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

     
#csv filepath
data_path = "C:\\Users\\M\\Documents\\.Data Analytics\\Week 8\\Day 1\\Interim Project\\ipvis\\vStoreWithDemographics.csv" 

vswd = pd.read_csv(data_path)

print(vswd)


sns.set_theme(style = 'whitegrid')  
     
# #group revenue by quartile
# vswd['Revenue'] = pd.qcut(
#     vswd['AnnualRevenue'],
#     q=4,
#     labels=['Low', 'Medium', 'High'],
#     duplicates='drop'
# )

#sum total employees per store size (square feet)
totalemp = vswd.groupby(['SquareFeet','AnnualRevenue'])['NumberEmployees'].sum().reset_index()

#sort store sizes by total employees (descending)
size_total = totalemp.groupby('SquareFeet')['NumberEmployees'].sum()

#convert index to list 
size_total_list = size_total.index.tolist()

#SquareFeet to ordered category variable
totalemp['SquareFeet'] = pd.Categorical(totalemp['SquareFeet'], categories=size_total_list, ordered=True)

#remove stores with no revenue data, testing only. Don't use this.
#totalemp['SquareFeet'] = totalemp['SquareFeet'].cat.remove_unused_categories()  


#set colour palette
sns.set_palette("mako")

fig, ax = plt.subplots()
ax.set_facecolor("#113953")
bplot =sns.barplot(
    data=totalemp,
    x="SquareFeet",
    y="NumberEmployees",
    hue="AnnualRevenue",   #colour by revenue
    width=0.8,
    palette="colorblind",
    ci=None
)


#labels size and padding
plt.xlabel('Store Size (sq ft)',fontsize=24,labelpad=15)
plt.ylabel('Number of Employees',fontsize=24,labelpad=25)
plt.title("Impact of Store size and Employee Count on Revenue",fontsize=28, pad=20)
plt.legend(title='Annual Revenue ($)',title_fontsize=24, loc='upper left', fontsize=22)
#tick label size
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=18)
#tick mark size
plt.tick_params(axis='x', length=8, width=2)  
plt.tick_params(axis='y', length=8, width=2)  


# show the graph
plt.show()