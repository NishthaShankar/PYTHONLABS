

import os

try:
    # Get the folder where this Python file is saved
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "log.txt")

    file = open(file_path, "r")

    error_count = 0

    print("----- LOG FILE CONTENTS -----")

    for line in file:
        print(line.strip())

        if "ERROR" in line:
            error_count += 1

    file.close()

    print("\nTotal number of errors:", error_count)

except FileNotFoundError:
    print("Error: log.txt file does not exist.")

