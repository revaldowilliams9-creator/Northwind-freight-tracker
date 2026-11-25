# This program cleans tracking codes, checks if they are valid,
# and saves (archives) them in a compressed file.

import re
import zlib

# This function cleans a code: removes spaces and makes it uppercase
def clean_code(code):
    code = code.replace(" ", "")  # remove all spaces
    code = code.upper()           # make everything uppercase
    return code

# This function checks if a code is valid (3 letters + 4 digits)
def is_valid_code(code):
    pattern = r"[A-Z]{3}\d{4}"   # 3 uppercase letters then 4 digits
    if re.fullmatch(pattern, code):
        return True
    else:
        return False

# ---- Main program ----

# The list of tracking codes we must check
codes = ["abc 1234", "XYZ9999", "12ab567"]

# We will store the cleaned codes here so we can archive them later
cleaned_codes = []

# Go through each code one at a time
for code in codes:
    cleaned = clean_code(code)       # clean the code first
    cleaned_codes.append(cleaned)    # keep it for the archive

    # Print the cleaned code with its status
    if is_valid_code(cleaned):
        print(cleaned, "Valid")
    else:
        print(cleaned, "Invalid")

# ---- Compress and save (archive) the codes ----

# Join all the cleaned codes into one string
text = ", ".join(cleaned_codes)

# Compress the string (turn it into bytes first)
compressed = zlib.compress(text.encode())

# Write the compressed bytes to the file using WITH statement
with open("archived_codes.bin", "wb") as f:
    f.write(compressed)

print("Codes archived to archived_codes.bin")