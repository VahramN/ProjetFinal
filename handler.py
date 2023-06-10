import math

import pandas as pd
from pandastable import Table
import matplotlib
import aerodynamics as aero
import atmosphere as atm

AIRFOILS_FILE = "airfoils.csv"


class Handler:
    def __init__(self):
        self.aero_obj = aero.Aerodynamics()
        self.atm_obj = atm.Atmosphere()
        self.dataset_airfoils = pd.read_csv(AIRFOILS_FILE, sep=',', header=0)

    def calc_stall_speed(self):
        v_stall = math.sqrt((self.aero_obj.weight / self.aero_obj.surface) *
                            2 / (self.atm_obj.density() * self.aero_obj.cl_max))

        # temporary printing
        print(f"stall speed is: {v_stall} (m/s)")
        return v_stall

    def calc_optimal_speed(self):
        pass
