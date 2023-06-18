class Aerodynamics:

    def __init__(self, weight, surface, wingspan, thrust, cl_max, l_d_max):
        self._weight = weight
        self._surface = surface
        self._wingspan = wingspan
        self._thrust = thrust
        self._cl_max = cl_max
        self._l_d_max = l_d_max

    def coeff_aspect_ratio(self):
        A = (self._wingspan ** 2) / self._surface
        return A

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, value):
        self._surface = value

    @property
    def wingspan(self):
        return self._wingspan

    @surface.setter
    def wingspan(self, value):
        self._wingspan = value

    @property
    def thrust(self):
        return self._thrust

    @surface.setter
    def thrust(self, value):
        self._thrust = value

    @property
    def cl_max(self):
        return self._cl_max

    @cl_max.setter
    def cl_max(self, value):
        self._cl_max = value

    @property
    def l_d_max(self):
        return self._l_d_max

    @l_d_max.setter
    def l_d_max(self, value):
        self._l_d_max = value

