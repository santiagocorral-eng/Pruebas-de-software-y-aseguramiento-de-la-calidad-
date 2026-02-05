import sys
import time


def read_numbers(file_path):
    numbers = []
    file = open(file_path, "r")
    for line in file:
        value = line.strip()
        try:
            numbers.append(float(value))
        except ValueError:
            print("Invalid data:", value)
    file.close()
    return numbers


def mean(numbers):
    Sum = 0
    for n in numbers:
        Sum += n
    return Sum / len(numbers)


def median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    mid = size // 2
    if size % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]


def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py file.txt")
        return

    start = time.time()
    nums = read_numbers(sys.argv[1])

    avg = mean(nums)
    med = median(nums)

    variance = 0
    for n in nums:
        variance += (n - avg) ** 2
    variance = variance / len(nums)
    std = variance ** 0.5

    elapsed = time.time() - start

    print("Mean:", avg)
    print("Median:", med)
    print("Variance:", variance)
    print("Std Dev:", std)
    print("Time:", elapsed)


if __name__ == "__main__":
    main()

