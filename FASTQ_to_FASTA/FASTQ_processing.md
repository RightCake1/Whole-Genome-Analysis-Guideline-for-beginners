# FASTQ to FASTA Processing Guide

## Introduction

This guide is all about handling FASTQ sequence files, performing quality control, and getting them ready for downstream analysis. This step-by-step workflow helps manage files, assess quality, and trim sequences effectively.

## Prerequisites

```bash
# Install required tools via conda
conda create -n seq_processing
conda activate seq_processing
conda install -c bioconda fastqc trimmomatic

or 

#Install directly from terminal
sudo apt install fastqc
sudo apt install ttrimmomatic

# Verify installations
fastqc --version
trimmomatic -version
```

## Detailed Workflow

### 1. Obtaining FASTQ Sequences

* Download sequences from sequencing facility or public databases
* Common sources:
  * NCBI Sequence Read Archive (SRA)
  * European Nucleotide Archive (ENA)
  * Commercial sequencing providers
  * Provided by supervisors
  * Genome Taxonmomy Database 

### 2. File Decompression

```bash
# For gzip compressed files
gunzip *.fastq.gz

# For zip files
unzip sequence_files.zip

# For tar archives
tar -xvf sequence_files.tar.gz
```

### 3. File Organization and Renaming

```bash
# Create organized directory structure
mkdir -p {raw_data,trimmed,fastqc_reports,final_output}

# Rename files for clarity
```

### 4. Merging Multiple FASTQ Files

```bash
# Merge forward reads
cat sample1_L001_R1.fastq \
    sample1_L002_R1.fastq \
    sample1_L003_R1.fastq \
    sample1_L004_R1.fastq > R1.fastq

# Merge reverse reads
cat sample1_L001_R2.fastq \
    sample1_L002_R2.fastq \
    sample1_L003_R2.fastq \
    sample1_L004_R2.fastq > R2.fastq

# Verify file sizes
ls -lh R*.fastq
```

### 5. Initial Quality Control with FastQC

```bash
# Basic usage
fastqc R1.fastq R2.fastq

# Advanced usage
fastqc \
    --outdir fastqc_reports \
    --threads 4 \
    --noextract \
    --format fastq \
    R*.fastq

# Run on multiple files in parallel
fastqc *.fastq
```

#### Interpreting FastQC Reports

Key metrics to examine:

* Per base sequence quality
* Per sequence quality scores
* Per base sequence content
* Overrepresented sequences
* Adapter content
* GC content

### 6. Sequence Trimming with Trimmomatic

```bash
# Basic paired-end trimming
trimmomatic PE \
    -phred33 \
    R1.fastq R2.fastq \
    R1P.fastq R1U.fastq \ 
    R2P.fastq R2U.fastq \
    SLIDINGWINDOW:4:20 \
    LEADING:20 \
    TRAILING:20 \
    MINLEN:36

# Can exclude R1U and R2U since they are unpaired reads and not needed for downstream analysis
```

#### Trimmomatic Parameters Explained

* **SLIDINGWINDOW:4:20**
  * Window size: 4 bases
  * Quality threshold: 20
  * Recommended ranges: Window 4-5, Threshold 15-30

* **LEADING/TRAILING:20**
  * Trim low quality bases from start/end
  * Adjust based on FastQC quality plot
  * Common range: 20-30

* **CROP:147**
  * Cut reads to specified length
  * Use when quality drops at specific position
  * Determine from FastQC per base quality

* **HEADCROP:15**
  * Remove specified number of bases from start
  * Use when consistent poor quality at read start
  * Check FastQC per base sequence content

* **MINLEN:36**
  * Discard reads below this length
  * Adjust based on downstream analysis needs

### 7. Post-trimming Quality Control

```bash
# Run FastQC on trimmed files
fastqc trimmed_R*P.fastq
```

## Best Practices

### File Management
* Maintain original files in a separate directory
* Use consistent naming conventions
* Track file provenance
* Calculate and verify checksums

### Quality Control
* Always run FastQC before and after trimming
* Compare paired-end read qualities
* Monitor sequence duplication levels
* Check for adapter contamination

### Resource Management
* Monitor disk space during merging
* Use appropriate thread counts
* Consider using ramdisk for temporary files
* Compress intermediate files when possible

### Common Issues and Solutions

#### Low Quality Scores
* Increase SLIDINGWINDOW threshold
* Adjust LEADING/TRAILING values
* Consider shorter CROP length

#### Adapter Contamination
* Use appropriate adapter sequences
* Adjust ILLUMINACLIP parameters
* Verify adapter orientation

#### Uneven Coverage
* Check for PCR duplicates
* Verify library complexity
* Consider sequence normalization

## Additional Resources

* [FastQC Documentation](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
* [Trimmomatic Manual](http://www.usadellab.org/cms/?page=trimmomatic)
* [Illumina Adapter Sequences](https://support.illumina.com/downloads/illumina-adapter-sequences-document-1000000002694.html)

---

> **Note**: Parameters should be adjusted based on your specific dataset and research goals. Always verify output quality after each step.