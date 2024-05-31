import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self) -> None:

        super().__init__()

        size = [230, 240]  # size of window
        font = ("Helvetica", 10)  # text-style of all labels

        # opening a chemical elements data file
        with open(".\\BindingEnergyCalc\\data\\ElementsList.txt", "r") as file:
            self.__mass = [word.split() for word in file.readlines()]
            file.close()
        
        # output label (results will be displayed here)
        self.__lbls = [
            "Atomic weight : ",
            "Center\'s weight : ",
            "Element : ",
            "Mass defect : ",
            "Energy : "
        ]

        self.title("Binding Energy")
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)

        # data layout for only one component -
        # entry where number of element will be entered
        self.__entryFrame = tk.LabelFrame(
            self,
            text="Data (element\'s number) : ",
            font=font,
            padx=10,
            pady=10
        )
        self.__entryFrame.pack()

        self.__texter = tk.StringVar()  # string variable constructor (for input field validating)
        # data entry filter that restricts the input of only integers
        self.__vcmd = (self.__entryFrame.register(self.__checkEntry), "%P")
        # field for entering element serial number
        self.__entry = ttk.Entry(
            self.__entryFrame,
            validate="key",
            validatecommand=self.__vcmd,
            textvariable=self.__texter,
            width=25
        )
        self.__entry.grid(column=1, row=1)
        # self.__calculate() called every time input field data changes
        self.__texter.trace_add("write", self.__calculate)

        # layout for displaying calculation results (here will be labels)
        self.__resultFrame = tk.LabelFrame(
            self,
            text="Results : ",
            font=font,
            padx=10,
            pady=10
        )
        self.__resultFrame.pack()

        # creating labels for calculation results layout
        self.__resultFrame_txts = [
            tk.Label(
                self.__resultFrame,
                text=f"{self.__lbls[i]}",
                font=font
            ) for i in range(len(self.__lbls))
        ]
        for item in self.__resultFrame_txts: item.pack()
    
    # verifying method :
    # entered data is integer from 1 to 118 (existing chemical element numbers)
    def __checkEntry(self, P : str) -> bool:
        return P.isdigit() and int(P) in range(1, 119) or P == ""

    # calculation method :
    # user enters element number --> results displayed automatically
    # if input incorrect - results won't be displayed OR input will be unavailable
    def __calculate(self, *args) -> None:
        if self.__entry.get() == "":
            for j in range(5):
                self.__resultFrame_txts[j].config(text=self.__lbls[j])
            return
        i = int(self.__entry.get()) - 1
        params = [i+1, self.__mass[i][1], self.__mass[i][0]]
        for j in range(3):
            self.__resultFrame_txts[j]\
                .config(text=self.__lbls[j]+f"{params[j]}")

        p_mass = 1.007276466621  # proton mass
        n_mass = 1.00866491595  # neutron mass
        const_eW = 931.5  # binding energy per atomic unit of mass (mev)

        Z = i + 1  # element sequence number (charge number)
        A = round(float(self.__mass[i][1]), 0)  # mass number (number of nucleons)
        M_center = float(self.__mass[i][1])  # atomic nucleus mass
        
        Ne = A - Z  # neutrons count
        M_defect = (Z*p_mass + Ne*n_mass) - M_center  # mass defect
        energy = M_defect*const_eW  # binding energy

        results = [round(M_defect, 6), round(energy, 5)]  # rounded results

        for j in range(2):
            self.__resultFrame_txts[-2+j].configure(
                text=f"{self.__lbls[-2+j]}{results[-2+j]}"
            )
