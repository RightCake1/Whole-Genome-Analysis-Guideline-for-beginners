# OrthoANI Manual

This guide explains how to install and use OrthoANI for bacterial genome characterization.

Orthologous Average Nucleotide Identity (OrthoANI) is a key metric for classifying bacteria by measuring the average nucleotide identity of orthologous genes shared between two genomes. An ANI value of 95-96% is typically used as the threshold for defining a species boundary.

OrthoANI is similar to other ANI methods like FastANI but uses a more precise approach by first identifying and comparing only a defined set of orthologous genes,

## Installation

To use OrthoANI, you need to install both the Python-based pyorthoani package and the command-line suite BLAST+.

1. **Install PyOrthoANI**  
    ```bash
    pip install pyorthoani
    ```

2. **Install BLAST+**  

Install BLAST+ binaries. pyorthoani relies on BLAST for sequence alignment. You must download and install the BLAST+ command-line tools from the NCBI website and ensure they are accessible from your terminal.

    PyOrthoANI requires [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) binaries.  
    Ensure BLAST+ is installed and available in your system's PATH.

3. **Reference**  
    - [PyOrthoANI GitHub Repository](https://github.com/althonos/pyorthoani)

---

## Basic Usage

### One-to-One Comparison

To compare two bacterial genomes and get a single ANI value, you can use a simple command.

```bash
pyorthoani -q sequence1.fa -r sequence2.fa
```
q: query
r: reference

This command will output a single value representing the OrthoANI percentage between the two files. For example: 98.5.

---

## Batch Analysis

For comparing multiple genomes, you'll need a more automated approach. The provided Python scripts are designed to handle this.

The OrthoANI_calculate.py script automates the all-versus-all comparison for a directory of genome files. Before running it, you must edit the script to point to the correct input directory containing all your .fa files.

- [OrthoANI_calculate.py](OrthoANI_calculate.py)

Run the script with:
```bash
python OrthoANI_calculate.py
#Make sure to change the directory of files and names from the script before using
```
The script will produce a text file (typically a .tsv or .csv) containing the OrthoANI values for every pairwise comparison.

Outputs 

File: ani_matrix.tsv

Square matrix, symmetric.

Diagonal = 100.0 (self-comparisons).

Off-diagonal = ANI values from pyorthoani
---

## Visualization

Visualizing the results as a dendrogram or a heatmap provides a clearer picture of the genomic relationships.

Dendrogram: Use the OrthoANI_Dendrogram.py script. A dendrogram is a tree diagram that groups genomes with high ANI values close together, illustrating their evolutionary relatedness.

- [OrthoANI_Dendrogram.py](OrthoANI_Dendrogram.py)

Run the script with:
```bash
python OrthoANI_Dendrogram.py
#Make sure to change the directory of files and names from the script before using
```
Outputs: colored_dendrogram.png

Heatmap: Use the OrthoANI_Heatmap.py script. A heatmap displays ANI values in a grid, where colors represent different levels of identity. It's an excellent way to see all pairwise comparisons at a glance.

[OrthoANI_Heatmap](OrthoANI_Heatmap.py) script
```bash
python OrthoANI_Heatmap.py
#Make sure to change the directory of files and names from the script before using
```
---

**Note:**  
Ensure all required input files are in the correct format and paths are set appropriately.
