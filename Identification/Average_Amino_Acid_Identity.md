# Average Amino Acid Identity (AAI) Analysis with EzAAI

This guide walks you through installing EzAAI, preparing your data, running AAI calculations, and visualizing results.

---

## 1. Install EzAAI (Recommended: Conda)

Install EzAAI using Conda (recommended for ease and reproducibility):

```bash
conda install -c bioconda -y ezaai
```

Verify the installation:

```bash
ezaai -h
```

---

## 2. Validate FASTA Headers

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

This step compares each genome’s protein database to all others using MMseqs2 internally.

```bash
ezaai calculate -i /home/rightcake/KPV/EzAAI_dbs/ -j /home/rightcake/KPV/EzAAI_dbs/ -o /home/rightcake/KPV/AAI/aai_results.tsv
#make sure to change the locatin of the file to your location
```

- `-i` and `-j`: Input directories (use the same folder for all-vs-all comparison)
- `-o`: Path to your output AAI results file

---
## 5. Convert the Results for Visualization

Convert the resulting TSV file to a format suitable for figure generation using the provided script [`Convert_AAI_tsv.py`](./Convert_AAI_tsv.py).
Make sure to change the locatin of the file to your location.

```bash
python Convert_AAI_tsv.py -i /home/rightcake/KPV/AAI/aai_results.tsv -o /home/rightcake/KPV/AAI/aai_results_converted.tsv
```

---

## 6. Visualize AAI Results

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

## References

- [EzAAI GitHub Repository](https://github.com/endixk/ezaai?tab=readme-ov-file)
- [EzAAI Website](https://endixk.github.io/ezaai/)