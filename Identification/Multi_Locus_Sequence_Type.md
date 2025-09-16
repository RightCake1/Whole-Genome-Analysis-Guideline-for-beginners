# Multi Locus Sequence Type

## Introduction
This guide covers essential tools for assigned sequence types to bacteria

## MLST (Multi Locus Sequence Type)

### Overview
Sequence type (ST) is based on the identification of housekeeping genes (usually 7), which allelic combination gives an unique ST. <br>
There are two complementary, public, curated databases which assign new STs, collect sequences, and isolates information:
* [PubMLST](https://pubmlst.org/)
* [BIGSdb-Pasteur](https://bigsdb.pasteur.fr/)

### MLST

MLST is databases-based tool to identify allelic combinations and determine STs from assembled genomes.

### Access and Usage

GitHub page: https://github.com/tseemann/mlst

#### Required input:
- Assembled genome in FASTA format


### Installation

First, you need to install the mlst tool on your computer. Using Conda is the easiest way to manage this and other bioinformatics software.

```bash
# Create conda environment
conda create -n mlst -c bioconda mlst
```

```bash
# Activate environment
conda activate mlst
```

```bash
# Verify installation
mlst --version
```

The primary input for the mlst tool is a complete or draft genome assembly file in FASTA format.

The tool will automatically detect the most likely bacterial species based on the genes it finds and then try to assign an ST.

```bash
### Basic Usage
mlst assembly.fasta
```

### Output Files
- `.tab`: It contains the filename, the matching scheme name, the ST , and the allele IDs. 

### Missing data

Missing or incomplete results, do not mean any error has occured. <br>
Indeed, MLST do not only find known alleles, but attempts to tell you as much as possible about what it found using the notation below:

Symbol | Meaning | Length | Identity
---   | --- | --- | ---
`n`   | exact intact allele                   | 100%            | 100%
`~n`  | novel full length allele similar to n | 100%            | &ge; `--minid`
`n?`  | partial match to known allele         | &ge; `--mincov` | &ge; `--minid`
`-`   | allele missing                        | &lt; `--mincov` | &lt; `--minid`
`n,m` | multiple alleles                      | &nbsp;          | &nbsp;

The most important part of the output is the ST number. If you get an ST, it's a confident match. If you get a new ST, it will be labeled accordingly, and you can submit it to the appropriate database.

## Best Practices

1. Quality Control
   - Ensure genome assembly quality before identify ST
   - Check for contamination: a contaminated assembly can cause a wrong alleles identification (ex. wrong scheme used)

2. Updating database

```bash
which mlst
```
    - The `mlst` software comes bundled with the traditional MLST databases;
namely those schemes with less than 10 genes. However, given the increase use of sequencing, every year many new allele profiles and STs are identified. To not lose any information, once every 6 months or 1 year would be good practice to update the database. <br>
Here an brief guide:
    ```
    # Figure out where mlst is installed
    % which mlst
    /home/user/sw/mlst

    # Go into the scripts folder (you need to have write access!)
    % cd /home/user/sw/mlst/scripts

    # Run the downloader script (you need 'wget' installed)
    % ./mlst-download_pub_mlst | bash

    # Check it downloaded everything ok
    % find pubmlst | less

    # Save the old database folder
    % mv ../db/pubmlst ../db/pubmlst.old

    # Put the new folder there
    % mv ./pubmlst ../db/

    # Regenerate the BLAST database
    % ./mlst-make_blast_db

    # Check schemes are installed
    % ../bin/mlst --list
    ```


## Additional Resources
- [MLST GitHub](https://github.com/tseemann/mlst)
- [PubMLST](https://pubmlst.org/organisms)
- [BIGSdb-Pasteur](https://bigsdb.pasteur.fr/)

---
**Note**: For detailed parameters and advanced usage, refer to each tool's documentation.