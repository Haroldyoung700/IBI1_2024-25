# Description: This file contains the dictionary that will be used in the main file.
languages = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5
}  
print("Languages (descending):")
print([f"{k}: {v}%" for k, v in sorted(languages.items(), key=lambda x: x[1], reverse=True)]) # Print the sorted dictionary of languages

import matplotlib.pyplot as plt # Importing the matplotlib library
# Creating a bar chart
x = languages.keys()
y = languages.values()
plt.bar(x, y)
plt.xlabel("Programming languages")
plt.ylabel("Popularity(%)") 
plt.title("Study of programming language popularity")
plt.show()          # Displaying the bar chart
#Close the bar image to continue
# Requested language 
requested_language = 'JavaScript'# Change this to the language you want to check
if requested_language in languages:
    print(f"{requested_language}: {languages[requested_language]}%")# If the language is in the dataset, print the percentage
else:
    print("Language not in dataset")# If the language is not in the dataset, print this message