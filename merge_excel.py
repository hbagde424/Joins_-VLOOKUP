import pandas as pd

# File paths
file1 = "C:/Users/devel/Downloads/New folder (2)/merged_output.xlsx"
file2 = "C:/Users/devel/Downloads/New folder (2)/assemblyexcel.xlsx"
output_file = "C:/Users/devel/Downloads/New folder (2)/allout.xlsx"

# Read the Excel files into DataFrames
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Perform a left join to mimic VLOOKUP functionality
merged_df = pd.merge(df1, df2, on='AC_NO', how='left')

# Write the merged DataFrame to a new Excel file
merged_df.to_excel(output_file, index=False)

print(f"Merged data with VLOOKUP-like functionality has been saved to {output_file}")
