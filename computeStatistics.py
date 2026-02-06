"""
compute_statistics.py

Computes descriptive statistics (mean, median, variance, std dev) from a numeric file.
Prints results on console and writes them to StatisticsResults.txt.
Handles invalid data and measures execution time.
"""
# pylint: disable=invalid-name
import sys
import time


def read_numbers(file_name):
    """Read numbers from a file and skip invalid entries."""
    numbers = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    num = float(line.strip())
                    numbers.append(num)
                except ValueError:
                    print(f"Invalid data: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    return numbers


def mean(numbers):
    """Calculate mean of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0


def median(numbers):
    """Calculate median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def main():
    """Main function to execute statistics calculations."""
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py file.txt")
        return

    start_time = time.time()
    numbers = read_numbers(sys.argv[1])

    avg = mean(numbers)
    med = median(numbers)

    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers) if numbers else 0
    std_dev = variance ** 0.5
    elapsed = time.time() - start_time

    # Print results
    print("Mean:", avg)
    print("Median:", med)
    print("Variance:", variance)
    print("Std Dev:", std_dev)
    print("Time:", elapsed)

    # Write results to file
    with open("StatisticsResults.txt", "w", encoding="utf-8") as f:
        f.write(f"Mean: {avg}\n")
        f.write(f"Median: {med}\n")
        f.write(f"Variance: {variance}\n")
        f.write(f"Std Dev: {std_dev}\n")
        f.write(f"Time: {elapsed}\n")


if __name__ == "__main__":
    main()
