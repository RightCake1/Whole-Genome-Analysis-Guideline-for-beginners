# Pangenome Analysis Guide Using Roary

## Introduction
Roary is a high-speed bacterial pangenome pipeline that can compute the pangenome of large datasets of bacterial isolates (1000s) within minutes. This guide covers installation, usage, and visualization of pangenome analyses.

## Installation and Setup

### Prerequisites
```bash
# Install Miniconda (if not already installed)
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

### Visualization Scripts

You can visualize Roary results using either the official script or a custom script provided in this repository.

```bash
# Option 1: Download and use the official Roary plots script
wget https://raw.githubusercontent.com/sanger-pathogens/Roary/master/contrib/roary_plots.py
chmod +x roary_plots.py

# Option 2: Use the custom visualization script included here
chmod +x Roary_Visualize.py
```

- [Roary_Visualize.py](Roary_Visualize.py): This custom script offers additional figures - Pangenome pie, Separate Pangenome Matrix, Seoarate Cluster Tree, Merged Tree and Matrix and Length barchart. The Official one will give Pangenome pie and Pangenome Matrix.

## Running Roary

```bash
# Create an environment. 
conda activate pangenome
```
# Annotate related strains and generated .gff files using Prokka.

```bash
for file in *.fasta; do
prokka --outdir output_"${file%.fasta}" "$file"
done 
```

# Run Roary. 

Basic Roary RUN

```bash
roary -f Roaryresults -p 6 -e -n -v --maft *.gff 
```
More Robust and clear roary (takes more time)

```bash
roary -f Roaryresults -p 12 -e --mafft -i 95 -cd 99 -iv 1.5 -v *.gff
```

# Use FastTree.

```bash
FastTree -nt -gtr -gamma -boot 100 -spr 4 Roaryresult/core_gene_alignment.aln > Roaryresult/mytree.newick
```
# Generate images. 
Need to download the [Roary.py](https://github.com/sanger-pathogens/Roary/tree/master/contrib/roary_plots)

```bash 
python roary_plots.py --labels Roaryresult/mytree.newick Roaryresult/gene_presence_absence.csv
```

# OR

```bash 
python roary_plots.py location/to/Pangenome.newick location/to/gene_presence_absence.csv --labels
```

### Parameter Explanations
* `-f`: Output directory
* `-e`: Create gene alignment files
* `-n`: Fast core gene alignment
* `-v`: Verbose output
* `-p`: Number of threads
* `-i`: Minimum percentage identity
* `-cd`: Percentage of isolates for core definition
* `-g`: Maximum clusters
* `-s`: Don't split paralogs
* `--mafft`: Use MAFFT for alignment

## Output Files and Analysis

### Key Output Files
```plaintext
gene_presence_absence.csv          # Main results table
gene_presence_absence.Rtab         # Binary matrix of gene presence/absence
core_gene_alignment.aln           # Core genes aligned
pan_genome_reference.fa           # All genes in FASTA format
clustered_proteins               # Clustered proteins
number_of_genes_in_pan_genome.Rtab  # Pan-genome size analysis
```

### Analyzing Results
1. Core genome size
2. Accessory genome distribution
3. Strain relationships
4. Gene presence/absence patterns
5. Functional annotations

## Best Practices

### Input Preparation
* Use consistent annotation methods
* Verify GFF3 format compliance
* Check for contamination
* Use appropriate strain selection

### Resource Management
* Adjust thread count appropriately
* Monitor memory usage
* Use SSD for temporary files
* Consider job scheduling for large datasets

### Quality Control
* Check alignment quality
* Verify core gene definitions
* Validate phylogenetic trees
* Assess clustering parameters

## Common Issues and Solutions

### Memory Issues
* Reduce thread count
* Increase memory allocation
* Split dataset into smaller batches
* Use memory-efficient mode

### Long Runtime
* Check input file quality
* Adjust parallelization
* Optimize temporary file location
* Consider hardware limitations


## Additional Resources

* [Roary GitHub](https://github.com/sanger-pathogens/Roary)
* [Roary Paper](https://academic.oup.com/bioinformatics/article/31/22/3691/240757)
* [Pangenome Analysis Methods](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00928-4)

---

**Note**: Regular updates of tools and appropriate parameter selection are essential for accurate analysis.