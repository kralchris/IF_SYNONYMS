from collections import defaultdict
from io import StringIO

# Create a StringIO object to capture the output
output_stringio = StringIO()

# Read from input file
with open('test.in', 'r') as input_file:
    # Read the number of test cases
    t = int(input_file.readline())
    for _ in range(t):
        # Read the synonym dictionary
        n = int(input_file.readline())
        synonym_dict = defaultdict(set)
        for _ in range(n):
            word1, word2 = input_file.readline().split()
            synonym_dict[word1.lower()].add(word2.lower())
            synonym_dict[word2.lower()].add(word1.lower())

        # Read the queries and check if they are synonyms
        q = int(input_file.readline())
        for _ in range(q):
            word1, word2 = input_file.readline().split()
            word1_lower = word1.lower()
            word2_lower = word2.lower()

            if word1_lower == word2_lower:
                # Rule 4: Words are the same
                print("synonyms", file=output_stringio)
            elif word2_lower in synonym_dict[word1_lower]:
                # Rule 1: Words are declared synonymous in the input
                print("synonyms", file=output_stringio)
            elif word1_lower in synonym_dict[word2_lower]:
                # Rule 2: Being synonyms doesn’t depend on order
                print("synonyms", file=output_stringio)
            else:
                # Rule 3: Derive the synonymous relationship indirectly
                found_synonym = False
                for synonym in synonym_dict[word1_lower]:
                    if word2_lower in synonym_dict[synonym]:
                        print("synonyms", file=output_stringio)
                        found_synonym = True
                        break
                if not found_synonym:
                    print("different", file=output_stringio)

# Get the captured output as a string
output_string = output_stringio.getvalue()

# Write to output file
with open('test.out', 'w') as output_file:
    output_file.write(output_string)
