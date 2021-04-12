# Mortal Online Calculator
Calculators for use with Mortal Online 2

## Prerequisites

### Pip

You will need python>=3.6 to run this project. Python can be found along with installation instructions here: https://www.python.org/

You will also need PyQt5 which can be installed by:

```bash
pip install pyqt5
```

### Anaconda

You can instead use anaconda which can be found here: https://www.anaconda.com/products/individual

After installing you can use conda to install PyQt5

```bash
conda install pyqt
```

## Installation

To install the scripts first navigate to the base directory where you want to locate the project folder

You can eith download a zip and extract, or you can use git

```bash
git clone https://github.com/minyiky/mortal_calcs.git
```

## Usage

### Bow Calculator

While in project root folder navigate to the bow folder

```bash
cd bow
```

Once there you can run the program with:

```bash
python bow_calc.py
```

## Known Issues

 - Currently a single bow calculator has not been implimented, please use the one found at https://www.mortalonlinemap.info/emulator/bowcalc.php
Note that there is a parculiarity with how the input is used and it is the opposite to what you expect. Compared to the order in the crfting table, the materials should be entered the opposite way round, and the percentage should be entered as 100 - the value used at the crafting bench

 - Some material combinations may be out, especially at percentages ner 25 or 75, if you find an error please submit an issue as detailed below

 - Durability calculations are not currently included. More testing is need

 - Emalji is currently not included

## Contributing

If you find an error in the numbers, please first check that the bow you have made is of impreccable quality and that all lores and bowery skills were at 100 before you began crafting the bow

If that is the case please submit a "Bow Calculation Error" here https://github.com/minyiky/mortal_calcs/issues/new/choose

## Acknowledgemnts
A massive thank you to the team that made https://www.mortalonlinemap.info/ There data has been very useful and enabled me to make this tool

## License
[MIT](https://choosealicense.com/licenses/mit/)
