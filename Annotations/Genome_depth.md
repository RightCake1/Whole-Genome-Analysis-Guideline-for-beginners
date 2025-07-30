# Read Mapping and Coverage Analysis Guide
## Using BWA, Samtools, and Bowtie2

## Introduction
This guide covers the process of mapping sequencing reads to a reference genome and analyzing coverage metrics using BWA, Samtools, and Bowtie2. These tools are essential for various genomic analyses, including variant calling and genome assembly validation.

## Installation

```bash
# Via conda (recommended)
conda create -n mapping
conda activate mapping
conda install -c bioconda bwa samtools bowtie2

# Verify installations
bwa
samtools --version
bowtie2 --version
```

## Read Mapping Workflow


### 2. Perform Read Mapping
```bash
# Indexed. Code:
bwa index contigs.fasta
# Made SAM file. Code:
bwa mem -t 12 contigs.fasta R1p.fastq R2p.fastq > contigs.sam 
# Converted SAM to BAM. Code:
samtools view -S -b contigs.sam > contigs.bam
# Sorted Alignment. Code:
samtools sort contigs.bam --reference contigs.fasta > contigs_sort.bam
# Checked Mean Read Depth. Code:
samtools depth -a contigs_sort.bam | awk '{c++;s+=$3}END{print s/c}'
```

### 4. Coverage Analysis

```bash
# Basic coverage statistics
samtools coverage contigs_sort.bam

# Detailed per-base coverage
samtools depth -a contigs_sort.bam > coverage.txt

# Mean read depth
samtools depth -a contigs_sort.bam | \
    awk '{c++;s+=$3}END{print "Mean depth = " s/c}'

# Coverage breadth (percentage of reference covered)
samtools depth -a contigs_sort.bam | awk '{c++;s+=$3}END{print s/c}'

# or 

samtools depth -a contigs_sort.bam | awk '{c++; if($3>0) total+=1}END{print (total/c)*100}'

# Coverage at different thresholds
samtools depth -a contigs_sort.bam | \
    awk '{c++; if($3>=10) d10++; if($3>=20) d20++; if($3>=30) d30++}END{
        print "≥10x coverage: " (d10/c)*100 "%"
        print "≥20x coverage: " (d20/c)*100 "%"
        print "≥30x coverage: " (d30/c)*100 "%"
    }'
```

## Best Practices

### Resource Management
* Allocate appropriate thread count
* Monitor memory usage
* Use sorted BAM files when possible
* Index reference genomes once and reuse

### Quality Control
* Check mapping statistics
* Verify proper pair rates
* Monitor duplicate levels
* Assess coverage uniformity

### Common Issues and Solutions

#### Low Mapping Rate
* Check read quality
* Verify reference genome
* Adjust mapping parameters
* Consider trimming reads

#### High Duplicate Rate
* Check library complexity
* Verify PCR conditions
* Consider removing duplicates
* Assess sequencing depth

#### Uneven Coverage
* Check GC bias
* Verify library preparation
* Consider PCR-free protocols
* Assess mapping quality


## Additional Resources

* [BWA Manual](http://bio-bwa.sourceforge.net/bwa.shtml)
* [Samtools Documentation](http://www.htslib.org/doc/samtools.html)
* [Bowtie2 Manual](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml)
* [SAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)

---

**Note**: Parameters should be adjusted based on your specific dataset and research goals. Always verify output quality after each step.