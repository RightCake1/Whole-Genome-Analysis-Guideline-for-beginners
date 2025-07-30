# Plasmid Detection Tools Guide

A comprehensive guide for identifying plasmids using Deeplasmid, Platon, and MOB-suite.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Tools Overview](#tools-overview)
- [Deeplasmid Analysis](#deeplasmid-analysis)
- [Platon Analysis](#platon-analysis)
- [MOB-suite Analysis](#mob-suite-analysis)
- [Troubleshooting](#troubleshooting)

## Prerequisites
- Docker account
- Conda environment
- Input FASTA files
- Basic command line knowledge

## Tools Overview

### Supported Tools
1. **Platon**: Plasmid contig classification
2. **MOB-suite**: Plasmid mobility prediction

## Platon Analysis

### Setup
1. Create Conda environment
```bash
conda create -n platon
conda activate platon
conda install platon
```

### Usage
```bash
# Activate environment
conda activate platon

# Run Platon
platon --db db --output PlatonResults Your_file.fasta
```

## MOB-suite

### Installation
1. **Using Conda (Recommended)**
```bash
# Create and activate new environment
pip3 install mob_suite

2. **Using pip**
```bash
pip install mob_suite
```

3. **Dependencies**
- BLAST+ (v2.7.1 or higher)
- MMSeqs2
- Mash
- bioperl
- ncbi-blast+

```bash
# Install dependencies via conda
conda install -c bioconda blast mmseqs2 mash perl-bioperl ncbi-blast+
```

### Usage
```bash
# Activate environment (if using conda)
conda activate mob_suite

# Run MOB-suite analysis
mob_recon -i contigs.fasta -o Plasmids_list
```

### Common Options
```bash
mob_recon --help  # Display all available options

# Basic usage with additional parameters
mob_recon \
    -i contigs.fasta \
    -o output_directory \
    --run_typer \  # Include plasmid typing
    --keep_tmp \   # Keep temporary files
    -n 8          # Use 8 threads
```

## Additional Resources
- [Platon GitHub](https://github.com/oschwengers/platon)
- [MOB-suite](https://github.com/phac-nml/mob-suite)

