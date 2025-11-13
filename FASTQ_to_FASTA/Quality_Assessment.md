# QUAST: Quality Assessment Tool for Genome Assemblies

## Introduction
QUAST (QUality ASsessment Tool) is an excellent tool for evaluating genome assemblies. It provides comprehensive quality metrics that are crucial for assessing the quality of your assemblies. 


```bash
# Prerequisites

# All default requirements are usually preinstalled on Linux. The only missing one could be zlib-dev. See their web-site for installation details for various platforms. In particular, it is preinstalled on macOS, and it can be simply installed on Ubuntu as:

sudo apt-get install zlib1g-dev

#  QUAST draws plots in two formats: HTML and PDF. If you need the PDF versions, make sure that you have installed Matplotlib Python library. We recommend to use Matplotlib version 1.1 or higher. QUAST is fully tested with Matplotlib v.1.3.1. Installation on Ubuntu:

sudo apt-get install -y pkg-config libfreetype6-dev libpng-dev python-matplotlib
```

```bash
#To download the QUAST source code tarball and extract it, type:

wget https://github.com/ablab/quast/releases/download/quast_5.3.0/quast-5.3.0.tar.gz
tar -xzf quast-5.3.0.tar.gz
cd quast-5.3.0
```

```bash
# QUAST automatically compiles all its sub-parts when needed (on the first use). Thus, installation is not required. However, if you want to precompile everything and add quast.py to your PATH, you may choose either:
# Basic installation (about 120 MB):

./setup.py install

# or
# Full installation (about 540 MB, additionally includes (1) tools for SV detection based on read pairs, which is used for more precise misassembly detection, and (2) tools/data for reference genome detection in metagenomic datasets):

./setup.py install_full

# If you get error in installation then - 

sudo apt-get install python-distutils 

# Rerun ./setup.py install
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