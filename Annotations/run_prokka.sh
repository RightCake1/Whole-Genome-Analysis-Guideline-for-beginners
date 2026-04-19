# 1. Create the destination directory if it doesn't exist
DEST_DIR="/home/rightcake/Fida_thesis/Annotations"
mkdir -p "$DEST_DIR"

# 2. Run the loop from your fasta directory
cd /home/rightcake/Fida_thesis/fasta

for file in *.fna; do
    # Extract filename without .fna
    name=$(basename "$file" .fna)
    
    echo "Starting annotation for: $name"
    
    # Run Prokka
    # --outdir points to the new Annotations folder
    # --prefix ensures files inside match the genome name
    prokka --outdir "$DEST_DIR/${name}_annot" \
           --prefix "$name" \
           --locustag "$name" \
           --cpus 8 \
           "$file"
done