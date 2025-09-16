# QUAST: Quality Assessment Tool for Genome Assemblies

## Introduction
QUAST (QUality ASsessment Tool) is an excellent tool for evaluating genome assemblies. It provides comprehensive quality metrics that are crucial for assessing the quality of your assemblies. 


```bash
## Installation
conda create -n bioinfo_quast python=3.8
conda activate bioinfo_quast
```
```bash 
# Ensure channels are added in the right order
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

```bash
# Try installing QUAST again
conda install -c bioconda quast
```

```bash
# Verify installation
quast.py --version
```

## Basic Usage

### Simple Assembly Assessment

```bash
# Basic usage
python3 quast.py contigs.fasta
```

```bash 
# Multiple assemblies comparison
quast.py \
    assembly1.fasta assembly2.fasta assembly3.fasta \
    -o quast_comparison
```

### Filtering Small Contigs

```bash
# Filter contigs shorter than 1000 bp
quast.py --min-contig 1000 contigs.fasta -o quast_filtered

# Common minimum contig lengths:
# Bacterial genomes: 200-500 bp
# Eukaryotic genomes: 1000-5000 bp
```
With QUAST, you can quickly identify strengths and weaknesses of your genome assemblies, guide parameter tuning, and ensure your assemblies meet the required quality standards.

## Key Metrics Explained

### Basic Metrics
* **N50**: Length where contigs of this length or longer contain 50% of genome
* **L50**: Number of contigs needed to reach N50
* **Total length**: Sum of all contig lengths
* **Number of contigs**: Total number of contigs in assembly
* **Largest contig**: Length of the longest contig

### Reference-based Metrics (when using -r)
* **Genome fraction (%)**: Percentage of reference covered by assembly
* **Misassemblies**: Number of positions with breakpoints relative to reference
* **Mismatches per 100 kbp**: Number of mismatches per 100,000 aligned bases
* **Indels per 100 kbp**: Number of insertions/deletions per 100,000 aligned bases

## Best Practices

### Assembly Assessment
* Always filter contigs below meaningful length for your organism
* Compare multiple assemblies from different parameters/assemblers
* Use reference genome when available
* Check both basic stats and alignment-based metrics

### Resource Management
* Adjust thread count based on system capabilities
* Monitor memory usage for large assemblies
* Consider using `--space-efficient` for large datasets

### Output Interpretation
* Focus on metrics relevant to your research goals
* Consider biological context when interpreting results
* Look for red flags in alignment statistics
* Compare results with similar published assemblies

## Additional Resources

* [QUAST Documentation](http://quast.sourceforge.net/docs/manual.html)
* [QUAST GitHub Repository](https://github.com/ablab/quast)
* [QUAST Tutorial](http://quast.sourceforge.net/docs/manual.html#sec3)

---

**Note**: For detailed documentation and additional features, consult the [official QUAST manual](http://quast.sourceforge.net/docs/manual.html).