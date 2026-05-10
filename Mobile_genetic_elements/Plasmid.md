# Plasmid Detection Tools Guide

A comprehensive guide for identifying plasmids using Platon and MOB-suite.

Finding plasmids in bacterial genomes is important because they often carry genes for
antibiotic resistance and virulence, which can be shared between bacteria. This guide
covers how to use two popular command-line tools, Platon and MOB-suite.

---

## Table of Contents
- [Tools Overview](#tools-overview)
- [Platon Analysis](#platon-analysis)
- [MOB-suite Analysis](#mob-suite-analysis)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Tools Overview

| Tool | Purpose |
|------|---------|
| **Platon** | Plasmid contig classification using gene analysis + known plasmid database |
| **MOB-suite** | Plasmid mobility prediction + replicon typing |

---

## Platon Analysis

Platon identifies plasmid contigs using a combination of gene analysis and comparisons
to a known plasmid database.

### Installation

```bash
conda create -n platon -c bioconda platon
conda activate platon
```

### Download Database

Platon needs a database of known plasmid sequences to work. Download and decompress it:

```bash
wget https://zenodo.org/record/4066768/files/db.tar.gz
tar -xzf db.tar.gz
rm db.tar.gz
```

### Usage

```bash
conda activate platon

platon --db <db-path> --output PlatonResults your_genome_file.fasta
```

| Parameter | Description |
|-----------|-------------|
| `--db <db-path>` | Path to the database folder you downloaded |
| `--output PlatonResults` | Save results in a folder named PlatonResults |
| `your_genome_file.fasta` | Your bacterial genome assembly file |

---

## MOB-suite Analysis

MOB-suite is a comprehensive tool that not only identifies plasmids but also predicts
their mobility and assigns a replicon type.

### Installation

```bash
# Create environment and install
conda create -n mobsuite -c bioconda mob_suite -y
conda activate mobsuite
```

### Initialize the Database

Since it's your first time, you must download the plasmid database before running anything:

```bash
mob_init
```

> ⚠️ This requires an internet connection and may take a while to download.

### Basic Usage

```bash
conda activate mobsuite

# Single file
mob_recon -i contigs.fasta -o Plasmids_list

# With additional options
mob_recon \
    -i contigs.fasta \
    -o output_directory \
    --run_typer \
    --keep_tmp \
    -n 8
```

### Running MOB-suite on Multiple Genomes

To run MOB-suite across all your isolates at once with a progress bar, use the script
below. Make sure to update the paths to match your own setup.

```bash
#!/bin/bash

mkdir -p /home/rightcake/Fida_thesis/MOB_Results

# Get the total count of files
files=(/home/rightcake/Fida_thesis/fasta/*.fna)
total_files=${#files[@]}
current_count=0

echo "Starting MOB-suite Plasmid Typing for $total_files isolates..."

for f in "${files[@]}"; do
    ((current_count++))
    id=$(basename "$f" .fna)
    
    # Calculate percentage and progress bar width (20 blocks total)
    percent=$((current_count * 100 / total_files))
    filled=$((percent / 5))
    empty=$((20 - filled))
    
    # Print the progress bar on one line
    printf "\rProgress: ["
    printf "%${filled}s" '' | tr ' ' '#'
    printf "%${empty}s" '' | tr ' ' '.'
    printf "] %d%% (%d/%d) - Current: %s" "$percent" "$current_count" "$total_files" "$id"
    
    # Run mob_typer (logging output to keep the progress bar clean)
    mob_typer --infile "$f" \
              --outdir "/home/rightcake/Fida_thesis/MOB_Results/$id" \
              --db /home/rightcake/Fida_thesis/mobsuite_db/data \
              > "/home/rightcake/Fida_thesis/MOB_Results/${id}_run.log" 2>&1
done

echo -e "\n\n✅ MOB-suite analysis complete!"
```

### Run the Script

```bash
chmod +x run_mobsuite.sh
./run_mobsuite.sh
```

---

## Troubleshooting

**Database Not Found** — Ensure you have downloaded the database and that the path
provided with `--db` is correct.

**Missing Dependencies** — If not using Conda, you must manually install all
dependencies including BLAST+, MMSeqs2, Mash, and bioperl.

**Low Confidence Results** — If a tool reports a contig as potentially a plasmid
but with low confidence, it may be a chromosomal fragment or a novel plasmid.
Consider manual inspection or cross-validate using another tool.

---

## Additional Resources

- [Platon GitHub](https://github.com/oschwengers/platon)
- [MOB-suite GitHub](https://github.com/phac-nml/mob-suite)
- [PCNE](https://github.com/riccabolla/PCNE)