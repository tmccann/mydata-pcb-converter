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
