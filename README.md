# 🚚 NorthWind Freight Tracking Validator

A lightweight **Python** data-hygiene and archiving tool built to clean, validate, and compress shipment tracking codes before database ingestion.

## 💡 Why I Built This
I built this utility to solve two common backend data-pipeline bottlenecks: messy incoming text inputs and storage bloat. Using pre-compiled regular expressions for strict format enforcement and `zlib` binary compression for archiving, it ensures only clean, standardized tracking records reach downstream storage while isolating malformed entries for auditing.

## ✨ Key Features
* 🧹 **String Normalization:** Strips all accidental whitespace (spaces, tabs, newlines) and converts raw tracking inputs to consistent uppercase formatting.
* 🛡️ **Pre-Compiled Regex Validation:** Enforces strict `[A-Z]{3}\d{4}` pattern rules using Python's `re` module for fast validation across large batches.
* 📂 **Flexible Input Handling:** Reads raw tracking codes from `incoming_codes.txt` with an automatic fallback to built-in sample data if no input file is present.
* 🚨 **Error Auditing:** Separates malformed records into `rejected_codes.log` so invalid data never pollutes downstream storage.
* 📦 **Binary Compression & Verification:** Serializes and compresses validated tracking logs into `archived_codes.bin` using `zlib`, then performs a round-trip decompression check to verify archive integrity.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Standard Libraries:** `re` (Regular Expressions), `zlib` (Data Compression), `pathlib` (File System Paths)

## 🚀 Quick Start & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Northwind-freight-tracker
   ```

2. **(Optional) Add your own input file:**
   Create an `incoming_codes.txt` file in the project root with one tracking code per line. If omitted, the script automatically runs using built-in sample data.

3. **Run the tracking validator:**
   ```bash
   python tracking_validator.py
   ```

## 🖥️ Sample Output
```text
Notice: 'incoming_codes.txt' not found. Running with built-in sample data.

[VALID]   ABC1234
[VALID]   XYZ9999
[INVALID] 12AB567
[INVALID] DEF-5678
[VALID]   GHI0001
----------------------------------------
Successfully archived 3 valid codes to 'archived_codes.bin'.
Logged 2 invalid codes to 'rejected_codes.log'.
Verified archive contents: ['ABC1234', 'XYZ9999', 'GHI0001']
```

<img width="604" height="100" alt="image" src="https://github.com" />
