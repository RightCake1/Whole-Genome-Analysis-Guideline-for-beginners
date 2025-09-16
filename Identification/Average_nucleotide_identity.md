# Average Nucleotide Identity (ANI) Analysis Guide

## Introduction
Average Nucleotide Identity (ANI) is a powerful method for comparing the genomic similarity between bacterial strains. It provides a numerical value, typically expressed as a percentage, that indicates how much of two genomes' DNA sequences are identical. An ANI value of 95% or higher

## FastANI Setup and Usage

The ANI Workflow: A Step-by-Step Guide
The process of calculating ANI involves three main steps:

Preparation: Getting your tool and data ready.

Calculation: Running FastANI to compute the ANI values.

Interpretation & Visualization: Analyzing the results to draw conclusions about species relatedness.

### Installation

The easiest way to install FastANI and its dependencies is by using a Conda environment. This ensures all the required software works together seamlessly.

Open your terminal.

Create a new Conda environment and install FastANI from the bioconda channel.

```bash
# Via conda (recommended)
conda create -n ani_tools
conda activate ani_tools
conda install -c bioconda fastani
```

# OR 
```bash

# Via source
git clone https://github.com/ParBLiSS/FastANI.git
cd FastANI
make
```
Verify the installation by checking the version.

```bash 
# Verify installation
fastANI --version
```

### Preparing Reference Data

For ANI analysis, you need to compare your "query" genome (the one you want to identify) against one or more "reference" genomes (known genomes from public databases). The most common source for high-quality genomes is the NCBI RefSeq database.

#### Download RefSeq Data
 
You can download reference sequences from GTDB (Genome Taxonomy Database), NCBI (National Center for Biotechnology Information), JGI IMG/M (Integrated Microbial Genomes & Microbiomes) or Type Strain Genome Server (TYGS).

#### Create Reference List
```bash
# Create list of reference genomes
ls *.fna > reference_list.txt

# For multiple queries
ls query_*.fasta > query_list.txt
```

### Running FastANI

#### Basic Usage
```bash
# Single query vs single reference
fastANI \
    -q contigs.fasta \
    -r reference.fasta \
    -o output.txt
```
```bash
# Single query vs multiple references
fastANI \
    -q contigs.fasta \
    --rl reference_list.txt \
    -o multi_ref_output.txt
```
```bash 
# Multiple queries vs multiple references
fastANI \
    --ql query_list.txt \
    --rl reference_list.txt \
    -o all_vs_all.txt
```

### Output Format
FastANI output contains:
```plaintext
query_genome  reference_genome  ANI_value  fragments_mapped  total_fragments
```

Understanding the Output
FastANI generates a simple, tab-separated output file with the following columns:

query_genome: The name of your input genome file.

reference_genome: The name of the reference genome it was compared to.

ANI_value: The most important column! This is the percentage of identity.

fragments_mapped: The number of DNA fragments that were mapped from your query to the reference.

total_fragments: The total number of fragments from the query genome.

## Interpreting the ANI Value
The ANI value is your key to species classification.

≥95% ANI: The two genomes likely belong to the same species. This is the standard cutoff for species-level classification.

≥75% ANI: The two genomes are likely in the same genus.

<75% ANI: The two genomes are likely from different genera.

## Visualization Using Python Script

A table of numbers can be hard to read. Visualizing the ANI data as a dendrogram (a tree diagram) or a heatmap makes the relationships between your genomes much clearer. . The Python script provided in the original guide will use your FastANI output to create a tree, grouping genomes with high ANI values close together.

Before running the script, make sure you edit it to point to the correct file names and paths for your ANI output file and your query/reference lists.

To run the script, use the command python [ANI Dendrogram Python script](Ani_based_dendrogram.py). 

**Required files:**
- Query genome list (`query_list.txt`)
- Reference genome list (`reference_list.txt`)
- FastANI output file (e.g., `all_vs_all.txt`)

**To run the script:**
```bash
python Ani_based_dendrogram.py
```
Reads FastANI results from:

fastani.txt → contains pairwise ANI comparisons.

query_list.txt and reference_list.txt → lists of genomes (you don’t actually use them later in the code, but they’re read).

Creates an ANI matrix using pivot:

Rows = queries

Columns = references

Values = ANI (%)

Fills missing values with 0.

Runs hierarchical clustering on the matrix with linkage(method='average').

Plots dendrogram of the 81 genomes, saved as: dendrogram.png
## Visualization with Proksee

For a more advanced and interactive visualization, you can use Proksee. This web-based tool allows you to upload a query and reference genome and instantly see a comparison plot.

**Website**: [Proksee](https://proksee.ca/)
Used for 1-1 comparison

Why use it?: Proksee not only shows you the ANI value but also visualizes synteny (the order of genes) between the two genomes, providing a much richer biological context.

#### Features
* Interactive visualization
* Genome comparison
* Synteny analysis
* Gene annotation
* Metabolic pathway mapping

#### Usage Steps
1. Register/Login to Proksee
2. Upload genome files:
   * Query genome
   * Reference genome
   * FastANI results
3. Select visualization options
4. Generate and download reports

### Quality Control
* Minimum genome completeness
* Appropriate fragment coverage
* Sufficient query length
* Contamination assessment

## Best Practices

### Data Preparation
* Use complete or high-quality draft genomes
* Check assembly quality metrics
* Verify taxonomy assignments
* Use appropriate reference genomes

### Analysis Workflow
1. Quality check input genomes
2. Run FastANI with appropriate parameters
3. Validate results
4. Visualize relationships
5. Document findings

### Tips for Success
* Use multiple reference strains
* Consider evolutionary relationships
* Validate critical results
* Document analysis parameters

## Common Issues and Solutions

### Low ANI Values
* Check genome quality
* Verify taxonomic assignment
* Consider evolutionary distance
* Check for contamination

### Computation Issues
* Adjust fragment size
* Increase memory allocation
* Use multiple threads
* Split large datasets

## Results Interpretation

### Making Species-Level Decisions
* Consider multiple lines of evidence
* Use appropriate thresholds
* Account for biological context
* Document decision criteria

## Additional Resources

* [FastANI GitHub](https://github.com/ParBLiSS/FastANI)
* [ANI Calculator](https://www.ezbiocloud.net/tools/ani)
* [NCBI Genome](https://www.ncbi.nlm.nih.gov/genome)
* [Type Strain Genome Server](https://tygs.dsmz.de)
* [GTDB (Genome Taxonomy Database)]( https://gtdb.ecogenomic.org/)
* [JGI IMG/M (Integrated Microbial Genomes & Microbiomes)](https://img.jgi.doe.gov/)

---

**Note**: Regular updates of reference databases and tools are essential for accurate analysis.