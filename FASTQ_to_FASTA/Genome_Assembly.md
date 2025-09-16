# SPAdes Genome Assembly Guide

## Introduction
In this guide, I'll walk you through using SPAdes (St. Petersburg genome assembler) for genome assembly. SPAdes is a fantastic toolkit, especially for assembling bacterial genomes.  

SPAdes (St. Petersburg Genome Assembler)
SPAdes is a sophisticated genome assembly tool designed for de novo assembly of DNA sequencing reads. Its primary function is to take raw, short reads (like those from Illumina) and piece them together to reconstruct a complete, or near-complete, genome sequence without a reference genome.

Function: Assembles a genome. It identifies overlapping regions between millions of short DNA fragments and connects them to build longer, continuous sequences called contigs.

Input: Requires raw FASTQ reads.

Output: Generates a FASTA file containing assembled contigs and scaffolds. This is the new, longer genomic sequence.

Complexity: It uses complex algorithms, including de Bruijn graphs, to solve the "genome puzzle." It requires significant computational resources (RAM and CPU).

Purpose: To create a new genome sequence from scratch.

Using SPAdes for genome assembly is an essential step in bioinformatics for reconstructing a complete genome from short DNA reads. While tools like seqtk are useful for simple file conversions, SPAdes performs the complex task of piecing together millions of tiny fragments into a coherent, much longer sequence, a process called de novo assembly.

Imagine you have a huge book, but every page has been shredded into millions of tiny, overlapping paper scraps. Your job is to put the book back together without an original copy to guide you. In bioinformatics, this "book" is a genome, and the "scraps" are the sequencing reads. Genome assembly is the process of using powerful algorithms to solve this puzzle and reconstruct the original sequence.

## Installation

Before you run SPAdes, you need a clean workspace and your data ready (the trimmmed .fastq R1 and R2 seqeunces).

SPAdes is a standalone program, so you don't need conda for a basic install.

Open your terminal.

