# Plasmid Detection Tools Guide

A comprehensive guide for identifying plasmids using Deeplasmid, Platon, and MOB-suite.

Finding plasmids in bacterial genomes is important because they often carry genes for antibiotic resistance and virulence, which can be shared between bacteria. This guide covers how to use two popular command-line tools, Platon and MOB-suite,

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
Platon is a tool that identifies plasmid contigs using a combination of gene analysis and comparisons to a known plasmid database.
Install Platon using Conda. This is the recommended method as it will automatically install all the necessary dependencies.

### Setup
1. Create Conda environment and install platon
```bash
conda create -n platon -c bioconda platon
```
2. Database
Download the database. Platon needs a database of known plasmid sequences to work effectively. Download and decompress the database files.

```bash
$ wget https://zenodo.org/record/4066768/files/db.tar.gz
$ tar -xzf db.tar.gz
$ rm db.tar.gz
```

### Usage
To run Platon, you need to tell it where the database is located and where to put the output.

```bash
# Activate environment
conda activate platon
```
Run Platon with your FASTA file.

```bash
# Run Platon
platon --db <db-path> --output PlatonResults Your_file.fasta
```
--db <db-path>: Replace <db-path> with the location of the database folder you downloaded.

--output PlatonResults: This tells Platon to save its results in a new folder named PlatonResults.

your_genome_file.fasta: The name of your bacterial genome assembly file.

## MOB-suite
MOB-suite is a comprehensive tool that not only identifies plasmids but also predicts their mobility and assigns a replicon type.

### Installation

The easiest way to install MOB-suite and its dependencies is with Conda.

1. **Using Conda (Recommended)**
# Create environment and install mobsuite

```bash
conda create -n mob_suite -c bioconda mob_suite
```
2. **Using pip**
```bash
pip install mob_suite
```

3. **Dependencies** 
If using conda they will be automatically installed
- BLAST+ (v2.7.1 or higher)
- MMSeqs2
- Mash
- bioperl
- ncbi-blast+

### Usage
MOB-suite's main command is mob_recon, which stands for "plasmid mobility reconnaissance." It analyzes your contigs and produces a detailed report.

```bash
# Activate environment (if using conda)
conda activate mob_suite
```

```bash
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

Troubleshooting
Database Not Found: Ensure you have downloaded the database for Platon and that the path you provide with the --db flag is correct.

Missing Dependencies: If you are not using Conda, you must manually install all dependencies, including BLAST+ and MMSeqs2. The installation will likely fail if a dependency is missing.

Low Confidence: If a tool reports a contig as potentially a plasmid but with low confidence, it may be a chromosomal fragment or a novel plasmid. Consider a manual inspection or use another tool to cross-validate the finding.