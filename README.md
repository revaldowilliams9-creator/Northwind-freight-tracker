# 🚚 NorthWind Freight Tracking Validator

A lightweight **Python** data-hygiene and archiving tool built to clean, validate, and compress shipment tracking codes before database ingestion.

## 💡 Why I Built This
I built this utility to solve two common backend data-pipeline bottlenecks: messy incoming text inputs and storage bloat. Using regular expressions for strict format enforcement and `zlib` binary compression for archiving, it ensures only clean, standardized tracking records reach downstream storage.

## ✨ Key Features
* 🧹 **String Normalization:** Strips accidental whitespace and converts raw tracking inputs to consistent uppercase formatting.
* 🛡️ **Regex Validation:** Enforces strict `[A-Z]{3}\d{4}` pattern rules using Python's built-in `re` module to reject malformed codes.
* 📦 **Binary Compression:** Serializes and compresses validated tracking logs into `archived_codes.bin` using `zlib` to minimize disk footprint.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Standard Libraries:** `re` (Regular Expressions), `zlib` (Data Compression)

## 🚀 Quick Start & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Northwind-freight-tracker
   ```

2. **Run the tracking validator:**
   ```bash
   python tracking_validator.py
   ```
