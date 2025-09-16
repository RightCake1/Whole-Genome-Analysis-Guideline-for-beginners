# Average Amino Acid Identity (AAI) Analysis with EzAAI

Average Amino Acid Identity (AAI) is a key metric for measuring the evolutionary relatedness between two organisms at the protein level. It calculates the average identity of all orthologous (gene pairs that arose from a speciation event) proteins shared between two genomes. An AAI value of 95% is a common threshold for distinguishing between species.

This guide walks you through the entire AAI analysis workflow using the EzAAI tool.

---
The AAI Analysis Workflow
Calculating AAI is a multi-step process that starts with your raw genome data and ends with a clear visualization of genetic relationships.

Preparation: Install EzAAI and organize your genome assemblies.

Protein Extraction: Convert your DNA genome files into protein databases.

Calculation: Run EzAAI to perform an all-versus-all comparison.

Visualization: Generate a dendrogram or heatmap to see the relationships.

## 1. Install EzAAI (Recommended: Conda)

The easiest way to install EzAAI is with Conda. This ensures you also get MMseqs2, the underlying tool EzAAI uses for protein comparisons.

```bash
conda install -c bioconda -y ezaai
```

Verify the installation:

```bash
ezaai -h
```

---

## 2. Validate FASTA Headers

Before you can calculate AAI, you need to convert your DNA genome files (in FASTA format) into protein databases. This is a crucial step that EzAAI handles for you.

Ensure all your input files have valid FASTA headers. Replace `*.fasta` with your actual file extension if needed.

```bash
for f in /home/rightcake/KPV/AAI/*.fasta; do
    if ! grep -q "^>" "$f"; then
        echo "❌ No FASTA header in: $f"
    fi
done
#make sure to change the locatin of the file to your location
```

---

## 3. Extract Protein Databases

Create a directory for EzAAI protein databases and extract them from your genome FASTA files:

```bash
mkdir -p /home/rightcake/KPV/EzAAI_dbs

for f in /home/rightcake/KPV/AAI/*.fasta; do
    if grep -q "^>" "$f"; then
        base=$(basename "$f" .fasta)
        echo "✅ Extracting: $base"
        ezaai extract -i "$f" -o "/home/rightcake/KPV/EzAAI_dbs/$base"
    else
        echo "❌ Skipped invalid FASTA: $f"
    fi
done
#make sure to change the locatin of the file to your location
```

---

## 4. Run All-Vs-All AAI Calculation

Once you have your protein databases, you can run the AAI calculation.

This step compares each genome’s protein database to all others using MMseqs2 internally.

```bash
ezaai calculate -i /home/rightcake/KPV/EzAAI_dbs/ -j /home/rightcake/KPV/EzAAI_dbs/ -o /home/rightcake/KPV/AAI/aai_results.tsv
#make sure to change the locatin of the file to your location
```

- `-i` and `-j`: Input directories (use the same folder for all-vs-all comparison)
- `-o`: Path to your output AAI results file

---
## 5. Convert the Results for Visualization

The aai_results.tsv file is a simple list of pairwise comparisons. To visualize this data, you first need to convert it into a format that a plotting script can use. This is done with a dedicated Python script.

Convert the resulting TSV file to a format suitable for figure generation using the provided script [`Convert_AAI_tsv.py`](./Convert_AAI_tsv.py).
Make sure to change the locatin of the file to your location.

```bash
python Convert_AAI_tsv.py -i /home/rightcake/KPV/AAI/aai_results.tsv -o /home/rightcake/KPV/AAI/aai_results_converted.tsv
```
This command takes the raw results and converts them into a formatted table suitable for generating a tree or heatmap.
---

## 6. Visualize AAI Results

The final step is to generate a visual representation of your data. The converted file can be used to create a dendrogram, which is a tree diagram that groups genomes by their AAI similarity. .

Generate figures from the converted data using the script [`AAI_dendrogram.py`](./AAI_dendrogram.py).
Make sure to change the locatin of the file to your location.

```bash
python AAI_dendrogram.py -i /home/rightcake/KPV/AAI/aai_results_converted.tsv -o /home/rightcake/KPV/AAI/aai_dendrogram.png
```

Alternatively, you can use [`AAI_visuals.py`](./AAI_visuals.py) for additional visualizations:

```bash
python AAI_visuals.py -i /home/rightcake/KPV/AAI/aai_results_converted.tsv -o /home/rightcake/KPV/AAI/aai_visuals.png
```
```
---

The output will be an image file (e.g., aai_dendrogram.png) that clearly shows the genetic relationships between all your genomes. Genomes that are closely related (i.e., have high AAI values) will be grouped together on the dendrogram.

## References

- [EzAAI GitHub Repository](https://github.com/endixk/ezaai?tab=readme-ov-file)
- [EzAAI Website](https://endixk.github.io/ezaai/)