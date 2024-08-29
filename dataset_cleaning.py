"""
This script reads a text file, replaces sequences of three or more spaces with a tab character,
and writes the cleaned data back to the same file.
"""
import re
filearray = ["TempoWordNet\TempoWnH_1.0.txt", "TempoWordNet\TempoWnL_1.0.txt", "TempoWordNet\TempoWnP_1.0.txt", ]

for i in filearray: 
    # Step 1: Read the .txt file
    with open(i, 'r') as file:
        data = file.read()

    # Step 2: Apply the Regex
    # The regex expression `re.sub(r'[ ]{3,}', ' ', data)` replaces 3 or more spaces with 5 spaces
    cleaned_data = re.sub(r'[ ]{3,}', '\t', data)

    # Step 3: Write the cleaned data back to a new file or overwrite the original file
    with open(i, 'w') as file:
        file.write(cleaned_data)
