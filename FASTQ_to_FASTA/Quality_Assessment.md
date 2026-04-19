# QUAST: Quality Assessment Tool for Genome Assemblies

## Introduction
QUAST (QUality ASsessment Tool) is an excellent tool for evaluating genome assemblies. It provides comprehensive quality metrics that are crucial for assessing the quality of your assemblies. 

## Installation
The current stable release is [v5.3.0](https://downloads.sourceforge.net/project/quast/quast-5.3.0.tar.gz). The package includes everything needed for running QUAST, MetaQUAST, QUAST-LG, and Icarus. After downloading the tar.gz package, just unpack it with tar -xzf quast-<VERSION>.tar.gz and start using QUAST on your data or check the installation with ```quast.py --test```

Installation via package managers
The fully-functional QUAST toolkit is available in popular package managers, namely pip, Brewsci/bio, and Bioconda. To install it from there, make sure that the corresponding package manager is properly installed and configured on your machine and execute one of the following commands, respectively:

```
pip install quast
```
```
brew install quast
```
```
install -c bioconda quast
```  
```bash
# Verify installation
quast.py --version
```
You can check the [official site](https://quast.sourceforge.net/install.html) to see how to download it.

QUAST draws plots in two formats: HTML and PDF. If you need the PDF versions, make sure that you have installed Matplotlib. We recommend to use Matplotlib version 1.1 or higher. QUAST is fully tested with Matplotlib v.1.3.1. Installation on Ubuntu (tested on Ubuntu 20.04):
```
sudo apt-get update && sudo apt-get install -y pkg-config libfreetype6-dev libpng-dev python3-matplotlib
```

## Basic Usage

### Simple Assembly Assessment

```bash
# Basic usage
python3 quast.py contigs.fasta
```
or 
```
./quast.py test_data/contigs_1.fasta \
           test_data/contigs_2.fasta \
        -r test_data/reference.fasta.gz \
        -g test_data/genes.txt \
        -1 test_data/reads1.fastq.gz -2 test_data/reads2.fastq.gz \
        -o quast_test_output
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