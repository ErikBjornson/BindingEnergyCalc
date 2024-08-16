import tkinter as tk
from tkinter import ttk

p_mass = 1.007276466621  # proton mass
n_mass = 1.00866491595  # neutron mass
const_eW = 931.5  # binding energy per atomic unit of mass (mev)


class Application(tk.Tk):

    def __init__(self) -> None:

        super().__init__()

        size = [250, 370]  # size of window
        font = ("Helvetica", 10)  # text-style of labels

        # opening a chemical elements data file
        with open(".\\data\\ElementsList.txt", "r") as file:
            self.__mass = [word.split() for word in file.readlines()]
            file.close()
        
        # output labels (results will be displayed here)
        self.__lbls = [
            "Element : ",
            "Atomic weight : ",
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
            text="Element\'s data : ",
            font=font,
            padx=10,
            pady=10
        )
        self.__entryFrame.pack()

        # Next, widgets are created, which are added to self.__entryFrame (till creating self.__resultFrame).
        # Appropriate validators have been created for the input fields. 
        # Event handlers for entering information into fields have also been added.
        
        self.__massNum = tk.StringVar()  # field for entering mass number or isotope number
        self.__massNumEntry = ttk.Entry(
            self.__entryFrame,
            validate="key",
            validatecommand=(self.__entryFrame.register(self.__checkMassNumEntry), "%P"),
            textvariable=self.__massNum,
            width=4
        )
        self.__massNumEntry.grid(column=1, row=1)
        # self.__calculate() called every time input field data changes
        self.__massNum.trace_add("write", self.__calculate)
        
        
        self.__elemSymbol = ttk.Label(  # label for displaying chemical element's symbol (for Ferrum it's Fe)
                    self.__entryFrame,
                    text="X",
                    font=(font[0], 30)
                )
        self.__elemSymbol.grid(column=2, row=2, padx=10)
        
        
        self.__order = tk.StringVar()  # field for entering element serial number
        self.__orderEntry = ttk.Entry(
            self.__entryFrame,
            validate="key",
            validatecommand=(self.__entryFrame.register(self.__checkOrderNumEntry), "%P"),
            textvariable=self.__order,
            width=4
        )
        self.__orderEntry.grid(column=1, row=3)
        # self.__fillInfo() called every time input field data changes
        self.__order.trace_add("write", self.__fillInfo)
        
        
        self.__kernelFrame = tk.LabelFrame(  # internal frame - input field for atom kernel mass located here
            self.__entryFrame,
            text="Kernel weight : ",
            font=font,
            padx=7,
            pady=7
        )
        self.__kernelFrame.grid(columnspan=4, row=4, pady=10)
        
        
        self.__kernel = tk.StringVar()  # field for atom kernel mass
        self.__kernelEntry = ttk.Entry(
            self.__kernelFrame,
            validate="key",
            validatecommand=(self.__kernelFrame.register(self.__checkKernelMassEntry), "%P"),
            textvariable=self.__kernel,
            width=20
        )
        self.__kernelEntry.pack()
        # self.__calculate() called every time input field data changes
        self.__kernel.trace_add("write", self.__calculate)


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
                text=f"{elem}",
                font=font
            ) for elem in self.__lbls
        ]
        for item in self.__resultFrame_txts: item.pack()
    
    # verifying method :
    # entered data is positive integer and element's order number already entered
    def __checkMassNumEntry(self, P : str) -> bool:
        return P.isdigit() and int(P) > 0 and self.__orderEntry.get() != "" or P == ""
    
    # verifying method :
    # entered data is integer from 1 to 118 (existing chemical element numbers)
    def __checkOrderNumEntry(self, P : str) -> bool:
        return P.isdigit() and int(P) in range(1, 119) or P == ""
    
    # verifying method :
    # entered data is positive float
    def __checkKernelMassEntry(self, P : str) -> bool:
        try:
            return P == "" or float(P) > 0 and " " not in P
        except ValueError:
            return False
    
    # filling method :
    # filling in data about the chemical element
    def __fillInfo(self, *args) -> None:
        
        # clearing output fields if there no data in input fields
        if self.__orderEntry.get() == "":
            
            for j in range(2):
                self.__resultFrame_txts[j].config(text=f"{self.__lbls[j]}")
            
            self.__elemSymbol.config(text="X")
            return
        
        i = int(self.__orderEntry.get()) - 1  # index of the chosen chemical element in the self.__mass
        params = [self.__mass[i][0], self.__mass[i][1]]  # the chemical element's data (name and base kernel mass)
        
        for j in range(2):
            self.__resultFrame_txts[j].config(text=f"{self.__lbls[j]}{params[j]}")
        
        # changing the X-symbol on the chemical element's symbol
        self.__elemSymbol.config(text=f"{params[0].split('(')[1][:-1]}")


    # calculation method :
    # user enters data --> results displayed automatically
    # if input incorrect - results won't be displayed OR input will be unavailable
    def __calculate(self, *args) -> None:
        
        # clearing output fields if there no data in input fields
        if "" in [self.__massNumEntry.get(), self.__orderEntry.get()]:
            for j in range(2):
                self.__resultFrame_txts[2+j].config(text=self.__lbls[2+j])
            return

        Z = int(self.__orderEntry.get())  # element sequence number (charge number)
        A = int(self.__massNumEntry.get())  # mass number (isotope number, number of nucleons)
        
        # M_center - atomic nucleus mass
        if self.__kernelEntry.get() == "":
            M_center = float(self.__mass[Z-1][1])
        else:
            M_center = float(self.__kernelEntry.get())
        
        self.__resultFrame_txts[1].config(text=f"{self.__lbls[1]}{M_center}")
        
        Ne = A - Z  # neutrons count
        M_defect = abs((Z*p_mass + Ne*n_mass) - M_center)  # mass defect
        energy = M_defect*const_eW  # binding energy

        # displaying rounded results
        self.__resultFrame_txts[2].config(text=f"{self.__lbls[2]}{round(M_defect, 6)}")
        self.__resultFrame_txts[3].config(text=f"{self.__lbls[3]}{round(energy, 5)}")
