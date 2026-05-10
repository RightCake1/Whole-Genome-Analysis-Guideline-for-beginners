# Pangenome Analysis Guide Using Roary

## Introduction

Roary is a high-speed bacterial pangenome pipeline that can compute the pangenome of large datasets of bacterial isolates (1000s) within minutes. This guide covers installation, usage, and visualization of pangenome analyses.

---

## Installation and Setup

### Installing Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Create Conda Environment

```bash
# Create and activate environment
conda create -n pangenome
conda activate pangenome

# Install required packages
conda install -c bioconda roary
conda install -c bioconda fasttree
conda install -c conda-forge biopython
conda install -c conda-forge numpy
conda install -c conda-forge matplotlib
```

---

## Running Roary

### Step 1 — Annotate genomes with Prokka first to get `.gff` files

Please look at [How to run Prokka](../Annotations/Genome_Annotaions.md).
Move all ``.gff`` files in a separate folder for convenience.

### Step 2 — Run Roary

Basic run:

```bash
roary -f Roaryresults -p 6 -e -n -v --maft *.gff
```

More robust run (takes longer but more accurate):

```bash
roary -f Roaryresults -p 12 -e --mafft -i 95 -cd 99 -iv 1.5 -v *.gff
```

### Step 3 — Build phylogenetic tree with FastTree

```bash
FastTree -nt -gtr -gamma -boot 100 -spr 4 Roaryresult/core_gene_alignment.aln > Roaryresult/mytree.newick
```

### Step 4 — Generate visualizations

```bash
python Roary_Visualize.py --labels Roaryresult/mytree.newick Roaryresult/gene_presence_absence.csv
```

---

## Parameter Explanations

| Parameter | Description |
|-----------|-------------|
| `-f` | Output directory |
| `-e` | Create gene alignment files |
| `-n` | Fast core gene alignment |
| `-v` | Verbose output |
| `-p` | Number of threads |
| `-i` | Minimum percentage identity |
| `-cd` | Percentage of isolates for core definition |
| `--mafft` | Use MAFFT for alignment |

---

## Output Files

| File | Description |
|------|-------------|
| `gene_presence_absence.csv` | Main results table |
| `gene_presence_absence.Rtab` | Binary matrix of gene presence/absence |
| `core_gene_alignment.aln` | Core genes aligned |
| `pan_genome_reference.fa` | All genes in FASTA format |
| `clustered_proteins` | Clustered proteins |

---

## Visualization Script (Roary_Visualize.py)

This custom script generates multiple figures: a pangenome pie chart, a separate pangenome matrix, a separate cluster tree, a merged tree + matrix, and a length barchart.

Save the code below as `Roary_Visualize.py` in your working directory:

