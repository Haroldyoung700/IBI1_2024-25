#Create a dictionary with the UK countries and their population in millions
uk_data = {
    'England': 57.11,
    'Scotland': 5.45,
    'Wales': 3.13,
    'N.Ireland': 1.91
} 
#Create a dictionary with the Chinese provinces and their population in millions
china_data = {
    'Jiangsu': 85.15,
    'Zhejiang': 65.77,
    'Anhui': 61.27,
    'Jiangxi': 45.28,
    'Fujian': 41.88
} 
#Sort the dictionaries in descending order
sorted_uk = sorted(uk_data.items(), key=lambda x: x[1], reverse=True)
sorted_china = sorted(china_data.items(), key=lambda x: x[1], reverse=True) #Sort the dictionaries in descending order
#Print the sorted dictionaries
print("UK Countries (descending):")
print([f"{k}: {v}M" for k, v in sorted_uk])    #Print the sorted dictionaries of UK
print("\nChina Provinces (descending):")
print([f"{k}: {v}M" for k, v in sorted_china]) #Print the sorted dictionaries of China
 #Import the matplotlib library
import matplotlib.pyplot as plt
import numpy as np 
#Create a pie chart with the UK countries and their population
y = np.array([57.11, 5.45, 3.13, 1.91])

plt.pie(y,
        labels=['England', 'Scotland', 'Wales', 'N.Ireland'], 
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], 
        explode=(0.2, 0, 0, 0), 
        autopct='%.2f%%', 
       )#Create a pie chart with the UK countries and their population
#The explode parameter is used to separate England from the rest
plt.title("uk_population")
plt.show() #Display the pie chart  
#Close the pie chart to continue

y = np.array([85.15, 65.77, 61.27, 45.28, 41.88])

plt.pie(y,
        labels=['Jiangsu', 'Zhejiang', 'Anhui', 'Jiangxi', 'Fujian'], 
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9", "#c9a564"], 
        explode=(0, 0.2, 0, 0, 0), 
        autopct='%.2f%%', 
       )#Create a pie chart with the Chinese provinces and their population
#The explode parameter is used to separate the Zhejiang province from the rest
plt.title("eastern_china_population")
plt.show() #Display the pie chart
#Close the pie chart to finish the program