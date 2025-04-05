import pandas as pd

# Load the scraped data from the Excel file
df = pd.read_excel('amazon_soft_toys_data.xlsx')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove any non-numeric characters (like ₹) from the 'Price' column
df['Price'] = df['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)

# Convert 'Reviews' and 'Rating' columns to numeric (force errors to NaN and then fill or drop)
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Handle missing values by dropping rows with missing critical data (Price, Reviews, Rating)
df.dropna(subset=['Price', 'Reviews', 'Rating'], inplace=True)

# Save the cleaned data to a new Excel file
df.to_excel('amazon_soft_toys_cleaned_data.xlsx', index=False)

print("Data cleaning complete. Saved cleaned data to 'amazon_soft_toys_cleaned_data.xlsx'.")
