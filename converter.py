import pandas as pd

# Replace with your actual file path
parquet_file = "ad2.parquet"
csv_file = "Set1_converted.csv"

# Load the parquet file
df = pd.read_parquet(parquet_file)
# Check its content
print("DataFrame shape:", df.shape)
print("Index sample:", df.index[:5])
print("Columns sample:", df.columns[:5])


# Preview the first few rows
print(df.head())

# Flatten the MultiIndex columns using underscore separator
df_flat = df.copy()
df_flat.columns = ['_'.join(col).strip() for col in df_flat.columns.to_flat_index()]

# Save full DataFrame to CSV
# df_flat.to_csv("Set1_full.csv")
# print("Full data exported to Set1_full.csv")

# Optional: Flatten multi-index columns (for easier CSV writing)
# if isinstance(df.columns, pd.MultiIndex):
#     df.columns = ['_'.join(col).strip() for col in df.columns.values]

# Save to CSV
# df.to_csv(csv_file)

# Select a field you want to see
key_fields = ['ltp']
subset_cols = [col for col in df.columns if col[0] in key_fields][:100]  # pick only first 100 to keep size manageable

# Subset the DataFrame
df_subset = df[subset_cols].copy()
df_subset.columns = ['_'.join(col) for col in df_subset.columns]

# Export to CSV
df_subset.to_csv("Set1_subset.csv")
print("Subset exported to Set1_subset.csv")

print(f"Converted '{parquet_file}' to '{csv_file}' successfully.")
