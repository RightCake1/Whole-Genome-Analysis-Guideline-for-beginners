# 16S rRNA Sequence Identification and Extraction

The 16S rRNA gene is found in all bacteria and archaea and changes very slowly over time,
making it act like a unique molecular barcode for each species. This guide covers how to
extract and validate 16S sequences from your genome assembly for use in phylogenetic
analysis and taxonomic classification.

> If you want to build a phylogenetic tree from your 16S sequence after extraction,
> see the [16S Phylogenetic Tree Guide](Identification/16s_rRNA.md).

## What is Barrnap?

Barrnap (Bacterial/Archaeal Ribosomal RNA Predictor) is a fast command-line tool that
scans a bacterial genome assembly and predicts the location of ribosomal RNA genes,
including the 16S, 23S, and 5S rRNA genes. It uses Hidden Markov Models (HMMs) built
from known rRNA sequences to do this accurately and quickly.

For our purposes, the most important output is the 16S rRNA sequence, which is used as
a molecular marker for species identification and phylogenetic analysis.


### Installation

```bash
conda create -n rRNA_tools
conda activate rRNA_tools
conda install -c bioconda barrnap

# Verify
barrnap --version
```

### Basic Usage

```bash
# Simple run — outputs GFF3 and extracts rRNA sequences
barrnap -o rrna.fa < contigs.fa > rrna.gff

# View the extracted 16S sequence
head -n 3 rrna.fa

# Get GFF3 only
barrnap contigs.fasta > output.gff3

# Filter for 16S only
barrnap --kingdom bac contigs.fasta | awk '$3 == "16S_rRNA"' > 16S_locations.gff3
```

### Advanced Options

```bash
barrnap \
    --threads 4 \
    --kingdom bac \
    --lencutoff 0.8 \
    --reject 0.25 \
    --evalue 1e-6 \
    contigs.fasta > detailed_output.gff3
```

| Parameter | Description |
|-----------|-------------|
| `--threads` | Number of CPU threads to use |
| `--kingdom` | Set to `bac` for bacteria, `arc` for archaea |
| `--lencutoff` | Minimum fraction of expected length (default 0.8) |
| `--reject` | Reject sequences below this fraction (default 0.25) |
| `--evalue` | E-value threshold for HMMER search |

### Output Format

Barrnap outputs in GFF3 format, which contains:

```
Sequence Name | Source | Feature Type | Start | End | Score | Strand | Frame | Attributes
```

A typical 16S rRNA sequence should be approximately **1500 bp** in length.

---

## Web-Based Validation Tools

After extracting with Barrnap, use a web tool to confirm your sequence is complete and
high quality — especially recommended for beginners.

### ContEST16S (EzBioCloud)

[ContEST16S](https://www.ezbiocloud.net/tools/contest16s) checks your 16S sequence for
completeness, chimeras (sequences with parts from different organisms), and assigns a
preliminary taxonomic classification.

1. Go to [ezbiocloud.net/tools/contest16s](https://www.ezbiocloud.net/tools/contest16s)
2. Register/login and upload your genome assembly or extracted 16S FASTA
3. Submit and download results including quality metrics and taxonomic assignments

### RNAcentral

[RNAcentral](https://rnacentral.org/) is a comprehensive database of all non-coding RNA
including 16S rRNA. Use it to check your sequence against a massive collection of known
sequences and find related entries.

---

## Multiple Sequence Alignment

If you have 16S sequences from multiple strains, align them before building a
phylogenetic tree:

```bash
# Using MUSCLE
muscle -align 16S_sequences.fasta -out aligned.fasta

# Using MAFFT
mafft --auto 16S_sequences.fasta > aligned.fasta
```

---

## Quality Control Checklist

- Sequence length is approximately 1500 bp
- No chimeric sequences (check with ContEST16S)
- Assembly is complete and uncontaminated
- Correct kingdom setting used in Barrnap (`--kingdom bac` for bacteria)
- Validated with at least one web-based tool

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Fragmented 16S sequence | Check assembly quality — low N50 leads to broken genes |
| No 16S found | Try lowering `--lencutoff` or check if genome is complete |
| Chimeric sequences | Use ContEST16S to detect and flag chimeras |
| Multiple 16S copies | This is normal — pick the longest full-length copy |

---

## Additional Resources

- [Barrnap GitHub](https://github.com/tseemann/barrnap)
- [SILVA rRNA Database](https://www.arb-silva.de/)
- [EzBioCloud](https://www.ezbiocloud.net/)
- [RNAcentral](https://rnacentral.org/)
- [RDP Database](http://rdp.cme.msu.edu/)