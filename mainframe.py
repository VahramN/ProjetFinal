import tkinter as tk
from tkinter import ttk
from airfoildataframe import AirfoilDataFrame
from handler import Handler
from aerodynamics import Aerodynamics
from atmosphere import Atmosphere


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.airfoil_dataframe = AirfoilDataFrame(self)
        self.airfoil_dataframe.pack(expand=True)

        self.handler = Handler()
        self.handler.airfoil_obj = self.airfoil_dataframe

        self.geometry('1500x770+2+1')
        self.title('MGA802 Final project')

        self.lbl_info = ttk.Label(self, text="Re=6M, Mach=0")
        self.lbl_info.place(relx=0.8, rely=0.78, anchor='ne')

        self.lbl_weight = ttk.Label(self, text="Weight (lb)")
        self.lbl_surface = ttk.Label(self, text="Surface (ft^2)")
        self.lbl_wingspan = ttk.Label(self, text="Wingspan (ft)")
        self.lbl_sweep_angle = ttk.Label(self, text="Sweep angle (deg)")
        self.lbl_thrust = ttk.Label(self, text="Jet Thrust (todo)")
        self.lbl_altitude = ttk.Label(self, text="Altitude (ft)")

        self.lbl_weight.place(relx=0.01, rely=0.83, anchor='sw')
        self.lbl_surface.place(relx=0.01, rely=0.86, anchor='sw')
        self.lbl_wingspan.place(relx=0.01, rely=0.89, anchor='sw')
        self.lbl_sweep_angle.place(relx=0.01, rely=0.92, anchor='sw')
        self.lbl_thrust.place(relx=0.01, rely=0.95, anchor='sw')
        self.lbl_altitude.place(relx=0.01, rely=0.98, anchor='sw')

        self.txt_weight = tk.Entry(self)
        self.txt_surface = tk.Entry(self)
        self.txt_wingspan = tk.Entry(self)
        self.txt_sweep_angle = tk.Entry(self, textvariable=tk.StringVar(self, value='0'))
        self.txt_thrust = tk.Entry(self)
        self.txt_altitude = tk.Entry(self)

        self.txt_weight.place(relx=0.1, rely=0.83, anchor='sw')
        self.txt_surface.place(relx=0.1, rely=0.86, anchor='sw')
        self.txt_wingspan.place(relx=0.1, rely=0.89, anchor='sw')
        self.txt_sweep_angle.place(relx=0.1, rely=0.92, anchor='sw')
        self.txt_thrust.place(relx=0.1, rely=0.95, anchor='sw')
        self.txt_altitude.place(relx=0.1, rely=0.98, anchor='sw')

        self.btn_stall_speed = tk.Button(self, text="Stall speed", command=self.compute_stall_speed)
        self.btn_takeoff_speed = tk.Button(self, text="Takeoff speed", command=self.compute_takeoff_speed)
        self.btn_optimal_speed = tk.Button(self, text="Optimal speed max distance", command=self.compute_optimal_speed)
        self.btn_takeoff_distance = tk.Button(self, text="Takeoff distance", command=self.compute_takeoff_distance)
        self.btn_landing_distance = tk.Button(self, text="Landing distance", command=self.compute_landing_distance)

        self.btn_stall_speed.place(relx=0.25, rely=0.835, anchor='sw')
        self.btn_takeoff_speed.place(relx=0.25, rely=0.875, anchor='sw')
        self.btn_optimal_speed.place(relx=0.25, rely=0.915, anchor='sw')
        self.btn_takeoff_distance.place(relx=0.25, rely=0.955, anchor='sw')
        self.btn_landing_distance.place(relx=0.25, rely=0.995, anchor='sw')

    def populate_from_frame_to_objects(self):
        selected_row = self.airfoil_dataframe.table.getSelectedRow()
        cl_max = self.airfoil_dataframe.dataset_airfoils.at[selected_row, 'Cl max']
        l_d_max = self.airfoil_dataframe.dataset_airfoils.at[selected_row, 'Cl/Cd max']
        # wing aerodynamics
        self.handler.aero_obj = Aerodynamics(float(self.txt_weight.get()),
                                             float(self.txt_surface.get()),
                                             float(self.txt_wingspan.get()),
                                             float(self.txt_sweep_angle.get()),
                                             float(self.txt_thrust.get()),
                                             cl_max=float(cl_max),
                                             l_d_max=float(l_d_max))

        # Air
        # convert altitude from foot to meter
        altitude = float(self.txt_altitude.get()) * 0.3048
        self.handler.atm_obj = Atmosphere(altitude)

    def compute_stall_speed(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_stall_speed()

    def compute_takeoff_speed(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_takeoff_speed()

    def compute_optimal_speed(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_optimal_speed()

    def compute_takeoff_distance(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_takeoff_distance()

    def compute_landing_distance(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_landing_distance()

    # def open_window(self):
    #     window = Window(self)
    #     window.grab_set()

    # def test(self):
    #     afdf = AirfoilDataFrame(self)
    #     afdf.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
