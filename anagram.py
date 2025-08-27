import argparse
import os
import sys

# Setup argument parser
parser = argparse.ArgumentParser(description="Find anagrams in a file.")
parser.add_argument(
    "-f",
    "--file",
    help="Path to the input file",
    default="sample.txt"  # Default if no argument is provided
)
args = parser.parse_args()

input_file = args.file

# Generate output filename based on input file
base, ext = os.path.splitext(input_file)
output_file = f"{base}_output.txt"

# Check if file exists
if not os.path.isfile(input_file):
    print(f"Error: file '{input_file}' not found.")
    sys.exit(1)

anagrams = {}

try:
    # Open and read input file
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if not word:
                continue
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

    # If no words were found, warn and exit
    if not anagrams:
        print(f"Warning: file '{input_file}' is empty. Nothing to process.")
        sys.exit(0)

    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for key, value in anagrams.items():
            formatted_output = ' '.join(value)
            f.write(formatted_output + '\n')
            print(formatted_output)

    print(f"\nOutput saved to: {output_file}")

except PermissionError:
    print(f"Error: no permission to read or write the file '{input_file}'.")
    sys.exit(1)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)