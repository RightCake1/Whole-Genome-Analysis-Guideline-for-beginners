# AMR & Virulence Factor Analysis Guide

A complete guide for identifying antimicrobial resistance (AMR) genes and virulence factors
in bacterial genomes.

---

## What is AMR?

Antibiotic resistance is a major global health threat. To track and understand it, scientists
use bioinformatics tools to analyze bacterial genomes for antimicrobial resistance (AMR) genes.
These tools compare a bacterial genome's DNA sequence to curated databases of known resistance
genes, identifying which ones a bacterium carries.

## What are Virulence Factors?

Think of a bacterium's virulence factors as its "weaponry." They are the genes, proteins, or
other molecules that enable a pathogen to cause disease in a host.

# AMR Tools
## Web-Based Tools

### ResFinder
[ResFinder](https://cge.cbs.dtu.dk/services/ResFinder/) is a web-based tool from the Center
for Genomic Epidemiology (CGE) that identifies acquired AMR genes and chromosomal mutations.

- Upload your bacterial genome assembly (FASTA file) and click submit
- Identifies acquired antimicrobial resistance genes
- Detects chromosomal mutations
- Supports both assembled genomes and raw reads

### RGI / CARD
[RGI](https://card.mcmaster.ca/analyze/rgi) uses the Comprehensive Antibiotic Resistance
Database (CARD) — one of the most authoritative databases for resistance genes. It not only
finds genes but also predicts their resistance mechanism.

- Upload your FASTA file and select the analysis type
- Predicts resistance mechanisms and confidence scores

---

## Command-Line Tools

### ABRicate

ABRicate is a versatile command-line tool for mass screening of contigs across multiple
databases at once.

```bash
# Installation
conda install -c bioconda abricate

# Single file
abricate your_file.fasta

# Multiple files
abricate *.fasta

# Create summary table
abricate --summary *.fasta > summary.tab

# List available databases
abricate --list

# Use a specific database
abricate --db card --file input.fasta
abricate --db resfinder input.fasta

# Set minimum identity and coverage thresholds
abricate --minid 80 --mincov 60 input.fasta
```

To run ABRicate across multiple databases and generate both raw results and a summary matrix for all your isolates at once, use the script below and save it ``run_abricate.sh``. Make sure to update the paths to match
your own setup.

```bash
#!/bin/bash
# Define paths
INPUT_DIR="/home"
OUTPUT_DIR="/home"
mkdir -p "$OUTPUT_DIR"

# List of databases to run
DATABASES=("ncbi" "vfdb" "resfinder")

for DB in "${DATABASES[@]}"; do
    echo "Running ABricate with $DB database..."
    
    # 1. Run raw extraction
    abricate --db "$DB" --threads 4 "$INPUT_DIR"/*.fna > "$OUTPUT_DIR/abricate_${DB}_raw.tab"
    
    # 2. Generate summary matrix (Presence/Absence)
    abricate --summary "$OUTPUT_DIR/abricate_${DB}_raw.tab" > "$OUTPUT_DIR/abricate_${DB}_summary.csv"
    
    echo "Finished $DB."
done

echo "All ABricate runs complete. Check the /Docs folder!"
```

---

### abriTAMR

abriTAMR is a more advanced pipeline that generates a comprehensive, structured AMR report.
It uses AMRFinderPlus under the hood.

**Installation:**

```bash
# Create the environment (python 3.9 for best compatibility)
conda create -n abritamr -c bioconda -c conda-forge abritamr python=3.9 -y

# Activate it
conda activate abritamr

# Verify versions
abritamr --version
amrfinder --version

# Download the latest NCBI AMR database (requires internet)
amrfinder_update
```

**Prepare your isolate list:**

Create a TSV file with sample ID in column 1 and full file path in column 2:

```bash
ls /home/*.fna \
  | awk -F'/' '{print $NF "\t" $0}' \
  | sed 's/\.fna//' \
  > /home/isolates_map.tsv
```

**Run abriTAMR:**

```bash
abritamr run \
  --contigs /home/isolates_map.tsv \
  --species Klebsiella_pneumoniae \
  --prefix /home/ABRITAMR_FINAL_RESULTS \
  --jobs 1 \
  --threads 6
```
You can change the ``job`` and ``threads`` number according to your system.

---

### AMR Classification Guidelines (Klebsiella pnuemoniae)

| Class | Definition |
|-------|-----------|
| **MDR** (Multidrug-Resistant) | Non-susceptible to ≥1 agent in ≥3 antimicrobial categories |
| **XDR** (Extensively Drug-Resistant) | Non-susceptible to ≥1 agent in all but ≤2 categories |
| **PDR** (Pandrug-Resistant) | Non-susceptible to all antimicrobial agents listed |

Reference: [Clinical Microbiology and Infection Journal](https://www.clinicalmicrobiologyandinfection.com/article/S1198-743X(14)61632-3/fulltext)

---

# Virulence Factor Tools

## VFDB (Virulence Factors Database)

[VFDB](http://www.mgc.ac.cn/VFs/) is a comprehensive, curated database of known bacterial
virulence factors. It serves as the core data repository for virulence research.

- Search by sequence similarity (BLAST)
- Browse virulence factors by organism
- Compare virulence factors across species
- Download complete datasets

**Usage:**
1. Visit the [VFDB Analysis Tools](http://www.mgc.ac.cn/VFs/main.htm)
2. Run a BLAST search with your genome
3. Cross-reference results with literature
4. Download results for documentation

> Note: ABRicate (above) can also screen for virulence factors using `--db vfdb`
> which is faster for batch processing.

---

## VirulenceFinder

[VirulenceFinder](https://cge.cbs.dtu.dk/services/VirulenceFinder/) is a user-friendly
web-based tool from CGE that quickly scans a genome for known virulence factors. Perfect
for a fast initial check.

- Upload your FASTA file and submit
- Results show matched virulence genes with identity scores

---

## BIGSdb-Pasteur

[BIGSdb-Pasteur](https://bigsdb.pasteur.fr/) is a specialized integrated database for
bacterial typing and analysis. Great for combining virulence factor analysis with MLST.

**Key analysis tools:**

- **Sequence Query** — upload FASTA, search against database, set identity threshold
- **Strain Query** — search by strain ID, filter by species/serovar
- **Locus/Scheme Query** — search specific virulence genes, browse schemes

**Step-by-step:**
1. Prepare your genome in FASTA format
2. Click "Sequence Query" and upload your file
3. Select DNA sequence type and choose your database
4. Set identity threshold and submit
5. Review matching sequences and similarity scores
6. Download results in TSV/CSV or FASTA format

---

## Best Practices

1. Always use the latest database versions for accurate results
2. Cross-validate results using multiple tools (e.g. ResFinder + RGI)
3. Set minimum coverage and identity thresholds (`--minid 90 --mincov 90` is a good start)
4. Keep records of database versions and parameters used
5. Validate critical findings with phenotypic testing

---

## Additional Resources

- [CARD Database](https://card.mcmaster.ca/)
- [ResFinder](https://cge.cbs.dtu.dk/services/ResFinder/)
- [NCBI AMRFinder](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/)
- [VFDB](http://www.mgc.ac.cn/VFs/)
- [VirulenceFinder](https://cge.cbs.dtu.dk/services/VirulenceFinder/)
- [BIGSdb-Pasteur](https://bigsdb.pasteur.fr/)