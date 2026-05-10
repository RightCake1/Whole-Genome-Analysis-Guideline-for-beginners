# SeqKit: Sequence File Manipulation

SeqKit is a fast, cross-platform toolkit for FASTA/Q file manipulation. This guide covers
the most frequently used commands for basic sequence analysis.

For comprehensive documentation visit the [official SeqKit page](https://bioinf.shenwei.me/seqkit/)
or the detailed [tutorial](https://bioinf.shenwei.me/seqkit/tutorial/).

---

## Installation

```bash
# Via conda (recommended)
conda install -c bioconda seqkit

# Via homebrew
brew install seqkit
```

---

## File Inspection

```bash
# View sequence file content
cat contigs.fasta

# Quick peek at first few sequences
head contigs.fasta
```

---

## Sequence Statistics

```bash
# Stats for a single file
seqkit stat contigs.fasta

# Stats for multiple files with additional info
seqkit stats *.f{a,q}.gz -a
```

Output includes: file format, sequence count, total length, min/avg/max length, and GC content.

---

## Sequence Manipulation

```bash
# Sort by length — longest to shortest
seqkit sort --by-length contigs.fasta > sorted.fasta

# Sort by length — shortest to longest
seqkit sort --by-length --reverse contigs.fasta > sorted_reverse.fasta

# Split multi-FASTA into separate files
seqkit split -i contigs.fasta

# Split by size (e.g., 1000 sequences per file)
seqkit split -s 1000 contigs.fasta
```

---

## Sequence Extraction

```bash
# First 12 bases
seqkit subseq -r 1:12 contigs.fasta > first12.fasta

# Last 12 bases
seqkit subseq -r -12:-1 contigs.fasta > last12.fasta

# Remove first and last 12 bases
seqkit subseq -r 13:-13 contigs.fasta > trimmed.fasta
```

---

## Format Conversion

```bash
# FASTA to tabular format
seqkit fx2tab contigs.fasta > output.tab

# Tabular to FASTA format
seqkit tab2fx input.tab > output.fasta
```

---

## Useful Flags

| Flag | Description |
|------|-------------|
| `-j` | Number of threads for faster processing |
| `-v` | Verbose output |
| `-o` | Output file |
| `-w` | Line width for FASTA format (default: 60) |

---

## Best Practices

- Always run `seqkit stats` before and after operations to verify sequence counts
- Use `-j` to enable multiple threads for large files
- Check output with `head` or `less` after each operation
- Use compressed files (`.gz`) to save disk space

---

## Additional Resources

- [SeqKit Official Documentation](https://bioinf.shenwei.me/seqkit/)
- [SeqKit Tutorial](https://bioinf.shenwei.me/seqkit/tutorial/)