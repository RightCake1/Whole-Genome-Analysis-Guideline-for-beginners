import pandas as pd

# Load your original TSV file
# CHANGE THIS: set the correct input file path/name
df = pd.read_csv("aai_results.tsv", sep='\t')

# Function to extract genome name from path
def extract_name(path):
    filename = path.split('/')[-1]  # get last part after '/'
    name = filename.replace('.fasta', '')  # remove file extension
    return name

# Create new columns with extracted genome names
# Assumes original file has columns "Label 1" and "Label 2"
df['query'] = df['Label 1'].apply(extract_name)
df['target'] = df['Label 2'].apply(extract_name)

# Select only required columns for the heatmap script
df_long = df[['query', 'target', 'AAI']].copy()

# Rename 'AAI' to lowercase 'aai' to match your script's expected column name
df_long.rename(columns={'AAI': 'aai'}, inplace=True)

# Save the reformatted dataframe to a new TSV file
# CHANGE THIS: output filename if needed
df_long.to_csv("aai_long_format.tsv", sep='\t', index=False)

print("✅ Converted AAI results saved to aai_long_format.tsv")
