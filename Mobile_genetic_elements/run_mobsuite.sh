#!/bin/bash

# Ensure your environment is active (optional, but good practice)
# conda activate mobsuite

mkdir -p /home/rightcake/Fida_thesis/MOB_Results

# Get the total count of files
files=(/home/rightcake/Fida_thesis/fasta/*.fna)
total_files=${#files[@]}
current_count=0

echo "Starting MOB-suite Plasmid Typing for $total_files isolates..."

for f in "${files[@]}"; do
    ((current_count++))
    id=$(basename "$f" .fna)
    
    # Calculate percentage and progress bar width (20 blocks total)
    percent=$((current_count * 100 / total_files))
    filled=$((percent / 5))
    empty=$((20 - filled))
    
    # Print the progress bar on one line
    printf "\rProgress: ["
    printf "%${filled}s" '' | tr ' ' '#'
    printf "%${empty}s" '' | tr ' ' '.'
    printf "] %d%% (%d/%d) - Current: %s" "$percent" "$current_count" "$total_files" "$id"
    
    # Run mob_typer (logging output to keep the progress bar clean)
    mob_typer --infile "$f" \
               --outdir "/home/rightcake/Fida_thesis/MOB_Results/$id" \
               --db /home/rightcake/Fida_thesis/mobsuite_db/data > "/home/rightcake/Fida_thesis/MOB_Results/${id}_run.log" 2>&1
Done
echo -e "\n\n✅ MOB-suite analysis complete!"