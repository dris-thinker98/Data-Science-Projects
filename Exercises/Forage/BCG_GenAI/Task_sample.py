import pandas as pd

# Load the data from the Excel spreadsheet
file_path = 'path_to_your_excel_file.xlsx'
df = pd.read_excel(file_path)

# Calculate year-over-year growth rates for Total Revenue and Net Income
df['Revenue Growth (%)'] = df.groupby('Company Name')['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company Name')['Net Income'].pct_change() * 100

# Fill NA values that result from pct_change calculations with 0 or an appropriate value
df.fillna(0, inplace=True)

# Display the dataframe to verify the calculations
print(df)

# Optionally, you could summarize these findings for each company
summary = df.groupby('Company Name').agg({
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean'
}).reset_index()
