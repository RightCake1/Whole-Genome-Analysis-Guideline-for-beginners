#!/bin/bash
# Define paths
ANNOTATIONS_DIR="/home/rightcake/Fida_thesis/Annotations"
OUTPUT_DIR="/home/rightcake/Fida_thesis/Docs"
OUTPUT_FILE="$OUTPUT_DIR/prokka_comprehensive_summary.tsv"
mkdir -p "$OUTPUT_DIR"

# Header
echo -e "Sample_ID\tTotal_Bases\tGC_Content\tContigs\tCDS\tHypothetical_Prots\tRibosomal_Prots\tEfflux_Pumps\tTransposases\ttRNA\trRNA" > "$OUTPUT_FILE"

echo "Extracting data from annotation folders..."

for dir in "$ANNOTATIONS_DIR"/*/ ; do
    sample=$(basename "$dir")
    txt_file=$(ls "$dir"/*.txt 2>/dev/null | grep -v "log")
    tsv_file=$(ls "$dir"/*.tsv 2>/dev/null | grep -v "prokka")
    fna_file=$(ls "$dir"/*.fna 2>/dev/null)

    if [ -f "$txt_file" ] && [ -f "$tsv_file" ]; then
        # Genome stats
        contigs=$(grep -c ">" "$fna_file")
        bases=$(grep -v ">" "$fna_file" | tr -d '\n' | wc -c)
        gc_count=$(grep -v ">" "$fna_file" | tr -d -c 'GCgc' | wc -c)
        gc_pct=$(echo "scale=2; ($gc_count * 100) / $bases" | bc)

        # Annotation stats
        cds=$(grep "CDS:" "$txt_file" | awk '{print $2}')
        trna=$(grep "tRNA:" "$txt_file" | awk '{print $2}')
        rrna=$(grep "rRNA:" "$txt_file" | awk '{print $2}')

        # Functional insights
        hypo=$(grep -c "hypothetical protein" "$tsv_file")
        ribo=$(grep -i -c "ribosomal protein" "$tsv_file")
        efflux=$(grep -i -c "efflux pump" "$tsv_file")
        transp=$(grep -i -c "transposase" "$tsv_file")

        echo -e "$sample\t$bases\t$gc_pct\t$contigs\t$cds\t$hypo\t$ribo\t$efflux\t$transp\t$trna\t$rrna" >> "$OUTPUT_FILE"
    fi
done

echo "Done! File saved at: $OUTPUT_FILE"