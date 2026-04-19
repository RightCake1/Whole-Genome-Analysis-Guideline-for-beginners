#!/bin/bash

# Configuration
TARGET_DIR="/home/rightcake/Fida_thesis"
ACCESSION_LIST="${TARGET_DIR}/accessions.txt"

cd "$TARGET_DIR" || { echo "Directory not found"; exit 1; }

echo "📂 Working directory: $TARGET_DIR"

while read -r ACC || [ -n "$ACC" ]; do
    # Clean whitespace and carriage returns
    ACC=$(echo "$ACC" | tr -d '\r' | xargs)
    [ -z "$ACC" ] && continue

    ZIP_NAME="${ACC}.zip"

    # Check if the zip already exists to allow resuming
    if [ -f "$ZIP_NAME" ]; then
        echo "✅ $ACC already exists. Skipping..."
    else
        echo "🚀 Downloading $ACC (Fasta + GFF3)..."
        
        datasets download genome accession "$ACC" \
            --include genome,gff3 \
            --filename "$ZIP_NAME"
            
        if [ $? -eq 0 ]; then
            echo "✨ $ACC download complete."
        else
            echo "❌ Error downloading $ACC"
        fi
    fi
done < "$ACCESSION_LIST"

echo "🎉 All downloads checked and completed!"