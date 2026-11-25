# NorthWind Freight Tracking Validator

A lightweight Python data-hygiene and archiving tool built to standardize shipment tracking codes before database ingestion.

## Features
- **String Normalization:** Strips whitespace and converts raw tracking inputs to uppercase.
- **Regex Validation:** Enforces strict `[A-Z]{3}\d{4}` formatting using Python's `re` module.
- **Binary Compression:** Serializes and compresses daily tracking logs into `archived_codes.bin` using `zlib`.

## Usage
```bash
python tracking_validator.py
```
