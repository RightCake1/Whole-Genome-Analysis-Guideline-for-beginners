# 16S rRNA Phylogenetic Tree Analysis

The 16S rRNA gene is the most widely used marker for bacterial and archaeal classification.
Because it is present in all bacteria, highly conserved, and contains both conserved and
variable regions, it serves as a reliable "molecular clock" for determining evolutionary
relationships between organisms.

---

## Core Workflow

**Extract 16S sequence → BLAST for relatives → Align sequences → Build tree → Visualize**

---

## Tools Needed

| Tool | Purpose | Type |
|------|---------|------|
| [Barrnap](https://github.com/tseemann/barrnap) | Extract 16S rRNA from genome | Command-line |
| [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/) | Find related sequences | Web |
| [MEGA11](https://www.megasoftware.net/) | Alignment and tree construction | Desktop app |
| [iTOL](https://itol.embl.de/) | Tree visualization | Web |

---

## Step 1 — Extract 16S rRNA Sequence with Barrnap

Barrnap predicts ribosomal RNA sequences directly from your genome FASTA file:

```bash
# Install
conda install -c bioconda barrnap

# Run on your genome
barrnap --kingdom bac your_genome.fasta > rrna.gff
```

This produces a GFF file with the locations of all rRNA sequences. Use this to extract
the 16S sequence specifically for downstream analysis.

---

## Step 2 — Find Related Sequences with NCBI BLAST

1. Go to [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) and select **Blastn**
2. Paste your 16S sequence and run the search
3. From the results, select the top hits from closely related organisms
4. Download the aligned sequences in FASTA format
5. Save the CSV results for record-keeping

---

## Step 3 — Prepare Your Sequence File

Create a FASTA file combining your sequence with the downloaded BLAST hits. Use a
consistent, descriptive naming format:

```
>Organism_Name_Location_Year
ACTGCTAGCTAGCTAGCTAGCTAGCTAGCTAG
```

---

## Step 4 — Align Sequences in MEGA11

1. Download and install MEGA11 from [megasoftware.net](https://www.megasoftware.net/)
2. Click **Align → Build New Alignment**
3. Select **DNA** as the sequence type
4. Import your sequences with `Ctrl+D`
5. Run alignment using the **MUSCLE** algorithm
6. Review the alignment — look for obvious gaps or misalignments
7. Save in MEGA format (`.meg`)

---

## Step 5 — Build the Phylogenetic Tree

1. In MEGA11, click **Phylogeny**
2. Choose your tree construction method:
   - **Neighbor-Joining** — fast, good for large datasets
   - **Maximum Likelihood** — more accurate, recommended for publication
   - **UPGMA** — for rooted trees
3. Set bootstrap replicates to **1000** for statistical support
4. Run and save the tree file in Newick format

---

## Step 6 — Visualize with iTOL

1. Go to [itol.embl.de](https://itol.embl.de/)
2. Upload your Newick tree file
3. Customize the visualization:
   - Color branches by taxonomy
   - Add labels and bootstrap values
   - Adjust layout (circular, rectangular, etc.)
4. Export in PNG, SVG, or PDF for publication

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No 16S found by Barrnap | Check genome quality and completeness |
| Poor BLAST hits | Try relaxing E-value threshold or search a broader database |
| Misaligned sequences | Manually inspect and trim poorly aligned ends in MEGA11 |
| Tree looks unresolved | Increase bootstrap replicates or try a different tree method |

---

## Additional Resources

- [Video Tutorial — 16S Phylogenetic Tree](https://www.youtube.com/watch?v=7GAYLbiyLuw)
- [MEGA11 Documentation](https://www.megasoftware.net/web_help)
- [iTOL User Guide](https://itol.embl.de/help.cgi)
- [Barrnap GitHub](https://github.com/tseemann/barrnap)