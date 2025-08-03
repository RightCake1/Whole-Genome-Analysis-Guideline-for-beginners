import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
from collections import Counter

# Load your long-format AAI file and pivot to matrix
df_long = pd.read_csv("aai_long_format.tsv", sep='\t')
df_matrix = df_long.pivot(index='query', columns='target', values='aai').fillna(100)
df_sym = (df_matrix + df_matrix.T) / 2  # Make symmetric

labels = df_sym.index.tolist()

# Distance matrix: 100 - AAI
dist_matrix = 100 - df_sym
condensed_dist = squareform(dist_matrix.values)

# Linkage clustering
Z = linkage(condensed_dist, method='average')

# Species-specific color assignment (adapt these species names/colors as needed)
species_colors = {
    "Klebsiella_oxytoca": "#ffa401",         # Orange
    "Klebsiella_quasipneumoniae": "#a638cf", # Purple
    "Klebsiella_variicola": "#f11100",       # Red
    "Klebsiella_pneumoniae": "#0000ff"       # Blue
}

def get_species_color(label):
    for species, color in species_colors.items():
        if species in label:
            return color
    return "#000000"  # Default black if no match

def get_descendant_leaves(Z, node_id, n_leaves):
    """Recursively get all leaf indices under a given node."""
    if node_id < n_leaves:
        return [node_id]
    else:
        left = int(Z[node_id - n_leaves, 0])
        right = int(Z[node_id - n_leaves, 1])
        return get_descendant_leaves(Z, left, n_leaves) + get_descendant_leaves(Z, right, n_leaves)

def branch_color_func(node_id):
    """Color each branch by the dominant species among its leaves."""
    leaf_ids = get_descendant_leaves(Z, node_id, len(labels))
    leaf_labels = [labels[i] for i in leaf_ids]
    color_counts = Counter(get_species_color(label) for label in leaf_labels)
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color

# Plot dendrogram with left orientation and custom colors
plt.figure(figsize=(18, 12))
dendrogram(
    Z,
    labels=labels,
    leaf_rotation=0,
    orientation='left',
    distance_sort='descending',
    show_leaf_counts=False,
    link_color_func=branch_color_func,
    color_threshold=0,
    above_threshold_color='black'
)
plt.title('AAI-based Hierarchical Tree', fontsize=14)
plt.xlabel('Distance (100 - AAI %)')
plt.tight_layout()
plt.savefig('aai_colored_phylo_tree.svg', dpi=1000)
plt.show()