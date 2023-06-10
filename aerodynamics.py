class Aerodynamics:

    def __init__(self):
        self._weight = 0.
        self._surface = 0.
        self._wingspan = 0.
        self._cl_max = 0.
        self._l_d_max = 0.

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

    def calc_stall_speed(self):
        pass
