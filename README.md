# A program for calculating the binding energy of chemical elements (BindingEnergyCalc)

![Static Badge](https://img.shields.io/badge/ErikBjornson-BindingEnergyCalc-BindingEnergyCalc)
![GitHub top language](https://img.shields.io/github/languages/top/ErikBjornson/BindingEnergyCalc)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ErikBjornson/BindingEnergyCalc)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/ErikBjornson/BindingEnergyCalc)

This GitHub repository contains a Python project that creates a graphical user interface (GUI) using the tkinter library. The GUI displays a window with two `tkinter.LabelFrame()` objects: *"Element's data"* and *"Results"*. The application is designed to display data about chemical elements based on user input.

## Project Overview

The program is divided into two main sections:

### Element's data Section

The "Element's data" section is used for inputting data into the program. It contains the following components:

- **Atomic Number Input**: This field accepts the atomic number of the selected chemical element. When a valid atomic number is entered, the symbol of the corresponding element is displayed in the symbol text field.

- **Symbol Text Field**: This field displays the symbol of the chemical element corresponding to the atomic number entered in the atomic number input field. The symbol is updated automatically as the atomic number changes. The symbol is taken from the periodic table of chemical elements created by Dmitri Mendeleev.

- **Isotope Number Input**: This field accepts the isotope number (mass number or isotope number) of the selected chemical element. When a valid isotope number is entered, the mass defect and binding energy of the atoms for the given chemical element are calculated. By default, the mass of the nucleus is the tabular value of the mass of the atom.

- **Nucleus Mass Input**: This field allows the user to input the mass of the nucleus of the isotope if it differs from the tabular value. When a valid mass is entered, the mass of the nucleus label in the "Results" section is updated, and the mass defect and binding energy are recalculated.

### Results Section

The "Results" section displays results of the calculations and additional information about the selected chemical element based on the user's input. It contains the following components:

- **Element Name Label**: This label displays the name of the chemical element corresponding to the atomic number entered in the "Element's Data" section.

- **Nucleus Mass Label**: This label displays the mass of the nucleus of the selected chemical element. By default, it displays the tabular value of the mass of the atom. If a valid mass is entered in the nucleus mass input field, this label is updated to display the new mass.

- **Mass Defect Label**: This label displays the mass defect of the selected chemical element. The mass defect is calculated automatically when a valid isotope number is entered in the isotope number input field or when a valid mass is entered in the nucleus mass input field.

- **Binding Energy Label**: This label displays the binding energy of the selected chemical element. The binding energy is calculated automatically when a valid isotope number is entered in the isotope number input field or when a valid mass is entered in the nucleus mass input field.

## Input Validation

The application implements input validation to ensure that the user enters valid data. 

For every single input field:
- Only positive values are allowed;
- Spaces are not allowed.

The validation rules for each input field are as follows:

- Atomic Number Field:
    - Only integers are allowed;
    - The value must be between 1 and 118 (since these are the atomic numbers of known chemical elements);

- Mass Number Field:

    - Only integers are allowed;
    - There is no fixed range for the value;

- Nucleus Mass Field:
    - Only floating-point numbers are allowed.

## Appearance

The following image shows the program window without the entered data:

![Just program window. There is no data](/assets/NoData.png)

The next two images show examples of calculations for some chemical elements (for `Ferrum (Iron)` and `Uranium`):

![Ferrum calculations](/assets/FerrumData.png)
![Uranium calculations](/assets/UraniumData.png)

## Usage

1. Clone the repository to your local machine.

2. Ensure you have Python and the tkinter library installed.

3. Run `src/main.py` file using a Python interpreter.

4. Use the input fields to enter the required data.

5. View the calculated mass defect and binding energy, as well as the chemical element information, in the *"Results"* section.

## Code Comments

The codebase includes comments that provide additional insights into how the program works. I recommend reading these comments to gain a deeper understanding of the program's functionality. 

## Dependencies

- Python 3.x
- tkinter library
