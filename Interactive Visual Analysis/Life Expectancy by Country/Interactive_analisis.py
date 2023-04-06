# Christian Lira - Winter 2023
# This code asks the user to enter a country name, and loops until the user types 'done'. For each country entered, it checks if it exists in the dataset, subsets the data, and adds a subplot for the country to the figure. Once all countries are added, it adds axis labels and a legend to the figure, converts it to an interactive HTML visualization, and saves it to a file. Finally, it shows the plot.

#Run Cell in Jupiter Notes to start the interactive analysis

#%%
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import mpld3
import os

# Load the data from the CSV file
data = pd.read_csv('life_expectancy.csv', encoding='ISO-8859-1')

# Create a figure to hold the subplots
fig, ax = plt.subplots()

# Loop to ask for countries until the user stops adding
while True:
    # Ask for a country
    country = input("Enter a country name (or 'done' to finish): ")
    
    # Convert the input to lowercase
    country = country.lower()
    
    # Check if the user is done adding countries
    if country == 'done':
        break
    
    # Check if the country exists in the dataset
    if country not in data['Entity'].str.lower().unique():
        print(f"{country} is not in the dataset.")
        continue
    
    # Subset the data for the country
    subset = data[data['Entity'].str.lower() == country]
    
    # Add the subplot for the country to the figure
    ax.plot(subset['Year'], subset['Life expectancy (years)'], label=country.capitalize())
    
# Add axis labels and legend to the figure
ax.set_xlabel('Year')
ax.set_ylabel('Life Expectancy')
ax.set_title('Life Expectancy over Time')
ax.legend()

# Convert the plot to an interactive HTML visualization
html = mpld3.fig_to_html(fig)

# Save the HTML visualization to a file
with open('life-expectancy.html', 'w') as f:
    f.write(html)
    
# Show the plot
plt.show()

# Print the current working directory
print(os.getcwd())
# %%