Download the latest SPAdes release. (Note: The version in the original prompt is old. It's best to use the most recent one).

```Bash
# Use a tool like wget or a browser to get the latest version
# The command below is a placeholder, find the latest on the SPAdes GitHub
wget https://github.com/ablab/spades/releases/download/v3.15.5/SPAdes-3.15.5-Linux.tar.gz
Extract the downloaded file.
```

```Bash
tar -xzf SPAdes-3.15.5-Linux.tar.gz
Navigate into the new SPAdes directory.
``` 

```Bash
cd SPAdes-3.15.5-Linux/bin/ #try using the latest version
Check that the installation works by verifying the version.
```

```bash
./spades.py --version
You will likely need to use ./spades.py to run the command, as the program isn't in your system's PATH by default.
```
Or or just run this in one go: 

```bash
wget https://github.com/ablab/spades/releases/download/v4.0.0/SPAdes-4.0.0-Linux.tar.gz
tar -xzf SPAdes-4.0.0-Linux.tar.gz
cd SPAdes-4.0.0-Linux/bin/
```

```bash
# Verify installation
spades.py --version
```

## Basic Assembly Commands

High-quality input reads are the key to a good assembly. You should always clean your reads before assembly.

Raw reads from a sequencer contain low-quality bases at the ends and artificial sequences called adapters (small fragments used during sequencing). If you don't remove them, they can cause errors and create false "contigs" (assembled sequences), leading to a fragmented and inaccurate final genome.

fastp is a highly recommended tool for quality control and trimming. You can easily install it using conda.

```Bash
# Install fastp if you don't have it
conda install -c bioconda fastp
```
```bash
# Navigate back to your main project folder
cd ../../
```
# Run fastp on your raw reads
```bash
fastp -i raw_data/forward_reads.fastq.gz -o trimmed/forward_reads.fastq.gz \
-I raw_data/reverse_reads.fastq.gz -O trimmed/reverse_reads.fastq.gz
```

This command automatically detects and removes adapters and low-quality bases. Your clean, ready-to-use files are now in the trimmed folder.

### De Novo Assembly with Paired Reads

The SPAdes run can take a long time, from minutes to hours, depending on the genome size and your computer's power. It will print its progress to the terminal.

The Basic Command
Use the spades.py script to run the assembly. The key parameters are:

-1: Specifies the forward reads file.
-2: Specifies the reverse reads file.
-o: Specifies the output directory.

```bash
# Basic paired-end assembly
# Navigate to the SPAdes folder or move spades.py to your trimmmed sequence folder.
spades.py \
    -1 forward_reads.fastq \
    -2 reverse_reads.fastq \
    -o spades_output
```

For better accuracy, especially with bacterial genomes, it's highly recommended to use the --careful flag. This option adds an extra step that helps reduce mismatches and indels (insertions/deletions) in the final assembly.

# Careful mode (recommended for bacterial genomes)
```bash
spades.py \
    -1 forward_reads.fastq \
    -2 reverse_reads.fastq \
    --careful \
    --cov-cutoff auto \
    -o spades_assembly_careful
```

### Reference-Guided Assembly
```bash
# Assembly with trusted reference contigs
spades.py \
    -1 forward_reads.fastq \
    -2 reverse_reads.fastq \
    --careful \
    --cov-cutoff auto \
    --trusted-contigs reference.fasta \
    -o reference_guided_assembly
```

Converting to FASTA with seqtk
You may have heard of seqtk for converting file formats. While SPAdes already outputs a FASTA file, you might use seqtk for other tasks, like converting your initial FASTQ reads to FASTA if that's all you need. 

# seqtk is a lightweight, general-purpose command-line toolkit for processing and converting sequence files. Its functions are much simpler and faster than SPAdes.

5. Alternative Assembly Methods and Automation
While running SPAdes from the command line is powerful, there are other options for different needs.

Function: Manipulates sequence files. One of its many functions is converting a FASTQ file to a FASTA file by simply removing the quality scores.

Input: Requires an existing FASTQ file.

Output: Generates a FASTA file containing the same exact sequences as the input, just without the quality information. It does not assemble or alter the sequence order.

Complexity: It's a simple, fast utility. It requires minimal computational resources.

Purpose: To quickly format and process sequence files for various downstream applications that don't need quality information. 

ou will convert your clean FASTQ files into FASTA format, which is much simpler and only contains the sequence data. We'll use the seqtk command-line tool.

Make sure you're in your main project folder.

Use the seqtk command to convert your trimmed, paired reads.

```bash
# Convert R1 (forward reads)
seqtk seq -a trimmed/R1P.fastq > final_output/R1.fasta
# Convert R2 (reverse reads)
seqtk seq -a trimmed/R2P.fastq > final_output/R2.fasta
```

-a: An option that tells seqtk to output the file in FASTA format.

>: A redirect command that sends the output of the command into a new file.

You now have a clean, ready-to-use FASTA file containing only the high-quality sequences from your original data. Good job!

# Why is SPAdes better for assembly? Because seqtk only removes quality scores and metadata; it doesn't have the sophisticated algorithms to align overlapping reads and build a new, longer sequence. SPAdes is a powerful assembler, not just a simple converter.
## Alternative Assembly Options

5. Alternative Assembly Methods and Automation
While running SPAdes from the command line is powerful, there are other options for different needs.

### Web-Based Assembly
The Bacterial and Viral Bioinformatics Resource Center (BV-BRC) offers web-based assembly:
- URL: https://www.bv-brc.org/
- Supports multiple assembly algorithms
- Provides quality assessment tools
- Enables comparative analysis

### Automation with Snakemake
For high-throughput or repetitive assemblies:
- [Assembly Pipeline Repository](https://github.com/Lagator-Group/De-Novo-Plasmid-Assembly-and-Annotation-Snakemake)
- Automates assembly workflow
- Ensures reproducibility
- Handles multiple samples efficiently

### Kbase 
- Link: https://www.kbase.us/
- Just upload your files here and run the app

## Best Practices

1. Quality Control
   - Always check input read quality
   - Use --careful for better accuracy
   - Monitor coverage distribution

2. Resource Management
   - Allocate sufficient memory
   - Use appropriate thread count
   - Monitor disk space

3. Output Validation
   - Check assembly statistics
   - Verify contig lengths
   - Assess coverage uniformity

## Troubleshooting Tips

1. Common Issues
   - Insufficient memory: Increase --memory parameter
   - Long runtime: Check input quality
   - Failed error correction: Try --only-assembler

2. Quality Checks
   - Use QUAST for assembly evaluation
   - Check coverage with BBMap
   - Validate completeness with BUSCO

## Additional Resources

- [SPAdes GitHub Repository](https://github.com/ablab/spades)
- [SPAdes Manual](http://cab.spbu.ru/files/release3.15.5/manual.html)
- [Tutorial](http://sepsis-omics.github.io/tutorials/modules/spades_cmdline/)
- [fastp](https://github.com/OpenGene/fastp)

---
**Note**: This guide covers basic usage. For advanced features and detailed parameters, consult the [official documentation](https://github.com/ablab/spades).