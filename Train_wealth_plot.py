import pandas as pd
import matplotlib.pyplot as plt

# Function to convert amount strings to numeric
def convert_to_numeric(amount):
    if isinstance(amount, str):
        amount = amount.replace(' Crore+', 'e7').replace(' Lac+', 'e5').replace(' Thou+', 'e3')
        return pd.to_numeric(amount, errors='coerce')
    return amount

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('train.csv')

# Convert 'Total Assets' and 'Liabilities' to numeric
data['Total Assets'] = data['Total Assets'].apply(convert_to_numeric)
data['Liabilities'] = data['Liabilities'].apply(convert_to_numeric)

# Step 3: Calculate the median wealth
median_wealth = data['Total Assets'].median()

# Step 4: Filter out rows where 'Total Assets' is greater than the median wealth
filtered_data = data[data['Total Assets'] > median_wealth]

# Step 5: Calculate the percentage distribution of parties
party_distribution = filtered_data['Party'].value_counts(normalize=True) * 100

# Step 6: Plot a bar chart to visualize the distribution
plt.figure(figsize=(12, 8))

# Create a horizontal bar chart with a gradient color scheme
colors = plt.cm.tab10.colors
party_distribution.sort_values().plot(kind='barh', color=colors[::-1], alpha=0.8)

plt.title('Percentage Distribution of Parties with Total Assets > Median Wealth (train.csv)', fontsize=16)
plt.xlabel('Percentage', fontsize=12)
plt.ylabel('Party', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)  # Add horizontal grid lines with lower opacity
plt.xticks(fontsize=10)  # Adjust x-axis tick font size
plt.yticks(fontsize=10)  # Adjust y-axis tick font size
plt.gca().invert_yaxis()  # Invert y-axis to have the highest percentage at the top

# Add data labels inside the bars
for i, value in enumerate(party_distribution.sort_values()):
    plt.text(value + 1, i, f'{value:.1f}%', va='center', fontsize=10)

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
