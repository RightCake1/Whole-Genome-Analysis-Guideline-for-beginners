# Multi-Locus Sequence Typing (MLST)

MLST assigns a Sequence Type (ST) to a bacterial isolate based on the allelic combination
of typically 7 conserved housekeeping genes. Each unique combination of alleles corresponds
to a distinct ST, making it a powerful tool for outbreak investigation, epidemiology, and
tracking the spread of bacterial lineages.

There are two complementary public databases that assign new STs and collect isolate
information:

- [PubMLST](https://pubmlst.org/)
- [BIGSdb-Pasteur](https://bigsdb.pasteur.fr/)

---

## Installation

```bash
conda install -c conda-forge -c bioconda -c defaults mlst

# Verify
mlst --version
```

---

## Usage

The tool takes an assembled genome in FASTA format, automatically detects the most likely
bacterial species, and assigns an ST:

```bash
# Single genome
mlst assembly.fasta

# Multiple genomes
mlst *.fasta

# Force a specific scheme
mlst --scheme klebsiella assembly.fasta

# List all available schemes
mlst --list
```

---

## Output

The output is a tab-delimited line containing:

```
filename    scheme    ST    gene1    gene2    gene3    gene4    gene5    gene6    gene7
```

---

## Understanding Missing or Novel Results

Missing or incomplete results do not mean an error occurred. MLST attempts to tell you
as much as possible about what it found using the following notation:

| Symbol | Meaning | Length | Identity |
|--------|---------|--------|----------|
| `n` | Exact intact allele | 100% | 100% |
| `~n` | Novel full-length allele similar to n | 100% | ≥ `--minid` |
| `n?` | Partial match to known allele | ≥ `--mincov` | ≥ `--minid` |
| `-` | Allele missing | < `--mincov` | < `--minid` |
| `n,m` | Multiple alleles found | — | — |

If you get a confirmed ST number, it's a confident match. If it's labeled as a new ST,
you can submit it to PubMLST or BIGSdb-Pasteur for official assignment.

---

## Updating the Database

New allele profiles and STs are identified every year. It is good practice to update
the database every 6–12 months:

```bash
# Find where mlst is installed
which mlst

# Go into the scripts folder
cd /home/user/sw/mlst/scripts

# Download the latest database
./mlst-download_pub_mlst | bash

# Verify the download
find pubmlst | less

# Backup the old database
mv ../db/pubmlst ../db/pubmlst.old

# Move the new database into place
mv ./pubmlst ../db/

# Regenerate the BLAST database
./mlst-make_blast_db

# Confirm schemes are installed
../bin/mlst --list
```

---

## Best Practices

- Always verify genome assembly quality before running MLST — a contaminated assembly
  can cause wrong allele identification or the wrong scheme being selected
- If you get an unexpected scheme, check your assembly for contamination with a tool
  like Kraken2 or CheckM
- Update your database regularly to avoid missing newly discovered STs

---

## Additional Resources

- [MLST GitHub](https://github.com/tseemann/mlst)
- [PubMLST Organism List](https://pubmlst.org/organisms)
- [BIGSdb-Pasteur](https://bigsdb.pasteur.fr/)