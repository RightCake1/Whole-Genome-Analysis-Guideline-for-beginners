# Mobile Genetic Elements (MGEs) Analysis Guide

Mobile Genetic Elements (MGEs) are segments of DNA that can move within or between genomes.
They are a primary driver of bacterial evolution, carrying genes for traits like antibiotic
resistance and virulence. This guide covers identification and analysis of the most common
MGEs — plasmids, prophages, insertion sequences, and CRISPR arrays.

---

## What are MGEs?

| MGE Type | Description |
|----------|-------------|
| **Plasmids** | Circular DNA elements that replicate independently of the chromosome |
| **Prophages** | Bacteriophages integrated into the bacterial chromosome |
| **Insertion Sequences (IS)** | The simplest MGEs, often involved in horizontal gene transfer |
| **CRISPR arrays** | Bacterial immune system elements that record past phage infections |

---

## Web-Based Tools

Web-based tools are ideal for quick initial analyses of single genomes — no installation
required.

---

### CGE Tools (Center for Genomic Epidemiology)

[genomicepidemiology.org](https://www.genomicepidemiology.org/) hosts several tools
including PlasmidFinder, ResFinder, VirulenceFinder, and MGE Finder.

**Usage:**
1. Visit the website and select the appropriate tool
2. Upload your FASTA file (max 20 MB)
3. Set minimum identity (90% default) and minimum coverage (60% default)
4. Submit and download results in JSON, TSV, or PDF format

---

### PlasmidFinder

[PlasmidFinder](https://cge.food.dtu.dk/services/plasmidfinder/) is perfect for a rapid
check for known plasmid replicon types.

**Usage:**
1. Upload your FASTA file
2. Select database (Enterobacteriaceae, Enterococcus, or Staphylococcus)
3. Set identity threshold (95% default) and minimum coverage (60% default)
4. Submit and download results

---

### PHASTER

[PHASTER](https://phaster.ca/) is the go-to tool for finding prophages — bacteriophages
integrated into a bacterial chromosome. It classifies prophage regions as intact,
questionable, or incomplete.

**Usage:**
1. Go to [phaster.ca](https://phaster.ca/)
2. Upload a FASTA file, paste a sequence, or provide an NCBI accession number
3. Submit your job and monitor progress
4. Download results including a summary table, detailed annotations, and genome viewer

---

### IS-finder

[IS-finder](https://isfinder.biotoul.fr/) is a specialized database for detecting
insertion sequences by BLASTing your genome against a curated collection of IS elements.

**Usage:**
1. Go to the IS-finder BLAST page
2. Upload your sequence in FASTA format
3. Select BLAST program — BLASTN for nucleotide, BLASTX for protein
4. Set E-value threshold to 1e-10 (recommended)
5. Submit and export the results table

---

### Proksee

[Proksee](https://proksee.ca/) is an integrated platform for multiple analyses including
HGT region detection and CRISPR arrays, with a built-in genome visualizer.

**Usage:**
1. Register and create a new project
2. Upload your genome file
3. Select tools:
   - **Alien Hunter** — for horizontal gene transfer (HGT) detection
   - **CRISPR-Cas++** — for CRISPR array detection
4. Run analysis and view or download results

---

## Command-Line Tools

For plasmid analysis with MOB-suite and Platon, see the detailed
[Plasmid Analysis Guide](Mobile_genetic_elements/Plasmid.md).

---

## Recommended Workflow

**Step 1 — Start with web tools for a quick overview:**
- PHASTER → prophage detection
- PlasmidFinder → plasmid replicon typing
- IS-finder → insertion sequence detection
- Proksee → HGT regions and CRISPR arrays

**Step 2 — Follow up with command-line tools for batch processing:**
- MOB-suite → detailed plasmid mobility and typing
- Platon → plasmid contig verification
- ABRicate with `--db vfdb` → virulence gene screening

---

## Best Practices

- Use a minimum contig length of 1000 bp for reliable MGE detection
- Aim for assembly N50 > 50 kb and sequencing coverage > 30x before analysis
- Always cross-validate findings between at least two tools
- Check for overlapping predictions between prophage and plasmid tools
- Compare results with closely related reference genomes

---

## Additional Resources

- [CGE Tools](https://www.genomicepidemiology.org/)
- [PHASTER](https://phaster.ca/)
- [IS-finder](https://isfinder.biotoul.fr/)
- [Proksee](https://proksee.ca/)
- [PlasmidFinder](https://cge.food.dtu.dk/services/plasmidfinder/)
- [MOB-suite GitHub](https://github.com/phac-nml/mob-suite)