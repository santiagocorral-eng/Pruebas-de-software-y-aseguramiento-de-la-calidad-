"""
wordCount.py

Counts all distinct words in a text file and their frequency.
Prints results on console and writes them to WordCountResults.txt.
Handles invalid data and measures execution time.
"""
# pylint: disable=invalid-name
import sys
import time


def count_words(file_name):
    """Read file and count distinct words."""
    word_counts = {}
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                for word in line.strip().split():
                    w = word.lower()
                    word_counts[w] = word_counts.get(w, 0) + 1
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    return word_counts


def main():
    """Main function to execute word count."""
    if len(sys.argv) != 2:
        print("Usage: python word_count.py file.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    counts = count_words(file_name)

    # Print and save results
    with open("WordCountResults.txt", "w", encoding="utf-8") as out_file:
        for word, freq in counts.items():
            line = f"{word}: {freq}"
            print(line)
            out_file.write(line + "\n")

    elapsed = time.time() - start_time
    print(f"Time elapsed: {elapsed:.4f} seconds")
    with open("WordCountResults.txt", "a", encoding="utf-8") as out_file:
        out_file.write(f"Time elapsed: {elapsed:.4f} seconds\n")


if __name__ == "__main__":
    main()
