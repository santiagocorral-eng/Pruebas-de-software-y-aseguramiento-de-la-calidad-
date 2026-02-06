4.2 Programming Excercise 1

Programs Included
1. compute_statistics.py

Computes descriptive statistics (mean, median, variance, and standard deviation)

Reads numeric data from a file

Handles invalid data and continues execution

Prints results to console and saves them to StatisticsResults.txt

Initial pylint analysis (errors detected)
Your code has been rated at 7.61/10
Issues included:
- Missing module and function docstrings
- Variable names not following snake_case (e.g., Sum)
- File handling without `with` statement
- Missing encoding specification
- Module name not following snake_case (C0103)

Actions Taken

Added module and function docstrings

Renamed variables to follow snake_case

Updated file handling using with statement

Specified file encoding

Ensured PEP8 compliance

Final pylint analysis
Your code has been rated at 9.79/10
Warning left intentionally:
- C0103: Module name "compute_statistics" doesn't follow snake_case (assignment requires original filename)

2. convert_numbers.py

Converts decimal numbers to binary and hexadecimal

Reads numeric data from a file

Handles invalid data and continues execution

Uses basic algorithms (no built-in conversion functions)

Prints results to console and saves them to ConvertionResults.txt

Initial pylint analysis (errors detected)
Your code has been rated at 6.56/10
Issues included:
- Missing module and function docstrings
- Variable names not following snake_case
- File handling without `with` statement
- Missing encoding specification
- Module name not following snake_case (C0103)

Actions Taken

Added module and function docstrings

Renamed variables to follow snake_case

Used with statement for file handling and specified encoding

Improved error handling for invalid data

Implemented binary and hexadecimal conversions using basic algorithms

Final pylint analysis
Your code has been rated at 9.80/10
Warning left intentionally:
- C0103: Module name "convert_numbers" doesn't follow snake_case (assignment requires original filename)

3. word_count.py

Counts all distinct words in a text file and their frequency

Prints results to console and saves them to WordCountResults.txt

Handles invalid data gracefully

Measures and prints execution time

Initial pylint analysis (errors detected)
Your code has been rated at 5.45/10
Issues included:
- Missing module and function docstrings
- Function and variable names not following snake_case
- Broad exception handling (catching Exception)
- File handling without `with` statement
- Missing encoding specification
- Module name not following snake_case (C0103)

Actions Taken

Added module and function docstrings

Renamed variables to follow snake_case

Replaced broad exception handling with more specific exceptions

Used with statement and specified encoding

Fixed PEP8 issues

Final pylint analysis
Your code has been rated at 9.78/10
Warning left intentionally:
- C0103: Module name "word_count" doesn't follow snake_case (assignment requires original filename)

Notes

All programs generate an output file (StatisticsResults.txt, ConvertionResults.txt, WordCountResults.txt) containing only the final results and execution time.

Invalid data is reported in the console but does not interrupt execution.

Execution times may vary depending on the system and file size.

The README reflects the evolution of pylint scores and the specific issues corrected for clarity
