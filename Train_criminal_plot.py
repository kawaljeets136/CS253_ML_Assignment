import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv('train.csv')

# Step 2: Filter out rows where the 'Criminal Case' column is greater than 5
filtered_df = df[df['Criminal Case'] > 5]

# Step 3: Calculate the percentage distribution of parties
party_distribution = filtered_df['Party'].value_counts(normalize=True) * 100

# Step 4: Plot a pie chart to visualize the distribution
plt.figure(figsize=(10, 8))

# Define colors for the pie chart
colors = plt.cm.Set3.colors[:len(party_distribution)]

# Explode some slices for emphasis
explode = [0.1 if i == party_distribution.idxmax() else 0 for i in party_distribution.index]

# Plot the pie chart with shadow effect and explode slices
plt.pie(party_distribution, labels=party_distribution.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True, textprops={'fontsize': 12})
plt.title('Percentage Distribution of Parties with Criminal Cases > 5 (train.csv)', fontsize=16)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.show()
