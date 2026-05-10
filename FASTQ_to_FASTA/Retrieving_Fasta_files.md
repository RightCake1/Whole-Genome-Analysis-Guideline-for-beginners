## 📥 Genome Download Workflow (NCBI Datasets CLI)

This guide explains how to set up your environment and automate the download of genome sequences and GFF3 annotation files using the NCBI Datasets CLI.

## What is NCBI Datasets CLI?

NCBI Datasets CLI is a command-line tool developed by NCBI for downloading genome
sequences, annotations, and metadata directly from NCBI databases. Instead of manually
downloading genomes one by one through a browser, you can provide a list of accession
IDs and the tool will automatically fetch all the corresponding FASTA and GFF3 files
in bulk.

This makes it essential for large-scale comparative genomics studies where you need
to download hundreds or thousands of reference genomes efficiently and reproducibly.

## 🧪 1. Environment Setup

Create a dedicated Conda environment to manage dependencies.

```bash
# Create the environment and install the CLI tool
conda create -n ncbi_datasets -c conda-forge ncbi-datasets-cli -y

# Activate the environment
conda activate ncbi_datasets
```

## 📄 2. Prepare Input Data

Prepare a text file containing your NCBI accession IDs.

```bash
# Navigate to your working directory
cd /path/to/your/folder

# Create the accession list file
touch accessions.txt
```

Open `accessions.txt` and add your accession IDs (one per line). You can get the accession IDs from [GTDB](https://gtdb.ecogenomic.org/), [NCBI](https://www.ncbi.nlm.nih.gov/), or the [IMG JGI web server](https://img.jgi.doe.gov/).

```
GCA_000001405.40
GCF_000005845.2
GCA_024321235.1
```

> ⚠️ Make sure there are no trailing blank lines or extra spaces.

## ⚙️ 3. Automation Script

Create a shell script to automate genome downloads with a built-in resume feature.

```bash
touch download_genomes.sh
```

Paste the code below into `download_genomes.sh` and save it. Make sure to change `TARGET_DIR` to your own working directory path.

```bash
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
```
Make it executable. 
```
chmod +x download_genomes.sh
```
Run the program. 
```
./download_genomes.sh
```
Now wait for the download to complete

## ▶️ 4. Execution

Make the script executable and run it.

```bash
# Give execution permission
chmod +x download_genomes.sh

# Run the script
./download_genomes.sh
```

## 📚 Further Reading

For more details, check the official documentation:  
[NCBI Datasets CLI – Download & Installation Guide](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/download-and-install/)