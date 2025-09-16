import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the FastANI .txt file
# CHANGE THIS: provide your own FastANI output file path/name
out_file = '/media/rightcake/Galib_Stuff/PKV_project/ANI_Stuff/All_81Genomes/81Genome_fastani.txt'
data = pd.read_csv(out_file, sep='\t', header=None)

# Assign column names based on the file format
data.columns = ['Query', 'Reference', 'ANI', 'Alignment_Fraction', 'Bidirectional_Fragments']

# Load the query and reference lists
# CHANGE THESE if your file names/paths differ 
with open('/media/rightcake/Galib_Stuff/PKV_project/ANI_Stuff/All_81Genomes/query_list.txt', 'r') as f:
    query_list = [line.strip() for line in f]

with open('/media/rightcake/Galib_Stuff/PKV_project/ANI_Stuff/All_81Genomes/reference_list.txt', 'r') as f:
    ref_list = [line.strip() for line in f]

# Reshape the pairwise comparisons into a matrix
matrix = data.pivot(index='Query', columns='Reference', values='ANI')

# Fill missing values with 0 (or another appropriate value)
matrix = matrix.fillna(0)

# Perform hierarchical clustering
Z = linkage(matrix, method='average')

# Create a dendrogram
plt.figure(figsize=(15, 10))
dendrogram(Z, labels=matrix.index, leaf_rotation=90, leaf_font_size=8)

# Add labels and title
plt.xlabel('Genomes')
plt.ylabel('Distance')
plt.title('Hierarchical Clustering Dendrogram (ANI Values)')

# Adjust layout and save the plot
plt.tight_layout()
# CHANGE THIS: output filename if needed
plt.savefig('dendrogram.png', dpi=300, bbox_inches='tight')
print("Dendrogram saved to 'dendrogram.png'")
