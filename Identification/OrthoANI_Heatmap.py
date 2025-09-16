import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load ANI matrix
# CHANGE THIS: provide your own input file path/name
df = pd.read_csv('ani_matrix.tsv', sep='\t', index_col=0)
labels = df.index.tolist()

# Optionally sort labels by species to group similar species together
species_order = [
    "Klebsiella_oxytoca",
    "Klebsiella_quasipneumoniae",
    "Klebsiella_variicola",
    "Klebsiella_pneumoniae"
]

def get_species(label):
    for sp in species_order:
        if sp in label:
            return sp
    return None

# Sort labels by species, then alphabetically within species
sorted_labels = sorted(labels, key=lambda x: (species_order.index(get_species(x)) if get_species(x) else 999, x))
df_sorted = df.loc[sorted_labels, sorted_labels]

# Color map for species
species_colors = {
    "Klebsiella_oxytoca": "#ffa401",         # Orange
    "Klebsiella_quasipneumoniae": "#a638cf", # Purple
    "Klebsiella_variicola": "#f11100",       # Red
    "Klebsiella_pneumoniae": "#0000ff"       # Blue
}

def get_label_color(label):
    sp = get_species(label)
    return species_colors.get(sp, "#000000")  # black if unknown

# Plot heatmap
plt.figure(figsize=(18, 18))
im = plt.imshow(df_sorted, cmap='coolwarm', vmin=95, vmax=100)

ax = plt.gca()
ax.set_xticks(np.arange(len(sorted_labels)))
ax.set_yticks(np.arange(len(sorted_labels)))

# Set tick labels
ax.set_xticklabels(sorted_labels, rotation=90, fontsize=7)
ax.set_yticklabels(sorted_labels, fontsize=7)

# Color the tick labels by species
for tick_label in ax.get_xticklabels():
    tick_label.set_color(get_label_color(tick_label.get_text()))
for tick_label in ax.get_yticklabels():
    tick_label.set_color(get_label_color(tick_label.get_text()))

plt.title("ANI Heatmap (Cutoff = 95%)", fontsize=14)

# Add colorbar
cbar = plt.colorbar(im, fraction=0.046, pad=0.04)
cbar.set_label('ANI %')

plt.tight_layout()
# CHANGE THIS: output filename if needed
plt.savefig("orthoani_heatmap_only_95cutoff.png", dpi=300)
plt.savefig("orthoani_heatmap_only_95cutoff.svg", dpi=300)
plt.show()


