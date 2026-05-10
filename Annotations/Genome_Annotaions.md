# Bacterial Genome Annotation Tools Guide

## Introduction

This guide covers essential tools for bacterial genome annotation. We'll explore both web-based (RAST) and command-line (Prokka) approaches to genome annotation.

Genome annotation is a critical step in bacterial genomics, enabling the identification of genes, their functions, and associated biological pathways. This guide introduces two widely used tools—RAST (web-based) and Prokka (command-line)—for efficient and accurate annotation of bacterial genomes.

---

## RAST (Rapid Annotation using Subsystem Technology)

### Overview

[RAST](https://rast.nmpdr.org/rast.cgi?page=Upload) is a web-based platform designed for the automated annotation of bacterial and archaeal genomes. It integrates gene prediction with functional assignment and pathway reconstruction.

### Access and Usage

Required input:

- Assembled genome in FASTA format
- Taxonomy information
- Domain (Bacteria/Archaea)

### Key Features

- Automated gene calling
- Functional annotation
- Metabolic reconstruction
- Comparative genomics
- Customizable annotation parameters

### SEED Viewer Analysis

After annotation completion:

1. Navigate to "Browse annotated genome"
2. Explore subsystems and features
3. Access metabolic pathways
4. Download annotations in various formats

---

## Prokka (Rapid Prokaryotic Genome Annotation)

### Installation

```bash
# Create conda environment
conda create -c bioconda -n prokka prokka

# Activate environment
conda activate prokka

# Verify installation
prokka --version
```

### Basic Usage

```bash
# Simple annotation
prokka contigs.fasta

# Specify output directory
prokka --outdir mygenome contigs.fasta
```

### Running Prokka on Multiple Genomes

If you have multiple FASTA files, use the script below to annotate all of them in one go. Make sure to change the directory paths to match your own setup. Create a new empty text file as save it as ``run_prokka.sh``

```bash
# 1. Create the destination directory if it doesn't exist
DEST_DIR="/home/rightcake/Fida_thesis/Annotations"
mkdir -p "$DEST_DIR"

# 2. Run the loop from your fasta directory
cd /home/rightcake/Fida_thesis/fasta

for file in *.fna; do
    # Extract filename without .fna
    name=$(basename "$file" .fna)
    
    echo "Starting annotation for: $name"
    
    # Run Prokka
    # --outdir points to the new Annotations folder
    # --prefix ensures files inside match the genome name
    prokka --outdir "$DEST_DIR/${name}_annot" \
           --prefix "$name" \
           --locustag "$name" \
           --cpus 8 \
           "$file"
done
```
Make it executable
```
chmod +x run_prokka.sh
```
Run it
```
./run_prokka.sh
```

### Output Files

- `.gff` — Annotation in GFF3 format
- `.gbk` — GenBank file format
- `.faa` — Protein sequences
- `.ffn` — Nucleotide sequences
- `.sqn` — NCBI submission format
- `.fna` — Nucleotide FASTA file
- `.txt` — Statistics summary
- `.log` — Log file

---

## Best Practices

1. **Quality Control**
   - Ensure genome assembly quality before annotation
   - Check for contamination and completeness
   - Verify genome is properly formatted

2. **Tool Selection**
   - Use RAST for: quick web-based analysis, metabolic reconstruction, comparative genomics
   - Use Prokka for: batch processing, local/offline analysis, custom database integration

3. **Documentation**
   - Record tool versions
   - Save all parameters used
   - Document any custom databases

---

## Tips for Better Results

**RAST**
- Provide accurate taxonomy information
- Allow sufficient time for processing
- Download results in multiple formats

**Prokka**
- Use species-specific databases when available
- Adjust `--mincontiglen` for draft genomes
- Enable `--compliant` for GenBank submissions

---

## Additional Resources

- [RAST Tutorial](https://www.theseed.org/wiki/SEED_Viewer_Tutorial)
- [Prokka GitHub](https://github.com/tseemann/prokka)
- [NCBI Prokaryotic Annotation Guidelines](https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/)
- [Bakta](https://github.com/oschwengers/bakta)