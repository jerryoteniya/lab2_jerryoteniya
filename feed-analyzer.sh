#!/bin/bash

INPUT_FILE="twitter_dataset.csv"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: '$INPUT_FILE' not found in the current directory."
    exit 1
fi

echo "Top 5 Most Active Users:"
echo "-------------------------"


python3 -c "
import csv
with open('$INPUT_FILE', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['Username'].strip())
" | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -5