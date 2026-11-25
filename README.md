# NorthWind Freight Tracking Validator

A lightweight Python data-hygiene and archiving tool built to standardize shipment tracking codes before database ingestion.

## 💡 Why I Built This 
I built this utility to solve two common backend data-pipeline bottlenecks: messy incoming text inputs and storage bloat. Using regular expressions for strict format enforcement and zlib binary compression for archiving, it ensures only clean, standardized tracking records reach downstream storage.

## Features
- **String Normalization:** Strips whitespace and converts raw tracking inputs to uppercase.
- **Regex Validation:** Enforces strict `[A-Z]{3}\d{4}` formatting using Python's `re` module.
- **Binary Compression:** Serializes and compresses daily tracking logs into `archived_codes.bin` using `zlib`.

## Usage
```bash
python tracking_validator.py
```
