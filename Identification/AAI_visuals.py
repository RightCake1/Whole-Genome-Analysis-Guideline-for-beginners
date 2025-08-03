import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load long format AAI data
    df_long = pd.read_csv("aai_long_format.tsv", sep='\t')

    # Pivot to square matrix
    df_matrix = df_long.pivot(index='query', columns='target', values='aai')
    df_matrix = df_matrix.fillna(100.0)  # Fill missing (diagonal)

    # Make symmetric by averaging upper and lower triangles
    df_sym = (df_matrix + df_matrix.T) / 2


    # Distance matrix (100 - AAI)
    dist_matrix = 100 - df_sym

    # Condensed distance for clustering
    dist_condensed = squareform(dist_matrix)

    # Linkage
    linkage_matrix = linkage(dist_condensed, method='average')

    # 1) Dendrogram only
    plt.figure(figsize=(10, 6))
    dendrogram(linkage_matrix, labels=df_sym.index.tolist(), leaf_rotation=90)
    plt.title("Hierarchical Clustering based on AAI")
    plt.tight_layout()
    plt.savefig("aai_dendrogram.png", dpi=300)
    plt.show()

    # 2) Heatmap only (no dendrogram)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_sym, cmap="viridis", square=True, cbar_kws={'label': 'AAI (%)'})
    plt.title("AAI Heatmap")
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("aai_heatmap.png", dpi=300)
    plt.show()

    # 3) Heatmap + dendrogram combined
    sns.set(font_scale=0.7)
    g = sns.clustermap(df_sym,
                       row_linkage=linkage_matrix,
                       col_linkage=linkage_matrix,
                       cmap="viridis",
                       figsize=(12, 12),
                       cbar_kws={'label': 'AAI (%)'})

    plt.title("Hierarchical Clustering Tree based on AAI", y=1.05)
    plt.savefig("aai_heatmap_dendrogram.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()


