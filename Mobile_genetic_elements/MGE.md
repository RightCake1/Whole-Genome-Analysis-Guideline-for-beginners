# Comprehensive Mobile Genetic Elements Analysis Guide

## Table of Contents
- [Web-based Tools](#web-based-tools)
- [Command-line Installation](#command-line-installation)
- [MGE Analysis Tools](#mge-analysis-tools)
- [Plasmid Analysis](#plasmid-analysis)
- [Prophage Analysis](#prophage-analysis)
- [CRISPR Analysis](#crispr-analysis)
- [Integration and Visualization](#integration-and-visualization)
- [Best Practices](#best-practices)

## Web-based Tools

### 1. Center for Genomic Epidemiology (CGE) Tools
**URL**: [https://www.genomicepidemiology.org/](https://www.genomicepidemiology.org/)

#### Tools Available:
- PlasmidFinder
- ResFinder
- VirulenceFinder
- MGE Finder

#### Usage Steps:
1. Visit the website
2. Select the appropriate tool
3. Upload your FASTA file (max 20 MB)
4. Configure parameters:
   - Minimum identity: 90% (default)
   - Minimum coverage: 60% (default)
5. Submit and wait for results
6. Download results in various formats (JSON, TSV, PDF)

### 2. IS-finder
**URL**: [https://isfinder.biotoul.fr/](https://isfinder.biotoul.fr/)

#### Usage Steps:
1. Go to IS-finder BLAST page
2. Upload sequence in FASTA format
3. Select BLAST program:
   - BLASTN for nucleotide sequences
   - BLASTX for protein sequences
4. Configure parameters:
   - E-value threshold: 1e-10 (recommended)
   - Word size: 11 (default)
5. Submit and analyze results
6. Export results table

### 3. Proksee Web-Server
**URL**: [https://proksee.ca/](https://proksee.ca/)

#### Features Available:
1. Alien Hunter for HGT detection
2. CRISPR-Cas++ analysis
3. Genome visualization
4. Comparative genomics

#### Usage Steps:
1. Register/Login to Proksee
2. Create new project
3. Upload genome files
4. Select analysis tools:
   - Alien Hunter
   - CRISPR-Cas++
   - Other analyses
5. Configure parameters
6. Run analysis
7. View/download results

### 4. PlasmidFinder Web Tool
**URL**: [https://cge.food.dtu.dk/services/plasmidfinder/](https://cge.food.dtu.dk/services/plasmidfinder/)

#### Usage Steps:
1. Upload FASTA file
2. Select database:
   - Enterobacteriaceae
   - Enterococcus
   - Staphylococcus
3. Configure settings:
   - Identity threshold: 95% (default)
   - Minimum coverage: 60% (default)
4. Submit analysis
5. Download results

### 5. PHASTER (PHAge Search Tool Enhanced Release)
**URL**: [https://phaster.ca/](https://phaster.ca/)

#### Usage Steps:
1. Choose submission type:
   - Upload sequence file
   - Paste sequence
   - Provide NCBI accession
2. Select analysis options:
   - Contigs vs complete genome
   - Sequence type (DNA/RNA)
3. Submit job
4. Monitor progress
5. Download results:
   - Summary table
   - Detailed annotations
   - Genome viewer

## Command-line Installation

```bash
# Create conda environment
conda create -n mge_analysis python=3.9
conda activate mge_analysis

# Install basic tools
conda install -c bioconda abricate mob_suite platon
conda install -c conda-forge biopython

# Install PlasmidSeeker
git clone https://github.com/bioinfo-ut/PlasmidSeeker.git
cd PlasmidSeeker
make
```

## Best Practices

### Analysis Workflow
1. Start with web tools for initial analysis:
   - Use PHASTER for prophage detection
   - Use PlasmidFinder for plasmid identification
   - Use IS-finder for insertion sequences
   - Use Proksee for HGT and CRISPR analysis

2. Follow up with command-line tools:
   - Use MOB-suite for detailed plasmid analysis
   - Use Platon for plasmid verification
   - Run custom scripts for integration

### Quality Control
1. Input Sequence Quality
   - Minimum contig length: >1000 bp
   - Assembly quality: N50 > 50kb
   - Coverage: >30x

### Result Validation
1. Cross-reference between web and command-line tools
2. Check for overlapping predictions
3. Validate key findings
4. Compare with related genomes

## References
- [CGE Tools](https://www.genomicepidemiology.org/)
- [IS-finder](https://isfinder.biotoul.fr/)
- [Proksee](https://proksee.ca/)
- [PHASTER](https://phaster.ca/)
- [PlasmidFinder](https://cge.food.dtu.dk/services/plasmidfinder/)
- [MOB-suite Documentation](https://github.com/phac-nml/mob-suite)