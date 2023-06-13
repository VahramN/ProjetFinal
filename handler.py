import math

import pandas as pd
from pandastable import Table
import matplotlib
import aerodynamics as aero
import atmosphere as atm
from airfoildataframe import AirfoilDataFrame

AIRFOILS_FILE = "airfoils.csv"


class Handler:
    def __init__(self):
        self.aero_obj = None
        self.atm_obj = None
        self.airfoil_obj = None

    def compute_stall_speed(self):
        v_stall = math.sqrt((self.aero_obj.weight / self.aero_obj.surface) *
                            2 / (self.atm_obj.compute_density() * self.aero_obj.cl_max))

        # temporary printing
        print(f"stall speed is: {v_stall} (m/s)")
        return v_stall

    def compute_optimal_speed(self):
        pass
