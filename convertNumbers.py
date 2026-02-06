"""
Converts numbers from a file to binary and hexadecimal.
Prints results on console and writes them to ConvertionResults.txt.
Handles invalid data and measures execution time.
"""
# pylint: disable=invalid-name
import sys
import time


def decimal_to_binary(n):
    """Convert decimal to binary using basic algorithm."""
    if n == 0:
        return "0"
    binary = ""
    num = int(n)
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary


def decimal_to_hex(n):
    """Convert decimal to hexadecimal using basic algorithm."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    num = int(n)
    hexa = ""
    while num > 0:
        hexa = hex_chars[num % 16] + hexa
        num //= 16
    return hexa


def main():
    """Main function to read file and convert numbers."""
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py file.txt")
        return

    start_time = time.time()
    results = []

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            for line in f:
                try:
                    num = int(line.strip())
                    bin_val = decimal_to_binary(num)
                    hex_val = decimal_to_hex(num)
                    line_result = f"{num} -> Binary: {bin_val}, Hexadecimal: {hex_val}"
                    print(line_result)
                    results.append(line_result)
                except ValueError:
                    print(f"Invalid data: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
        return

    elapsed = time.time() - start_time

    # Write results to file
    with open("ConvertionResults.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")
        f.write(f"Time: {elapsed}\n")

    print("Time:", elapsed)


if __name__ == "__main__":
    main()
