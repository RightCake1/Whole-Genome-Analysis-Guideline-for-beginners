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

### What is Prokka?

Prokka is a rapid command-line tool for annotating bacterial genome assemblies. Once
you have an assembled genome in FASTA format, Prokka scans it to identify and label all
the biological features — genes, rRNA, tRNA, and coding sequences — and assigns
functional descriptions to them where possible.

It produces several output files, the most important being the `.gff` file (used by
pangenome tools like Roary and Panaroo), the `.faa` file (protein sequences), and the
`.gbk` file (GenBank format for submission). Prokka runs in minutes and is the standard
first step after genome assembly.
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

### Extracting Summary Statistics from Prokka Results

After annotating all your genomes, you can extract a comprehensive summary table covering
genome size, GC content, CDS count, tRNA, rRNA, hypothetical proteins, efflux pumps, and
transposases across all isolates at once.

Save the script below as `compile_prokka.sh` and update the paths to match your setup:

```bash
#!/bin/bash
# Define paths
ANNOTATIONS_DIR="/home/rightcake/Fida_thesis/Annotations"
OUTPUT_DIR="/home/rightcake/Fida_thesis/Docs"
OUTPUT_FILE="$OUTPUT_DIR/prokka_comprehensive_summary.tsv"
mkdir -p "$OUTPUT_DIR"

# Header
echo -e "Sample_ID\tTotal_Bases\tGC_Content\tContigs\tCDS\tHypothetical_Prots\tRibosomal_Prots\tEfflux_Pumps\tTransposases\ttRNA\trRNA" > "$OUTPUT_FILE"

echo "Extracting data from annotation folders..."

for dir in "$ANNOTATIONS_DIR"/*/ ; do
    sample=$(basename "$dir")
    txt_file=$(ls "$dir"/*.txt 2>/dev/null | grep -v "log")
    tsv_file=$(ls "$dir"/*.tsv 2>/dev/null | grep -v "prokka")
    fna_file=$(ls "$dir"/*.fna 2>/dev/null)

    if [ -f "$txt_file" ] && [ -f "$tsv_file" ]; then
        # Genome stats
        contigs=$(grep -c ">" "$fna_file")
        bases=$(grep -v ">" "$fna_file" | tr -d '\n' | wc -c)
        gc_count=$(grep -v ">" "$fna_file" | tr -d -c 'GCgc' | wc -c)
        gc_pct=$(echo "scale=2; ($gc_count * 100) / $bases" | bc)

        # Annotation stats
        cds=$(grep "CDS:" "$txt_file" | awk '{print $2}')
        trna=$(grep "tRNA:" "$txt_file" | awk '{print $2}')
        rrna=$(grep "rRNA:" "$txt_file" | awk '{print $2}')

        # Functional insights
        hypo=$(grep -c "hypothetical protein" "$tsv_file")
        ribo=$(grep -i -c "ribosomal protein" "$tsv_file")
        efflux=$(grep -i -c "efflux pump" "$tsv_file")
        transp=$(grep -i -c "transposase" "$tsv_file")

        echo -e "$sample\t$bases\t$gc_pct\t$contigs\t$cds\t$hypo\t$ribo\t$efflux\t$transp\t$trna\t$rrna" >> "$OUTPUT_FILE"
    fi
done

echo "Done! File saved at: $OUTPUT_FILE"
```

```bash
# Make executable and run
chmod +x compile_prokka.sh
./compile_prokka.sh
```

The output is a `.tsv` file you can open directly in Excel or use for downstream
statistical analysis and visualization.


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