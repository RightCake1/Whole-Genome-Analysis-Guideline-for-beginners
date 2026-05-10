# Bacterial Species Identification and Characterization

When a bacterial genome is sequenced, you need to analyze it to answer three key questions:

- **What is it?** — Species and strain identification
- **What can it do?** — Virulence and antimicrobial resistance
- **Where does it come from?** — Population structure and epidemiology

This guide covers the best tools for each of these questions.

---

## Recommended Workflow

**KmerFinder** (quick species ID) → **PubMLST** (confirm + ST) → **PathogenWatch** (full characterization) → **Species-specific tool** if applicable

---

## 1. KmerFinder — Quick Species Identification

[KmerFinder](https://cge.cbs.dtu.dk/services/KmerFinder/) uses k-mers (short DNA sequences)
to rapidly match your genome against a known species database. Use this first for a fast
initial identification.

**Usage:**
1. Upload your FASTA file
2. Select database (Bacteria or Fungi)
3. Submit and review the species prediction, confidence score, and template coverage

---

## 2. PubMLST — Species Confirmation and Sequence Typing

[PubMLST](https://pubmlst.org/) confirms your species and assigns a Sequence Type (ST)
by analyzing conserved housekeeping genes. Use this to confirm KmerFinder results and
get a detailed genetic profile.

**Usage:**
1. Navigate to the Species ID section
2. Upload your FASTA file and select the appropriate scheme
3. Review the ST, allelic profiles, and population structure data

> For a dedicated MLST command-line guide, see the
> [MLST page](Identification/Multi_Locus_Sequence_Type.md).

---

## 3. PathogenWatch — Full Genomic Characterization

[PathogenWatch](https://pathogen.watch/) is an integrated platform that provides species
identification, AMR prediction, virulence factors, plasmid replicons, and phylogenetic
placement — all in one place.

**Usage:**
1. Create an account and upload your genome assembly
2. Review the results:

| Output | What it means |
|--------|--------------|
| **AMR Genes** | Antibiotic resistance genes found and predicted resistances |
| **Virulence Factors** | Genes that enable the bacterium to cause disease |
| **Phylogenetic Placement** | Where your strain sits among thousands of global strains |
| **MLST** | Sequence type assignment |

PathogenWatch is particularly useful for outbreak detection and global surveillance
because it places your strain in the context of thousands of other isolates worldwide.

---

## 4. Kleborate — Specialized Tool for *Klebsiella* species only

If your organism is identified as *Klebsiella*, use [Kleborate](https://kleborate.readthedocs.io/)
for a much more detailed characterization than general tools provide.

### Installation

```bash
# Via conda (recommended)
conda create -n kleborate
conda activate kleborate
conda install -c bioconda kleborate

# Via pip
pip install kleborate
```

### Usage

```bash
# Single genome
kleborate -a contigs.fasta -o output.csv

# Multiple genomes
kleborate -a *.fasta -o batch_output.txt

# Full analysis with resistance, virulence, and capsule typing
kleborate \
    -a contigs.fasta \
    --resistance \
    --virulence \
    --kaptive_k \
    --kaptive_o \
    -o detailed_output.txt
```

### What Kleborate detects

- Species identification and MLST
- Resistance genes and virulence factors
- Capsule typing (K locus) and O antigen typing
- Hypervirulence determinants
- Mobile genetic elements

---

## 5. StaphSCAN — Specialized Tool for *Staphylococcus aureus* only

If your organism is *Staphylococcus aureus*, use [StaphSCAN](https://github.com/riccabolla/StaphSCAN)
for detailed characterization.

### Installation

```bash
# Via conda
conda create -n staphscan -c bioconda staphscan -y
conda activate staphscan
```

### Usage

```bash
# Single genome
staphscan -i genome.fasta -o staphscan_output

# Multiple genomes
staphscan -i *.fasta -o staphscan_output
```

### What StaphSCAN detects

- Species identification and MLST
- SCCmec typing, spa typing, agr typing
- Resistance and virulence genes
- Biofilm genes and capsule typing

---

## Best Practices

- Always start with KmerFinder for a rapid initial ID before running heavier tools
- Cross-validate species predictions across at least two tools
- Check assembly quality before submission — contaminated assemblies cause wrong results
- Use species-specific tools (Kleborate, StaphSCAN) when applicable for much richer output
- Keep track of database versions used for reproducibility

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Discordant species results between tools | Check assembly quality and coverage, consider contamination |
| Low confidence calls | Increase sequencing depth or improve assembly |
| Wrong MLST scheme selected | Let the tool auto-detect, or verify species first with KmerFinder |
| No ST assigned | May be a novel ST — check allele-level output and submit to PubMLST |

---

## Additional Resources

- [CGE Tools](https://cge.cbs.dtu.dk/services/)
- [NCBI Pathogen Detection](https://www.ncbi.nlm.nih.gov/pathogens/)
- [Kleborate Documentation](https://kleborate.readthedocs.io/en/latest/)
- [StaphSCAN GitHub](https://github.com/riccabolla/StaphSCAN)
- [BacWGSTdb](http://bacdb.org/BacWGSTdb/)