import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/harold_young/Documents/GitHub/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


# Task1: show the year for the first 10 rows
years_first_10 = dalys_data.iloc[0:10, 2]  # column loc matching the year
print("\n the year for the first 10 rows：\n", years_first_10)
# gather the 10th year with DALYs data recorded in Afghanistan
afghan_data = dalys_data[dalys_data['Entity'] == 'Afghanistan'].reset_index(drop=True)
tenth_year_afghan = afghan_data.loc[9, 'Year'] 
print(f"\n the 10th year with DALYs data recorded in Afghanistan：{tenth_year_afghan}")
print("Data column name：", dalys_data.columns.tolist())  
# Filter the data for 1990
mask_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[mask_1990, ['Entity', 'DALYs']]  
print("\n1990 data：\n", dalys_1990.head())


# Task2: Calculate the mean of uk and france and conduct the comparison 
# Calculate the mean for uk and france
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
france_data = dalys_data[dalys_data['Entity'] == 'France']
mean_uk = uk_data['DALYs'].mean()          
mean_france = france_data['DALYs'].mean()  
print(f"\nUK mean DALYs：{mean_uk:.2f}")
print(f"France mean DALYs：{mean_france:.2f}")
print("UK mean" + (" higher than " if mean_uk > mean_france else " lower than ") + "France")


# Task3: print a plot describing the trend of uk data
# Plot the figure
plt.figure(figsize=(10,6))
plt.plot(uk_data['Year'], uk_data['DALYs'], label='United Kingdom')  
plt.title('DALYs Over Time in the UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.legend()
plt.tight_layout()   
plt.show()           
plt.savefig('uk_dalys_trend.png', dpi=300)


# Task4: Self-designed question: Compare the mean DALY data of different regions in terms of economic development
# define the region by representative country
def assign_region(entity):
    if entity in ['Afghanistan', 'India', 'Pakistan']:
        return 'South Asia'
    elif entity in ['France', 'Germany', 'United Kingdom']:
        return 'Europe'
    else:
        return 'Other'
dalys_data['Region'] = dalys_data['Entity'].apply(assign_region)
asia_data = dalys_data[dalys_data['Region'] == 'South Asia']
europe_data = dalys_data[dalys_data['Region'] == 'Europe']
    # Calculate the mean data
mean_asia = asia_data['DALYs'].mean()
mean_europe = europe_data['DALYs'].mean()
# output the results and conduct the comparison
print(f"\nSouthern Asia mean DALYs：{mean_asia:.2f}")
print(f"Western Europe mean DALYs：{mean_europe:.2f}")
print("Conclusion: The mean DALYs in South Asia is " + ("higher than" if mean_asia > mean_europe else "lower than") + " Europe.")