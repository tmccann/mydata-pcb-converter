# mydata-pcb-converter

About

I've been learning to code for close to three years, but I'd never used it to solve a real problem — just tutorials and "pretty things." This project is different: I worked for a company, and one of the time-consuming jobs was converting CAD-exported pick-and-place data into the MyData format their SMT machine needs, every single time, by hand. I built this to actually fix that, and to force myself to learn by solving something real rather than following along.

What it does

Reads pick-and-place data exported from CAD software (.txt) and converts it into the MyData .pcb format used by SMT pick-and-place machines — converting units (mm → µm), extracting reference points, and formatting component placement records.

Status

Work in progress. As it's been a while since I last used Python, this project is as much a learning curve as it is a build. Core conversion logic works and has been verified against sample data, currently being restructured into reusable functions. GUI planned next.

Tech stack

Python
VS Code
Git / GitHub

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