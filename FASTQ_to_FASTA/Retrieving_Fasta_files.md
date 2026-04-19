## 📥 Genome Download Workflow (NCBI Datasets CLI)

This guide explains how to set up your environment and automate the download of genome sequences and GFF3 annotation files using the NCBI Datasets CLI.

🧪 1. Environment Setup

Create a dedicated Conda environment to manage dependencies.

```bash
# Create the environment and install the CLI tool
conda create -n ncbi_datasets -c conda-forge ncbi-datasets-cli -y

# Activate the environment
conda activate ncbi_datasets
```

📄 2. Prepare Input Data

Prepare a text file containing your NCBI accession IDs.

```
# Navigate to your working directory
cd /path/to/your/folder

# Create the accession list file
touch accessions.txt
```

Open accessions.txt and add your accession IDs (one per line). You can get the accession IDs from [GTDB](https://gtdb.ecogenomic.org/), [NCBI](https://www.ncbi.nlm.nih.gov/), or the [IMG JGI web server](https://img.jgi.doe.gov/).

```
Example:

GCA_000001405.40

GCF_000005845.2

GCA_024321235.1
```
⚠️ Make sure there are no trailing blank lines or extra spaces.

⚙️ 3. Automation Script

Create a shell script to automate genome downloads with a built-in resume feature.

```
# Create the script file
touch download_genomes.sh
```

 Paste the code from [`download_genomes.sh`](./download_genomes.sh) into the empty text file and save it or just download the bash file from the repo.

▶️ 4. Execution

Make the script executable and run it.
```
# Give execution permission
chmod +x download_genomes.sh

# Run the script
./download_genomes.sh
```

## 📚 Further Reading

For more details, check the official documentation:  
[NCBI Datasets CLI – Download & Installation Guide](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/download-and-install/)