```python
#!/usr/bin/env python3

__author__ = "Marco Galardini (modified by ChatGPT)"
__version__ = '0.2.0-mod-clean'

import argparse
import matplotlib
matplotlib.use('Agg')  # use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
import pandas as pd
import numpy as np
from Bio import Phylo
from Bio.Phylo.BaseTree import Tree

def get_options():
    parser = argparse.ArgumentParser(description="Create Roary plots including phylogenetic tree, pangenome matrix, and clade-colored tree")
    parser.add_argument('tree', help='Newick Tree file')
    parser.add_argument('spreadsheet', help='Roary gene presence/absence spreadsheet')
    parser.add_argument('--labels', action='store_true', default=False, help='Show tip labels on tree')
    parser.add_argument('--format', choices=('png','tiff','pdf','svg'), default='png', help='Output format [Default: png]')
    parser.add_argument('-N', '--skipped-columns', type=int, default=14, help='Number of columns to skip in Roary CSV [Default: 14]')
    return parser.parse_args()

color_map = {
    "Klebsiella_oxytoca": "#ffa401",
    "Klebsiella_quasipneumoniae": "#a638cf",
    "Klebsiella_variicola": "#f11100",
    "Klebsiella_pneumoniae": "#0000ff"
}

def get_clade_color(name):
    if not name:
        return "#000000"
    for key in color_map:
        if key in name:
            return color_map[key]
    return "#000000"

def midpoint_root(tree: Tree):
    tree.root_at_midpoint()
    return tree

def set_uniform_branch_lengths(tree, length=1.0):
    for clade in tree.find_clades():
        clade.branch_length = length

def get_max_depth(tree):
    def max_depth_clade(clade, current_length):
        if clade.is_terminal():
            return current_length
        else:
            return max(max_depth_clade(child, current_length + (child.branch_length or 0)) for child in clade.clades)
    return max_depth_clade(tree.root, 0)

def extend_tips(tree, target_length):
    for clade in tree.find_clades():
        if clade.is_terminal():
            path = tree.get_path(clade)
            length_sum = sum((node.branch_length or 0) for node in path)
            extend_by = target_length - length_sum
            if extend_by > 0:
                clade.branch_length += extend_by

def colored_draw(tree, axes, show_labels=False):
    set_uniform_branch_lengths(tree, 1.0)
    max_depth = get_max_depth(tree)
    extend_tips(tree, max_depth)
    for clade in tree.find_clades():
        clade.color = get_clade_color(clade.name)
    Phylo.draw(
        tree,
        axes=axes,
        do_show=False,
        label_func=(lambda x: x.name) if show_labels else None,
        branch_labels=None,
        show_confidence=False,
    )
    axes.axis("off")

if __name__ == "__main__":
    options = get_options()

    try:
        t = Phylo.read(options.tree, 'newick')
    except Exception as e:
        print(f"Error reading tree file: {e}")
        exit(1)
    t = midpoint_root(t)

    roary = pd.read_csv(options.spreadsheet, low_memory=False)
    roary.set_index('Gene', inplace=True)
    roary.drop(roary.columns[:options.skipped_columns - 1], axis=1, inplace=True)
    roary.replace('.{2,100}', 1, regex=True, inplace=True)
    roary.replace(np.nan, 0, regex=True, inplace=True)

    roary_sorted = roary.loc[roary.sum(axis=1).sort_values(ascending=False).index]
    roary_sorted = roary_sorted[[x.name for x in t.get_terminals()]]

    # Tree only
    fig = plt.figure(figsize=(20, 25))
    ax = fig.add_subplot(1, 1, 1)
    colored_draw(t, ax, show_labels=options.labels)
    plt.savefig(f'colored_tree.{options.format}', dpi=100, bbox_inches='tight')
    plt.clf()

    # Matrix only
    fig = plt.figure(figsize=(25, 20))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(roary_sorted.T, cmap=plt.cm.Blues, vmin=0, vmax=1, aspect='auto')
    ax.set_title('Roary Pangenome Matrix')
    ax.set_yticks([])
    ax.set_xticks([])
    ax.axis('off')
    plt.savefig(f'roary_pangenome_matrix.{options.format}', dpi=100)
    plt.clf()

    # Combined tree + matrix
    fig = plt.figure(figsize=(45, 22))
    ax_tree = plt.subplot2grid((1,100), (0, 0), colspan=60)
    ax_matrix = plt.subplot2grid((1,100), (0, 60), colspan=40)
    colored_draw(t, ax_tree, show_labels=options.labels)
    ax_matrix.matshow(roary_sorted.T, cmap=plt.cm.Blues, vmin=0, vmax=1, aspect='auto')
    ax_matrix.set_xticks([])
    ax_matrix.set_yticks([])
    ax_matrix.axis('off')
    plt.savefig(f'roary_tree_matrix_combined.{options.format}', dpi=100, bbox_inches='tight')
    plt.clf()

    # Pangenome pie chart
    core     = roary[(roary.sum(axis=1) >= roary.shape[1]*0.99) & (roary.sum(axis=1) <= roary.shape[1])].shape[0]
    softcore = roary[(roary.sum(axis=1) >= roary.shape[1]*0.95) & (roary.sum(axis=1) <  roary.shape[1]*0.99)].shape[0]
    shell    = roary[(roary.sum(axis=1) >= roary.shape[1]*0.15) & (roary.sum(axis=1) <  roary.shape[1]*0.95)].shape[0]
    cloud    = roary[roary.sum(axis=1)  < roary.shape[1]*0.15].shape[0]

    total = roary.shape[0]
    def my_autopct(pct):
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)

    plt.figure(figsize=(10, 10))
    plt.pie(
        [core, softcore, shell, cloud],
        labels=[
            f'core ({core})',
            f'soft-core ({softcore})',
            f'shell ({shell})',
            f'cloud ({cloud})'
        ],
        explode=[0.1, 0.05, 0.02, 0],
        colors=[(0, 0, 1, float(x)/total) for x in (core, softcore, shell, cloud)],
        autopct=my_autopct
    )
    plt.savefig(f'pangenome_pie.{options.format}', dpi=1000)
```

> ⚠️ The `color_map` at the top of the script is set for Klebsiella species. If you're working with a different organism, update those species names and colors to match your dataset.

---

## Best Practices

- Use consistent annotation methods for all genomes
- Verify GFF3 format compliance before running Roary
- Adjust thread count (`-p`) based on your machine
- Monitor memory usage for large datasets

---

## Additional Resources

- [Roary GitHub](https://github.com/sanger-pathogens/Roary)
- [Roary Paper](https://academic.oup.com/bioinformatics/article/31/22/3691/240757)