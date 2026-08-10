# mydata-pcb-converter

**Note:** This is a basic converter — it currently handles top-side components only. Bottom-side support and additional features may be added in future if needed.

## About

I've been learning to code for close to three years, but I'd never used it to solve a real problem — just tutorials and "pretty things." This project is different: I worked for a company, and one of the time-consuming jobs was converting CAD-exported pick-and-place data into the MyData format their SMT machine needs, every single time, by hand. I built this to actually fix that, and to force myself to learn by solving something real rather than following along.

## What it does

Reads pick-and-place data exported from CAD software (`.txt`) and converts it into the MyData `.pcb` format used by SMT pick-and-place machines — converting units (mm → µm), extracting reference points, and formatting component placement records.

## Status

Version 1 complete. Core conversion logic (reference points, component data, PCB name) has been built as reusable functions and verified line-for-line against real sample data. Includes a file picker for selecting the source file and automatic saving alongside it. Currently top-side only — see note above.

## Tech stack

- Python
- VS Code
- Git / GitHub

## Sample Files

Two sample `.txt` files are provided in `test_files/` to demonstrate the converter:
- `LED-0134-001 iss 1.txt` — a real CAD export (19 components), verified against a known-correct `.pcb` output
- `LED-0134-001 iss 1 BIGTEST.txt` — a larger synthetic file (219 components) for testing at scale

## How to Run

### Windows
1. Check if Python is already installed by opening Command Prompt and running `python --version`
2. If not installed, install it from [python.org](https://www.python.org/downloads/) (tkinter is bundled automatically)
3. Download or clone this repository
4. Double-click `convert.py` to run
5. Select your CAD export `.txt` file when prompted
6. The converted `.pcb` file will be saved in the same folder as the source file

### Linux
1. Python 3 is pre-installed on most Ubuntu systems — check with `python3 --version`
2. Install tkinter if not already present:
```bash
   sudo apt install python3-tk
```
3. Download or clone this repository
4. Open a terminal in the project folder and run:
```bash
   python3 convert.py
```
5. Select your CAD export `.txt` file when prompted
6. The converted `.pcb` file will be saved in the same folder as the source file