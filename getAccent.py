# Create an empty set to store the distinct character pairs
distinct_pairs = set()

# Open the input file for reading
with open('./fr_FR.txt', 'r', encoding='utf-8') as input_file:

    # Iterate over each line in the input file
    for line in input_file:

        # Find all instances of the combining tilde character in the line
        tilde_indexes = [i for i, c in enumerate(line) if c == '\u0303']

        # Iterate over each tilde index
        for tilde_index in tilde_indexes:

            # Find the characters preceding and following the tilde
            prev_char = line[tilde_index - 1]
            next_char = line[tilde_index]

            # Add the character pair to the set
            distinct_pairs.add(prev_char + next_char)

# Open the output file for writing
with open('./TMP_EXPORT_ACCENT', 'w', encoding='utf-8') as output_file:

    # Write each distinct character pair to the output file
    for pair in distinct_pairs:
        output_file.write(pair + '\n')
