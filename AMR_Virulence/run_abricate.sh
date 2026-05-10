#!/bin/bash

# Define paths
INPUT_DIR="/home/rightcake/Fida_thesis/fasta"
OUTPUT_DIR="/home/rightcake/Fida_thesis/Docs"

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
