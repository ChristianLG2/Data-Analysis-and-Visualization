#%%
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import mpld3 
import os

#%%
# Load the data from the CSV file
data = pd.read_csv('life-expectancy.csv')

# Plot the life expectancy over time for a specific country
countries = ['United States', 'Mexico', 'China']
subset = data[data['Entity'].isin(countries)]

# Set up the plot
fig, ax = plt.subplots()

# Plot the data for the United States and Mexico using different colors
for country in countries:
    country_subset = subset[subset['Entity'] == country]
    ax.plot(country_subset['Year'], country_subset['Life expectancy (years)'], label=country)

# Add labels and legend to the plot
ax.set_xlabel('Year')
ax.set_ylabel('Life Expectancy')
ax.set_title('Life Expectancy over Time for the United States and Mexico')
ax.legend()

# Show the plot
plt.show()

#%%
# Convert the plot to an interactive HTML visualization
html = mpld3.fig_to_html(plt.gcf())

# Save the HTML visualization to a file
with open('life-expectancy.html', 'w') as f:
    f.write(html)
# %%
print(os.getcwd())
# %%
# Convert the plot to an interactive HTML visualization
html = mpld3.fig_to_html(fig)

# Save the HTML visualization to a file
with open('life-expectancy.html', 'w') as f:
    f.write(html)
# %%
