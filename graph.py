import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# Line Graph: Temperature Trend Over 10 Days
# ------------------------------------------

# Generate random data for the line graph
line_data = {
    'Day': range(1, 11),  # Days 1 to 10
    'Temperature (°C)': np.random.randint(15, 35, 10)  # Random temperatures between 15°C and 35°C
}

# Convert the data to a Pandas DataFrame
df_line = pd.DataFrame(line_data)

# Plot the line graph
plt.figure(figsize=(8, 5))
plt.plot(df_line['Day'], df_line['Temperature (°C)'], marker='o', color='blue', linestyle='-', label='Temperature')

# Add labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trend Over 10 Days')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Show the graph
plt.show()

# ------------------------------------------
# Bar Graph: Random Data for Categories
# ------------------------------------------

# Generate random data for the bar graph
bar_data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],  # Categories
    'Values': np.random.randint(10, 100, 5)  # Random values between 10 and 100
}

# Convert the data to a Pandas DataFrame
df_bar = pd.DataFrame(bar_data)

# Plot the bar graph
plt.figure(figsize=(8, 5))
plt.bar(df_bar['Category'], df_bar['Values'], color='darkblue', edgecolor='black')

# Add labels, title, and grid
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Random Data: Bar Graph')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the graph
plt.show()

# ------------------------------------------
# Histogram: Distribution of Random Scores
# ------------------------------------------

# Generate random data for the histogram
hist_data = {
    'Scores': np.random.randint(50, 100, 100)  # 100 random scores between 50 and 100
}

# Convert the data to a Pandas DataFrame
df_hist = pd.DataFrame(hist_data)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.hist(df_hist['Scores'], bins=10, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.title('Histogram: Distribution of Scores')

# Show the plot
plt.show()
