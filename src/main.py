from data_preparation import load_stock_data
from indicators import add_technical_indicators
from visualization import plot_indicators

# Load and prepare data
df = load_stock_data('data/raw/stock_data.csv')

# Add indicators
df = add_technical_indicators(df)

# Save processed data
df.to_csv('data/processed/processed_data.csv')

# Visualize
plot_indicators(df)