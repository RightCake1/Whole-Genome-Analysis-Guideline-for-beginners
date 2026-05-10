# Read Mapping and Coverage Analysis

## Using BWA, Samtools, and Bowtie2

Read mapping is a fundamental step in genomic analysis, enabling alignment of sequencing
reads to a reference genome. This process allows downstream applications such as variant
calling, coverage assessment, and assembly validation. This guide demonstrates a standard
workflow using three widely adopted tools: BWA, Samtools, and Bowtie2.

---

## Installation

```bash
# Create and activate environment
conda create -n mapping
conda activate mapping
conda install -c bioconda bwa samtools bowtie2

# Verify installations
bwa
samtools --version
bowtie2 --version
```

---

## Workflow

### Step 1 — Index the Reference Genome

Before mapping, the reference genome needs to be indexed:

```bash
bwa index contigs.fasta
```

### Step 2 — Map Reads to Reference

```bash
bwa mem -t 12 contigs.fasta R1p.fastq R2p.fastq > contigs.sam
```

| Parameter | Description |
|-----------|-------------|
| `-t 12` | Number of threads to use |
| `R1p.fastq` | Forward paired reads |
| `R2p.fastq` | Reverse paired reads |

### Step 3 — Convert and Sort

```bash
# Convert SAM to BAM
samtools view -S -b contigs.sam > contigs.bam

# Sort the alignment
samtools sort contigs.bam --reference contigs.fasta > contigs_sort.bam
```

### Step 4 — Coverage Analysis

```bash
# Basic coverage statistics
samtools coverage contigs_sort.bam

# Detailed per-base coverage saved to file
samtools depth -a contigs_sort.bam > coverage.txt

# Mean read depth
samtools depth -a contigs_sort.bam | \
    awk '{c++;s+=$3}END{print "Mean depth = " s/c}'

# Coverage breadth (percentage of reference covered)
samtools depth -a contigs_sort.bam | \
    awk '{c++; if($3>0) total+=1}END{print (total/c)*100}'

# Coverage at different thresholds
samtools depth -a contigs_sort.bam | \
    awk '{c++; if($3>=10) d10++; if($3>=20) d20++; if($3>=30) d30++}END{
        print ">=10x coverage: " (d10/c)*100 "%"
        print ">=20x coverage: " (d20/c)*100 "%"
        print ">=30x coverage: " (d30/c)*100 "%"
    }'
```

---

## Best Practices

**Resource Management**
- Allocate appropriate thread count based on your machine
- Use sorted BAM files whenever possible
- Index reference genomes once and reuse

**Quality Control**
- Check mapping statistics after each run
- Verify proper pair rates
- Monitor duplicate levels
- Assess coverage uniformity

---

## Common Issues

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| Low mapping rate | Poor read quality or wrong reference | Check read quality, verify reference, consider trimming |
| High duplicate rate | Low library complexity | Consider removing duplicates, assess sequencing depth |
| Uneven coverage | GC bias or library prep issues | Check GC bias, consider PCR-free protocols |

---

## Additional Resources

- [BWA Manual](http://bio-bwa.sourceforge.net/bwa.shtml)
- [Samtools Documentation](http://www.htslib.org/doc/samtools.html)
- [Bowtie2 Manual](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml)
- [SAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)