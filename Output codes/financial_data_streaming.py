# Import necessary libraries for data visualization and manipulation
import matplotlib.pyplot as plt  # For creating visual plots
import seaborn as sns          # For statistical data visualization
import pandas as pd            # For data manipulation and analysis

# Load the financial dataset from a CSV file into a pandas DataFrame
df = pd.read_csv("financial_data.csv")

# Convert the timestamp column into a datetime format for easier manipulation and better visualization
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')

# Visualization 1: Plot the distribution of prices
plt.figure(figsize=(10, 6))  # Set the figure size for the plot
sns.histplot(df['price'], bins=20, kde=True, color='blue')  # Create a histogram with KDE (Kernel Density Estimate) curve
plt.title('Distribution of Prices', fontsize=16)  # Set the title for the plot
plt.xlabel('Price', fontsize=12)  # Label the x-axis
plt.ylabel('Frequency', fontsize=12)  # Label the y-axis
plt.show()  # Display the plot

# Visualization 2: Show the top 10 symbols with the highest prices
top_symbols = df.nlargest(10, 'price')  # Get the top 10 rows sorted by the 'price' column in descending order
plt.figure(figsize=(10, 6))  # Set the figure size for the plot
sns.barplot(x='price', y='symbol', data=top_symbols, palette='viridis')  # Create a bar plot for the top symbols
plt.title('Top 10 Symbols by Price', fontsize=16)  # Set the title for the plot
plt.xlabel('Price', fontsize=12)  # Label the x-axis
plt.ylabel('Symbol', fontsize=12)  # Label the y-axis
plt.show()  # Display the plot

# Visualization 3: Show the price trend over time for a specific symbol
symbol_to_plot = "NTRNTRY"  # Set the symbol of interest for plotting the price trend (you can change this symbol)
symbol_data = df[df['symbol'] == symbol_to_plot]  # Filter the data for the selected symbol
plt.figure(figsize=(10, 6))  # Set the figure size for the plot
plt.plot(symbol_data['datetime'], symbol_data['price'], marker='o', linestyle='-', color='red')  # Plot the time-series data for the symbol
plt.title(f'Price Trend for {symbol_to_plot}', fontsize=16)  # Set the title for the plot
plt.xlabel('Time', fontsize=12)  # Label the x-axis
plt.ylabel('Price', fontsize=12)  # Label the y-axis
plt.grid(True)  # Add grid lines to the plot for better readability
plt.show()  # Display the plot

# Visualization 4: Boxplot to visualize the distribution of prices for each symbol
plt.figure(figsize=(12, 8))  # Set the figure size for the plot
sns.boxplot(x='price', y='symbol', data=df, palette='coolwarm')  # Create a boxplot to show the distribution of prices by symbol
plt.title('Price Distribution by Symbol', fontsize=16)  # Set the title for the plot
plt.xlabel('Price', fontsize=12)  # Label the x-axis
plt.ylabel('Symbol', fontsize=12)  # Label the y-axis
plt.show()  # Display the plot

# New Visualization 5: Show the time-series price trends for multiple top symbols
# Select the top 5 symbols based on the average price for plotting
top_symbols_by_avg_price = df.groupby('symbol')['price'].mean().nlargest(5).index  # Find the top 5 symbols by average price
filtered_data = df[df['symbol'].isin(top_symbols_by_avg_price)]  # Filter the dataset to include only the top symbols

plt.figure(figsize=(12, 8))  # Set the figure size for the plot
# Loop through each of the top 5 symbols and plot their price trends over time
for symbol in top_symbols_by_avg_price:
    symbol_data = filtered_data[filtered_data['symbol'] == symbol]  # Filter data for the current symbol
    plt.plot(symbol_data['datetime'], symbol_data['price'], label=symbol, marker='o', linestyle='-')  # Plot the time-series data for the symbol

plt.title('Price Trends for Top 5 Symbols', fontsize=16)  # Set the title for the plot
plt.xlabel('Time', fontsize=12)  # Label the x-axis
plt.ylabel('Price', fontsize=12)  # Label the y-axis
plt.legend(title="Symbols")  # Add a legend to distinguish the symbols
plt.grid(True)  # Add grid lines for better readability
plt.show()  # Display the plot
