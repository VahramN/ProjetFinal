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

    def compute_takeoff_speed(self):
        v_takeoff = 1.2 * self.compute_stall_speed()
        return v_takeoff

    def take_of_distance(self):
        TO_distance = 20.9*(self.aero_obj.weight / self.aero_obj.surface)*\
        (self.aero_obj.weight / self.aero_obj.thrust)*(1/self.aero_obj.cl_max)+\
        87* math.sqrt(self.aero_obj.weight /(1/self.aero_obj.cl_max))
        return TO_distance

    def coeff_K(self):
        e = 0.8
        PI=3.14
        k = 1/PI*e*self.aero_obj.wingspan
        return k
    def drag_coeff_0(self):
        CD0=4* self.coeff_K()/self.aero_obj.cl_max**2
        return CD0
    def compute_optimal_speed(self):
        v_optimal = math.sqrt(self.aero_obj.weight/0.5*self.atm_obj.compute_density()*\
                     self.aero_obj.surface)*(3*self.coeff_K()/self.drag_coeff_0())**0.25
        return v_optimal
#le coefficient de trainée CD=CD0+KCL**2
