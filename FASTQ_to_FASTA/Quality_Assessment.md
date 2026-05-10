# Quality Assessment with QUAST

QUAST (Quality Assessment Tool) evaluates genome assemblies and provides comprehensive
quality metrics to help you understand how good your assembly is. It can compare multiple
assemblies side by side and generate both HTML and PDF reports.

---

## Installation

```bash
# Via conda (recommended)
conda install -c bioconda quast

# Via pip
pip install quast

# Via apt
sudo apt-get update && sudo apt-get install -y \
    pkg-config libfreetype6-dev libpng-dev python3-matplotlib

# Or download directly
wget https://downloads.sourceforge.net/project/quast/quast-5.3.0.tar.gz
tar -xzf quast-5.3.0.tar.gz

# Verify installation
quast.py --version
```

> QUAST generates plots in HTML and PDF formats. For PDF output, make sure Matplotlib
> is installed (v1.1 or higher recommended).

---

## Basic Usage

### Single Assembly

```bash
python3 quast.py contigs.fasta
```

### Multiple Assemblies (side by side comparison)

```bash
quast.py \
    assembly1.fasta \
    assembly2.fasta \
    assembly3.fasta \
    -o quast_comparison
```

### With Reference Genome

```bash
quast.py contigs.fasta \
    -r reference.fasta \
    -g genes.txt \
    -1 reads1.fastq.gz \
    -2 reads2.fastq.gz \
    -o quast_output
```

### Filter Small Contigs

```bash
# Filter contigs shorter than 500 bp (recommended for bacterial genomes)
quast.py --min-contig 500 contigs.fasta -o quast_filtered
```

| Organism type | Recommended minimum contig length |
|---------------|----------------------------------|
| Bacterial genomes | 200 – 500 bp |
| Eukaryotic genomes | 1000 – 5000 bp |

---

## Key Metrics Explained

### Basic Metrics

| Metric | What it means |
|--------|--------------|
| **N50** | Length where contigs of this size or longer contain 50% of the total assembly — higher is better |
| **L50** | Number of contigs needed to reach N50 — lower is better |
| **Total length** | Sum of all contig lengths |
| **Number of contigs** | Total contigs in the assembly — fewer usually means better |
| **Largest contig** | Length of the longest contig |

### Reference-Based Metrics (when using `-r`)

| Metric | What it means |
|--------|--------------|
| **Genome fraction (%)** | Percentage of the reference covered by your assembly |
| **Misassemblies** | Number of positions with structural errors relative to reference |
| **Mismatches per 100 kbp** | Number of mismatches per 100,000 aligned bases |
| **Indels per 100 kbp** | Number of insertions/deletions per 100,000 aligned bases |

---

## Best Practices

- Always filter contigs below a meaningful length for your organism before assessment
- Compare multiple assemblies from different parameters or assemblers to find the best one
- Use a reference genome with `-r` when one is available for more detailed metrics
- Compare your results with similar published assemblies to set realistic expectations

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| PDF plots not generating | Install Matplotlib: `pip install matplotlib` |
| Running out of memory | Add `--space-efficient` flag for large datasets |
| Very high contig count | Lower `--min-contig` threshold or re-check trimming quality |

---

## Additional Resources

- [QUAST Documentation](http://quast.sourceforge.net/docs/manual.html)
- [QUAST GitHub](https://github.com/ablab/quast)
- [Official Installation Guide](https://quast.sourceforge.net/install.html)