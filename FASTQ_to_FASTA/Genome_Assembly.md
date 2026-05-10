# Genome Assembly with SPAdes

SPAdes (St. Petersburg Genome Assembler) is a sophisticated de novo genome assembly tool
designed to take raw short reads (like those from Illumina) and piece them together to
reconstruct a complete or near-complete genome sequence — without needing a reference genome.

---

## How does genome assembly work?

Imagine you have a huge book, but every page has been shredded into millions of tiny,
overlapping paper scraps. Your job is to put the book back together without an original
copy to guide you. In bioinformatics, this "book" is a genome and the "scraps" are the
sequencing reads. SPAdes solves this puzzle using complex algorithms called de Bruijn graphs.

| | SPAdes | seqtk |
|--|--------|-------|
| **Purpose** | Assembles a genome from scratch | Converts file formats |
| **Input** | Raw FASTQ reads | Existing FASTQ file |
| **Output** | FASTA contigs and scaffolds | FASTA with quality scores removed |
| **Complexity** | High — requires significant RAM and CPU | Minimal resources |

---

## Installation

```bash
# Option 1 — apt install
sudo apt install spades

# Option 2 — download directly
wget https://github.com/ablab/spades/releases/download/v3.15.5/SPAdes-3.15.5-Linux.tar.gz
tar -xzf SPAdes-3.15.5-Linux.tar.gz
cd SPAdes-3.15.5-Linux/bin/

# Verify installation
spades.py --version
```

---

## Before You Assemble

Always clean your reads before assembly. Raw reads contain low-quality bases and adapter
sequences that can cause errors and create false contigs, leading to a fragmented and
inaccurate final genome. See the [FASTQ Processing Guide](FASTQ_to_FASTA/FASTQ_processing.md)
for how to do this.

---

## Assembly Commands

### Basic Paired-End Assembly

```bash
spades.py \
    -1 forward_reads.fastq \
    -2 reverse_reads.fastq \
    -o spades_output
```

### Careful Mode (Recommended for Bacterial Genomes)

The `--careful` flag adds an extra step that reduces mismatches and indels in the final
assembly. Always use this for bacterial genomes:

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
spades.py \
    -1 forward_reads.fastq \
    -2 reverse_reads.fastq \
    --careful \
    --cov-cutoff auto \
    --trusted-contigs reference.fasta \
    -o reference_guided_assembly
```

**Key parameters:**

| Parameter | Description |
|-----------|-------------|
| `-1` | Forward reads file |
| `-2` | Reverse reads file |
| `-o` | Output directory |
| `--careful` | Reduces mismatches and indels (recommended) |
| `--cov-cutoff auto` | Automatically filters low-coverage contigs |
| `--trusted-contigs` | Reference contigs to guide assembly |

> The SPAdes run can take anywhere from minutes to hours depending on genome size and
> your computer's resources. It will print its progress to the terminal.

---

## Converting FASTQ to FASTA with seqtk

If you don't need a full assembly and just want to convert your cleaned FASTQ files to
FASTA format, use seqtk:

```bash
# Install
sudo apt install seqtk

# Convert forward reads
seqtk seq -a trimmed/R1P.fastq > final_output/R1.fasta

# Convert reverse reads
seqtk seq -a trimmed/R2P.fastq > final_output/R2.fasta
```

The `-a` flag tells seqtk to output FASTA format. The `>` redirects the output into a
new file.

---

## fastp for QC and Trimming

fastp is a fast all-in-one quality control and trimming tool that automatically detects
and removes adapters:

```bash
# Install
conda install -c bioconda fastp

# Run on paired reads
fastp \
    -i raw_data/forward_reads.fastq.gz \
    -o trimmed/forward_reads.fastq.gz \
    -I raw_data/reverse_reads.fastq.gz \
    -O trimmed/reverse_reads.fastq.gz
```

---

## Alternative Assembly Options

If you prefer not to use the command line, these web-based platforms offer genome
assembly with a graphical interface:

**BV-BRC** — [bv-brc.org](https://www.bv-brc.org/)
- Supports multiple assembly algorithms
- Provides quality assessment tools
- Enables comparative analysis

**KBase** — [kbase.us](https://www.kbase.us/)
- Upload your files and run the assembly app directly in the browser

**Snakemake Pipeline** — for automated high-throughput assemblies:
- [De Novo Assembly Pipeline](https://github.com/Lagator-Group/De-Novo-Plasmid-Assembly-and-Annotation-Snakemake)

---

## Best Practices

- Always quality-check and trim reads before assembly
- Use `--careful` for bacterial genomes
- Allocate sufficient memory — SPAdes is RAM-intensive
- Validate your assembly with QUAST, BBMap, or BUSCO after completion

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Insufficient memory | Increase `--memory` parameter |
| Long runtime | Check input read quality, reduce dataset size for testing |
| Failed error correction | Try `--only-assembler` to skip error correction |

---

## Additional Resources

- [SPAdes GitHub](https://github.com/ablab/spades)
- [SPAdes Manual](http://cab.spbu.ru/files/release3.15.5/manual.html)
- [fastp GitHub](https://github.com/OpenGene/fastp)
- [QUAST](http://quast.sourceforge.net/)
- [BUSCO](https://busco.ezlab.org/)