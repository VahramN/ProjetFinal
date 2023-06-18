import math


class Handler:
    def __init__(self):
        self.aero_obj = None
        self.atm_obj = None
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

    def take_of_distance(self):
        TO_distance = 20.9 * (self.aero_obj.weight / self.aero_obj.surface) * \
                      (self.aero_obj.weight / self.aero_obj.thrust) * (1 / self.aero_obj.cl_max) + \
                      87 * math.sqrt(self.aero_obj.weight / (1 / self.aero_obj.cl_max))
        return TO_distance

    def coeff_K(self):
        e = 0.8
        PI = 3.14
        k = 1 / (PI * e * self.aero_obj.coeff_aspect_ratio())
        return k

    def coeff_drag0(self):
        cd0 = 1 / (4 * self.coeff_K() * self.aero_obj.l_d_max)
        return cd0
