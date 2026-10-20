import csv

# Mapping of CSV headers to RIS tags
FIELD_MAP = {
    'TY:': 'TY',
    'ID:': 'ID',
    'TI:': 'TI',
    'AU:': 'AU',
    'PB:': 'PB',
    'PY:': 'PY',   # RIS publication year tag
    'SP:': 'SP',
    'EP:': 'EP',
    'C1:': 'C1',
    'C2:': 'C2',
    'C3:': 'C3',
    'C4:': 'C4',
    'N1:': 'N1',
    'ER:': 'ER'
}

def csvtoris(csv_file, ris_file):
    with open(csv_file, newline='', encoding='utf-8') as infile, \
         open(ris_file, 'w', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)

        for row in reader:
            for csv_field, ris_tag in FIELD_MAP.items():
                value = row.get(csv_field, '').strip()

                if value:
                    # Special handling for multiple authors
                    if ris_tag == 'AU':
                        authors = [a.strip() for a in value.split(';')]
                        for author in authors:
                            outfile.write(f'AU  - {author}\n')
                    else:
                        outfile.write(f'{ris_tag}  - {value}\n')

            # Ensure RIS record ends properly
            outfile.write('ER  - \n\n')

    print(f"RIS file written to: {ris_file}")


# Example usage
csvtoris('books.csv', 'books.ris')
