# Description: This file contains the dictionary that will be used in the main file.
languages = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5
}
import matplotlib.pyplot as plt # Importing the matplotlib library
import numpy as np              # Importing the numpy library
# Creating a bar chart
x = np.array(['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript'])
y = np.array([62.3, 52.9, 51, 51, 38.5])
plt.bar(x, y)
plt.show()          # Displaying the bar chart
#Close the bar image to continue
# Requested language 
requested_language = 'JavaScript'# Change this to the language you want to check
if requested_language in languages:
    print(f"{requested_language}: {languages[requested_language]}%")# If the language is in the dataset, print the percentage
else:
    print("Language not in dataset")# If the language is not in the dataset, print this message