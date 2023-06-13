import tkinter as tk
from pandastable import Table
import pandas as pd

AIRFOILS_FILE = "airfoils.csv"


class AirfoilDataFrame(tk.Frame):
    def __init__(self, parent=None):
        self.parent = parent
        tk.Frame.__init__(self)
        self.main = self.master
        # self.main.geometry('1350x200+1+1')
        f = tk.Frame(self.main)
        f.pack(fill=tk.BOTH, expand=1)

        self.dataset_airfoils = pd.read_csv(AIRFOILS_FILE, sep=',', header=0)
        self.table = pt = Table(f, dataframe=self.dataset_airfoils, showtoolbar=True, showstatusbar=True)
        pt.show()
        return
