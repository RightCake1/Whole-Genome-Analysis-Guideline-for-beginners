# OrthoANI Manual

This guide explains how to install and use OrthoANI for bacterial genome characterization.

## Installation

1. **Install PyOrthoANI**  
    ```bash
    pip install pyorthoani
    ```

2. **Install BLAST+**  
    PyOrthoANI requires [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) binaries.  
    Ensure BLAST+ is installed and available in your system's PATH.

3. **Reference**  
    - [PyOrthoANI GitHub Repository](https://github.com/althonos/pyorthoani)

---

## Basic Usage

### One-to-One Comparison

To compare two genome sequences:

```bash
pyorthoani -q sequence1.fa -r sequence2.fa
```

Example output:
```
57.25
```

---

## Batch Analysis

For multiple genome comparisons, use the provided Python script:

- [OrthoANI_calculate.py](OrthoANI_calculate.py)

Run the script with:
```bash
python OrthoANI_calculate.py
#Make sure to change the directory of files and names from the script before using
```

---

## Visualization

To visualize results as a dendrogram, use:

- [OrthoANI_Dendrogram.py](OrthoANI_Dendrogram.py)

Run the script with:
```bash
python OrthoANI_Dendrogram.py
#Make sure to change the directory of files and names from the script before using
```

---

**Note:**  
Ensure all required input files are in the correct format and paths are set appropriately.
