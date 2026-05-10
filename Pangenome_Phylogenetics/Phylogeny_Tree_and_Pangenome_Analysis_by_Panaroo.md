# Pangenome Analysis with Panaroo and IQ-TREE2


## What is Panaroo?

Panaroo is a pangenome pipeline that uses a graph-based approach to identify and correct
errors that arise during genome annotation before computing the pangenome. This makes it
significantly more accurate than Roary when working with draft assemblies or genomes of
varying quality, because it can distinguish between real biological variation and
annotation artifacts.

## What is trimAl?

trimAl is a tool for automated alignment trimming. Before building a phylogenetic tree,
your core gene alignment will inevitably contain poorly aligned regions, gaps, and columns
with too much missing data. These noisy regions can introduce errors into your tree and
reduce its accuracy.

trimAl scans the alignment and removes these problematic columns while keeping the
informative ones. The `-automated1` flag automatically selects the best trimming method
based on the characteristics of your specific alignment, making it a reliable choice for
most datasets.

> Trimming is a small but important step — a cleaner alignment almost always produces
> a better tree.
## What is IQ-TREE2?

IQ-TREE2 is a maximum likelihood phylogenetic tree builder. Unlike FastTree which uses
approximations, IQ-TREE2 automatically selects the best-fit substitution model for your
data and uses ultrafast bootstrap (UFBoot) to generate reliable branch support values.
This makes it the preferred tool for producing publication-quality phylogenetic trees.

---

## Prerequisites

Before starting, annotate your FASTA files with Prokka or Bakta to get `.gff` files.
See [How to run Prokka](../Annotations/Genome_Annotaions.md).

---

## Installation

```bash
conda create -n panaroo -c bioconda -c conda-forge panaroo iqtree trimal -y
conda activate panaroo

# Verify
panaroo --version
iqtree2 --version
trimal --version
```

---

## Step 1 — Create Working Directories

```bash
cd /home/
mkdir -p panaroo_input panaroo_out
```

---

## Step 2 — Collect All `.gff` Files

Copy all `.gff` files from your Prokka annotation subfolders into one place:

```bash
find /home/Annotations -name "*.gff" -exec cp {} panaroo_input/ \;
```

Verify the count matches your expected number of genomes:

```bash
ls panaroo_input/*.gff | wc -l
```

> ⚠️ If the count doesn't match your total number of genomes, stop and investigate
> before continuing.

---

## Step 2.1 — Check File Names (Critical)

Panaroo is sensitive to messy filenames. Check your files:

```bash
ls panaroo_input/
```

Make sure:
- ❌ No spaces in filenames
- ❌ No special characters (`(`, `)`, `&`, etc.)
- ✅ Short clean names like `Kp_001.gff`

If you need to batch rename your files, this command strips spaces and replaces them
with underscores:

```bash
for f in panaroo_input/*.gff; do
    mv "$f" "${f// /_}"
done
```

---

## Step 3 — Run Panaroo

```bash
panaroo \
    -i panaroo_input/*.gff \
    -o panaroo_out \
    --clean-mode moderate \
    --remove-invalid-genes \
    --core_threshold 0.95 \
    --refind-mode off \
    -t 8 \
    -a core \
    > logs/panaroo.log 2>&1 &
```

**Parameter explanations:**

| Parameter | Description |
|-----------|-------------|
| `-i` | Input GFF files |
| `-o` | Output directory |
| `--clean-mode moderate` | Balanced error correction — use `strict` for high-quality assemblies or `sensitive` for more fragmented ones |
| `--remove-invalid-genes` | Removes genes that don't meet basic quality criteria |
| `--core_threshold 0.95` | Genes present in ≥95% of genomes are considered core |
| `--refind-mode off` | Disables re-finding of missing genes (faster) |
| `-t` | Number of threads. Change according to you system|
| `-a core` | Generate core gene alignment |

> Don't worry if the progress shows `0/101` or a number that doesn't match your total.
> Panaroo processes genomes in batches internally — it will still complete all of them.
> The more files you have, the more time it takes.


---

## Step 4 — Trim the Alignment with trimAl

Before building the tree, trim poorly aligned columns from the core gene alignment:

```bash
cd /home/rightcake/Fida_thesis/panaroo_out

trimal \
    -in core_gene_alignment.aln \
    -out core_gene_alignment_trimmed.aln \
    -automated1
```

`-automated1` automatically selects the best trimming method based on your alignment.

---

## Step 5 — Build Phylogenetic Tree with IQ-TREE2

```bash
nohup iqtree2 \
    -s panaroo_out/core_gene_alignment_trimmed.aln \
    -m GTR+G \
    --ufboot 1000 \
    --mem 4G \
    -T 2 \
    --safe \
    --redo \
    > logs/iqtree_run.log 2>&1 &
```

**Parameter explanations:**

| Parameter | Description |
|-----------|-------------|
| `-s` | Input alignment file |
| `-m GTR+G` | Substitution model — GTR+G is a reliable choice for bacterial core genomes |
| `--ufboot 1000` | Ultrafast bootstrap with 1000 replicates for branch support values |
| `--mem 4G` | Maximum RAM to use |
| `-T` | Number of threads |
| `--safe` | Safer likelihood calculation — recommended for large datasets |
| `--redo` | Overwrites previous results if rerunning |
| `nohup ... &` | Runs the job in the background so it continues even if you close the terminal |

Monitor progress:

```bash
tail -f logs/iqtree_run.log
```

---

## Output Files

| File | Description |
|------|-------------|
| `panaroo_out/core_gene_alignment.aln` | Core gene alignment |
| `panaroo_out/gene_presence_absence.csv` | Presence/absence matrix |
| `panaroo_out/pan_genome_reference.fa` | All pan-genome sequences |
| `*.treefile` | Final phylogenetic tree in Newick format |
| `*.iqtree` | Detailed IQ-TREE2 log with model information |
| `*.contree` | Consensus tree with bootstrap values |

---

## Visualizing the Tree

Your `.treefile` output can be visualized with:

- [iTOL](https://itol.embl.de/) — web-based, publication-ready
- [FigTree](http://tree.bio.ed.ac.uk/software/figtree/) — desktop app, good for quick inspection
- [MEGA11](https://www.megasoftware.net/) — desktop app with editing tools

---

## Additional Resources

- [Panaroo Documentation](https://gthlab.au/panaroo/#/gettingstarted/quickstart)
- [IQ-TREE2 Documentation](http://www.iqtree.org/doc/)
- [trimAl GitHub](https://github.com/scapella/trimal)
- [iTOL](https://itol.embl.de/)