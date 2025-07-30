import os
import subprocess
import pandas as pd

# Directory containing your FASTA files
fasta_dir = "/home/rightcake/OrthoANI"  # <-- Set your FASTA directory here
output_file = "ani_matrix.tsv"  # Output matrix file

# Get all FASTA files (case-insensitive .fasta)
fasta_files = [os.path.join(fasta_dir, f) for f in os.listdir(fasta_dir) if f.lower().endswith(".fasta")]
fasta_names = [os.path.basename(f).replace(".fasta", "") for f in fasta_files]  # Strip extension

# Initialize results
ani_values = {}

print("Starting all-against-all ANI calculations...")
print(f"Found {len(fasta_files)} FASTA files in {fasta_dir}")

# Progress tracking
total_comparisons = len(fasta_files) * (len(fasta_files) - 1) / 2 + len(fasta_files)
current_comparison = 0

# Run pairwise comparisons
for i, file1_path in enumerate(fasta_files):
    name1 = fasta_names[i]
    for j, file2_path in enumerate(fasta_files):
        name2 = fasta_names[j]

        # Skip duplicate comparisons
        if (name1, name2) in ani_values or (name2, name1) in ani_values:
            continue

        if name1 == name2:
            ani_values[(name1, name2)] = 100.0
            current_comparison += 1
            print(f"Processed {current_comparison}/{int(total_comparisons)}: {name1} vs {name2} (self-comparison)")
        else:
            current_comparison += 1
            print(f"Processing {current_comparison}/{int(total_comparisons)}: {name1} vs {name2}")
            try:
                command = ["pyorthoani", "-q", file1_path, "-r", file2_path]
                result = subprocess.run(command, capture_output=True, text=True, check=True)

                # ✅ FIXED: Robust parsing of numeric output
                ani_line = result.stdout.strip()
                try:
                    ani_value = float(ani_line)
                    ani_values[(name1, name2)] = ani_value
                except ValueError:
                    print(f"Warning: Could not parse ANI from output for {name1} vs {name2}. Output: {ani_line}")
                    ani_values[(name1, name2)] = float('nan')

            except subprocess.CalledProcessError as e:
                print(f"Error running pyorthoani for {name1} vs {name2}:")
                print(f"  Return Code: {e.returncode}")
                print(f"  STDOUT: {e.stdout}")
                print(f"  STDERR: {e.stderr}")
                ani_values[(name1, name2)] = float('nan')
            except Exception as e:
                print(f"Unexpected error for {name1} vs {name2}: {e}")
                ani_values[(name1, name2)] = float('nan')

# Build symmetric ANI matrix
all_genomes = sorted(set([name for pair in ani_values for name in pair]))
ani_matrix = pd.DataFrame(index=all_genomes, columns=all_genomes)

for (name1, name2), value in ani_values.items():
    ani_matrix.loc[name1, name2] = value
    ani_matrix.loc[name2, name1] = value  # ensure symmetry

# Replace NaN with 0 or another fallback
ani_matrix.fillna(0, inplace=True)

# Save output
ani_matrix.to_csv(output_file, sep="\t")
print(f"\n✅ ANI matrix saved to {output_file}")
print("Next: Use 100 - ANI values to compute distance matrix for dendrogram.")



