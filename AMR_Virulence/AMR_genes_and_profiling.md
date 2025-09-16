# Antimicrobial Resistance (AMR) Analysis Tools Guide

## Introduction
This guide covers essential tools for antimicrobial resistance analysis in bacterial genomes. Each tool offers unique features for detecting and analyzing resistance genes and mutations.

Antibiotic resistance is a major global health threat. To track and understand it, scientists use bioinformatics tools to analyze bacterial genomes for antimicrobial resistance (AMR) genes. These tools compare a bacterial genome's DNA sequence to curated databases of known resistance genes, identifying which ones a bacterium carries.

he process of detecting AMR genes is straightforward: you'll take your bacterial genome assembly and screen it against one or more specialized databases. You can use web-based tools for a quick, visual analysis or command-line tools for automated, high-throughput screening.

## Commonly Used Tools

These tools are great for beginners or for quick analysis of one or a few samples without needing to install any software.

### ResFinder

ResFinder is a web-based tool from the Center for Genomic Epidemiology (CGE) that identifies acquired AMR genes and chromosomal mutations. It's user-friendly and very popular.

Usage: Simply upload your bacterial genome assembly (FASTA file) and click "submit." The service will compare your sequences to its databases and give you a detailed report of all resistance genes found.


# Web-based tool - No command line required
URL: https://cge.cbs.dtu.dk/services/ResFinder/

# Key Features:
- Identifies acquired antimicrobial resistance genes
- Detects chromosomal mutations
- Supports both assembled genomes and raw reads
- Provides detailed resistance gene annotations

### RGI (Resistance Gene Identifier)

RGI is the main tool of the CARD (Comprehensive Antibiotic Resistance Database), one of the most comprehensive and authoritative databases for resistance genes. RGI not only finds genes but also predicts their resistance mechanism.

Usage: Upload your FASTA file and select the analysis type (e.g., "Main Analysis"). The output includes predicted resistance genes, their mechanisms of action, and confidence scores.

# Web interface
URL: https://card.mcmaster.ca/analyze/rgi

## ABRicate

For analyzing many genomes at once, or for building automated pipelines, command-line tools are more efficient.

ABRicate is a versatile and widely used command-line tool for mass screening of contigs. It's fast and can use multiple databases.

```bash
# Installation
conda install -c bioconda abricate
```
```bash 
# Basic usage
abricate your_file.fasta              
```
```bash
Single file analysis
abricate *.fasta                      
```
```bash
Multiple files analysis
abricate --summary *.fasta > summary.tab  
```
 Create summary table

# Database options
ABRicate allows you to choose which database to use, including CARD and ResFinder.

```bash
abricate --list                       # List available databases
```
```bash
abricate --db card --file input.fasta # Use CARD database
```
```bash
abricate --db resfinder input.fasta   # Use ResFinder database
```

# Minimum coverage threshold
You can set minimum identity (--minid) and coverage (--mincov) thresholds to control how strict the match has to be. A common starting point is --minid 90 --mincov 90.

```bash
abricate --minid 80 --mincov 60 input.fasta
```

## Advanced Tools

### abriTAMR
abriTAMR is a more advanced pipeline built on top of ABRicate that generates a comprehensive AMR report. It's useful for a complete, structured analysis.

```bash
# Installation via conda
conda create -n abritamr -c bioconda abritamr
conda activate abritamr
```
```bash
# Basic usage
abritamr run --contigs genome.fasta --prefix klebsiella_amr --species Klebsiella_pneumoniae
```
This command will run a full analysis and create a report with a consistent naming scheme (my_amr_report).

### AMR Classification Guidelines

### MDR, XDR, PDR Criteria
Reference: [Clinical Microbiology and Infection Journal](https://www.clinicalmicrobiologyandinfection.com/article/S1198-743X(14)61632-3/fulltext)

Key definitions:
- MDR (Multidrug-Resistant): Non-susceptible to ≥1 agent in ≥3 antimicrobial categories
- XDR (Extensively Drug-Resistant): Non-susceptible to ≥1 agent in all but ≤2 categories
- PDR (Pandrug-Resistant): Non-susceptible to all antimicrobial agents listed

## Best Practices

1. Always use the latest database versions for accurate results
2. Cross-validate results using multiple tools
3. Consider minimum coverage and identity thresholds
4. Keep detailed records of database versions and parameters used
5. Validate critical findings with phenotypic testing

## Additional Resources

- [CARD Database](https://card.mcmaster.ca/)
- [ResFinder Database](https://cge.cbs.dtu.dk/services/ResFinder/)
- [NCBI AMRFinder](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/)

---
**Note**: This guide covers basic usage. For detailed parameters and advanced features, refer to each tool's documentation.
