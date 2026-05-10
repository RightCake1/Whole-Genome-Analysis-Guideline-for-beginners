# Phylogenetic Tree Construction Using KBase

KBase is a free, web-based platform for biological data analysis. This guide walks you
through building a phylogenetic species tree from FASTA files entirely in the browser —
no command line needed.

---

## Step 1 — Retrieve FASTA Files

You can get your genome sequences from [IMG/M](https://img.jgi.doe.gov/) or use files
you already have. If downloading from IMG/M:

1. Create an account and go to the [Genome Search](https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=GenomeSearch&page=searchForm) page
2. Click **Advanced Search Builder → Add new builder line**
3. Select **Taxonomy → NCBI Species** and type your organism name
4. Add another builder line → **Sequencing Assembly Annotation → Sequencing Quality → Level 6** for highest quality genomes
5. Click **Evaluate Query** to check available sequences, then click **Search**
6. In the results table, scroll down and under **NCBI Metadata** select **NCBI Assembly Accession** and **NCBI GenBank ID**, then click **Redisplay**
7. Select all genomes using the top-left checkbox and click **Export** to download the table
8. To download sequences in bulk, click **Add to Genome Cart**, then **Upload & Export & Save → Export Genomes** — you will be notified by email when ready

---

## Step 2 — Set Up KBase

1. Go to [kbase.us](https://www.kbase.us/) and click **Get Started**
2. Create an account and log in
3. Click **New Narrative** in the top right once the platform loads

---

## Step 3 — Import Your FASTA Files

1. Click the **+** sign under **Data** and then click **Import**
2. Upload your FASTA files and set **Import As** to **FASTA Assembly**
3. Click **Import Selected** and wait for them to load
4. When the **Import from Staging Area** window appears, click **Run**
5. Your files will now appear under the **Data** panel

---

## Step 4 — Annotate Genomes

Under **Apps → Genome Annotation**, search for the appropriate tool:

| Situation | App to use |
|-----------|-----------|
| Single FASTA file | **Annotate Genome/Assembly with RASTtk - v1.073** |
| Multiple FASTA files | **Annotate Multiple Microbial Assemblies with RASTtk - v1.073** |

Select your files, click **Run**, and wait. Annotated files will appear under **Data**.

> Only annotated files will be visible in downstream steps.

---

## Step 5 — Create a GenomeSet

1. Under **Comparative Genomics**, select **Add Genomes to GenomeSet - v1.7.6**
2. Add your annotated genome files and click **Run**
3. You can create multiple GenomeSets to manage large file lists more easily

---

## Step 6 — Build the Species Tree

1. Under **Comparative Genomics**, click **Insert Set of Genomes Into SpeciesTree - v2.2.0**
2. Select your GenomeSet(s) and click **Run**

> This step can take time depending on the number of genomes and available RAM.

**Neighbor Public Genome Count** parameter:
- If your organism is well-known → set to **2–3**
- If less characterized → set to **1** to reduce clutter in the tree

---

## Step 7 — Trim the Tree

1. Under **Comparative Genomics**, click **Trim SpeciesTree to GenomeSet - v1.4.0**
2. This removes any extra reference genomes that were added automatically and don't belong to your dataset

---

## Step 8 — Download Your Tree

Your tree is now ready to download in multiple formats:

- `.newick` — for use in MEGA11, FigTree, or iTOL
- `-labels.newick` — newick with tip labels
- `.png` — image format
- `.pdf` — publication-ready format

---

## Additional Resources

- [KBase](https://www.kbase.us/)
- [IMG/M Genome Search](https://img.jgi.doe.gov/)
- [RASTtk Documentation](https://rast.nmpdr.org/)