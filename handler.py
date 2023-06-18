import math
from atmosphere import Atmosphere

class Handler:
    def __init__(self):
        self.aero_obj = None
        self.atm_obj = None
        self.atm_0_obj = Atmosphere(0)
        self.airfoil_obj = None

    def convert_speed_imperial_to_knots(self, speed):
        return speed / 1.687811

    def compute_stall_speed(self):
        v_stall = math.sqrt((self.aero_obj.weight / self.aero_obj.surface) *
                            2 / (self.atm_obj.compute_density_imperial() * self.aero_obj.cl_max))
        v_stall = self.convert_speed_imperial_to_knots(v_stall)
        # temporary printing
        print(f"stall speed is: {v_stall} (kts)")
        return v_stall

    def compute_takeoff_speed(self):
        v_takeoff = 1.2 * self.compute_stall_speed()  # already in kts
        # temporary printing
        print(f"takeoff speed is: {v_takeoff} (kts)")
        return v_takeoff

    def compute_optimal_speed(self):
        v_optimal = math.sqrt((2 * self.aero_obj.weight) / (self.atm_obj.compute_density_imperial() * self.aero_obj.surface)) * \
                    (3 * self.coeff_K() / self.coeff_drag0()) ** 0.25
        v_optimal = self.convert_speed_imperial_to_knots(v_optimal)
        # temporary printing
        print(f"optimal speed is: {v_optimal} (kts)")
        return v_optimal

    def compute_takeoff_distance(self):
        density_ratio = self.atm_obj.compute_density_imperial() / self.atm_0_obj.compute_density_imperial()
        TOP = (self.aero_obj.weight / self.aero_obj.surface) * \
              (1 / self.aero_obj.cl_max) * \
              (self.aero_obj.weight / self.aero_obj.thrust) * (1 / density_ratio)

        takeoff_distance = 20.9 * TOP + 87 * math.sqrt(TOP * (self.aero_obj.thrust / self.aero_obj.weight))
        # temporary printing
        print(f"takeoff distance is: {takeoff_distance} (ft)")
        return takeoff_distance

    def compute_landing_distance(self):
        density_ratio = self.atm_obj.compute_density_imperial() / self.atm_0_obj.compute_density_imperial()
        LP = (self.aero_obj.weight / self.aero_obj.surface) * (1 / (density_ratio * self.aero_obj.cl_max))
        landing_distance = 118 * LP + 400
        # temporary printing
        print(f"landing distance is: {landing_distance} (ft)")
        return landing_distance

    def coeff_K(self):
        e = 0.8
        PI = 3.14
        k = 1 / (PI * e * self.aero_obj.coeff_aspect_ratio())
        return k

    def coeff_drag0(self):
        cd0 = 1 / (4 * self.coeff_K() * self.aero_obj.l_d_max)
        return cd0
