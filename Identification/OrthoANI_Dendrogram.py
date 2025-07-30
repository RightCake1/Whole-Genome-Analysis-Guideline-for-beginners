#!/usr/bin/env python3

import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import os
from collections import Counter

# -------------------------------
# PATH SETTINGS
# -------------------------------
base_dir = "/home/rightcake/KPV/OrthoANI_TEST"
ani_file = os.path.join(base_dir, "ani_matrix.tsv")
fig_output = os.path.join(base_dir, "colored_dendrogram.png")

# -------------------------------
# Step 1: Load ANI matrix
# -------------------------------
ani_matrix = pd.read_csv(ani_file, sep="\t", index_col=0)
labels = ani_matrix.index.tolist()

# Convert ANI to distance
distance_matrix = 100 - ani_matrix.astype(float)
condensed_dist = squareform(distance_matrix.values, checks=False)

# -------------------------------
# Step 2: Perform Clustering
# -------------------------------
linked = linkage(condensed_dist, method="average")

# --- Stretch horizontal distances by scale factor ---
scale_factor = 5.0  # Increase to stretch branches more horizontally
linked[:, 2] = linked[:, 2] * scale_factor

# -------------------------------
# Step 3: Species color mapping
# -------------------------------
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
    return "#000000"  # default black

# Assign leaf colors
label_colors = {label: get_species_color(label) for label in labels}

# -------------------------------
# Step 4: Link color function for branches
# -------------------------------
def get_cluster_descendant_labels(linkage_matrix, node_id, n_leaves):
    if node_id < n_leaves:
        return [node_id]
    else:
        left = int(linkage_matrix[node_id - n_leaves, 0])
        right = int(linkage_matrix[node_id - n_leaves, 1])
        return get_cluster_descendant_labels(linkage_matrix, left, n_leaves) + \
               get_cluster_descendant_labels(linkage_matrix, right, n_leaves)

def branch_color_func(node_id):
    leaf_ids = get_cluster_descendant_labels(linked, node_id, len(labels))
    leaf_labels = [labels[i] for i in leaf_ids]
    color_counts = Counter(get_species_color(label) for label in leaf_labels)
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color

# -------------------------------
# Step 5: Plot with better spacing and dpi=600
# -------------------------------
plt.figure(figsize=(18, max(12, len(labels) * 0.35)))  # wider and taller figure

dendrogram(
    linked,
    labels=labels,
    orientation='left',
    leaf_font_size=10,
    leaf_rotation=0,            # horizontal labels
    link_color_func=branch_color_func,
    color_threshold=0,          # disables default cutoff coloring
    above_threshold_color='black',
    show_leaf_counts=False,
)

plt.title("Hierarchical Clustering Tree Based on OrthoANI Similarity", fontsize=16)
plt.xlabel("Distance (100 - ANI) [Scaled]")
plt.tight_layout()

plt.savefig(fig_output, dpi=600, bbox_inches='tight')  # high DPI + tight bounding box
plt.show()

print(f"✅ Colored dendrogram saved to: {fig_output}")


