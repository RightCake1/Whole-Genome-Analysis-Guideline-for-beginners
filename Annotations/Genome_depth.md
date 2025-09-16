# Read Mapping and Coverage Analysis Guide
## Using BWA, Samtools, and Bowtie2

## Introduction
This guide covers the process of mapping sequencing reads to a reference genome and analyzing coverage metrics using BWA, Samtools, and Bowtie2. These tools are essential for various genomic analyses, including variant calling and genome assembly validation.

Read mapping is a fundamental step in genomic analysis, enabling alignment of sequencing reads to a reference genome. This process allows downstream applications such as variant calling, coverage assessment, and assembly validation. This guide demonstrates a standard workflow using three widely adopted tools: BWA, Samtools, and Bowtie2.

## Installation

```bash
# Via conda (recommended)
conda create -n mapping
conda activate mapping
conda install -c bioconda bwa samtools bowtie2
```
```bash
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
```

```bash
# Made SAM file. Code:
bwa mem -t 12 contigs.fasta R1p.fastq R2p.fastq > contigs.sam 
```

```bash
# Converted SAM to BAM. Code:
samtools view -S -b contigs.sam > contigs.bam
```

```bash
# Sorted Alignment. Code:
samtools sort contigs.bam --reference contigs.fasta > contigs_sort.bam
```

```bash
# Checked Mean Read Depth. Code:
samtools depth -a contigs_sort.bam | awk '{c++;s+=$3}END{print s/c}'
```

### 4. Coverage Analysis

```bash
# Basic coverage statistics
samtools coverage contigs_sort.bam
```
```bash
# Detailed per-base coverage
samtools depth -a contigs_sort.bam > coverage.txt
```
```bash
# Mean read depth
samtools depth -a contigs_sort.bam | \
    awk '{c++;s+=$3}END{print "Mean depth = " s/c}'
```
```bash
# Coverage breadth (percentage of reference covered)
samtools depth -a contigs_sort.bam | awk '{c++;s+=$3}END{print s/c}'
```
# OR

```bash
samtools depth -a contigs_sort.bam | awk '{c++; if($3>0) total+=1}END{print (total/c)*100}'
```
```bash
# Coverage at different thresholds
samtools depth -a contigs_sort.bam | \
    awk '{c++; if($3>=10) d10++; if($3>=20) d20++; if($3>=30) d30++}END{
        print "≥10x coverage: " (d10/c)*100 "%"
        print "≥20x coverage: " (d20/c)*100 "%"
        print "≥30x coverage: " (d30/c)*100 "%"
    }'
```
BWA and Bowtie2 provide efficient, high-quality read alignment, while Samtools offers powerful tools for manipulating and analyzing alignments. Together, they form a robust pipeline for read mapping, coverage analysis, and quality control in bacterial genomics.

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