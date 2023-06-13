import tkinter as tk
from tkinter import ttk
from airfoildataframe import AirfoilDataFrame
from handler import Handler


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.handler = Handler()

        self.airfoil_dataframe = AirfoilDataFrame(self)
        self.airfoil_dataframe.pack(expand=True)

        self.geometry('1500x770+2+1')
        self.title('MGA802 Final project')

        self.lbl_weight = ttk.Label(self, text="Weight (Kg)")
        self.lbl_surface = ttk.Label(self, text="Surface (m^2)")
        self.lbl_wingspan = ttk.Label(self, text="Wingspan (m)")
        self.lbl_altitude = ttk.Label(self, text="Altitude (m)")

        self.lbl_weight.place(relx=0.01, rely=0.85, anchor='sw')
        self.lbl_surface.place(relx=0.01, rely=0.88, anchor='sw')
        self.lbl_wingspan.place(relx=0.01, rely=0.91, anchor='sw')
        self.lbl_altitude.place(relx=0.01, rely=0.94, anchor='sw')

        self.txt_weight = tk.Entry(self)
        self.txt_surface = tk.Entry(self)
        self.txt_wingspan = tk.Entry(self)
        self.txt_altitude = tk.Entry(self)

        self.txt_weight.place(relx=0.08, rely=0.85, anchor='sw')
        self.txt_surface.place(relx=0.08, rely=0.88, anchor='sw')
        self.txt_wingspan.place(relx=0.08, rely=0.91, anchor='sw')
        self.txt_altitude.place(relx=0.08, rely=0.94, anchor='sw')

        self.btn_stall_speed = tk.Button(self, text="Stall speed", command=self.compute_stall_speed)
        self.btn_optimal_speed = tk.Button(self, text="Optimal speed", command=self.compute_optimal_speed)

        self.btn_stall_speed.place(relx=0.18, rely=0.86, anchor='sw')
        self.btn_optimal_speed.place(relx=0.18, rely=0.9, anchor='sw')

    def populate_from_frame_to_objects(self):
        # wing aerodynamics
        self.handler.aero_obj.weight = float(self.txt_weight.get())
        self.handler.aero_obj.surface = float(self.txt_surface.get())
        self.handler.aero_obj.wingspan = float(self.txt_wingspan.get())

        # TEMPORARY VALUES
        self.handler.aero_obj.cl_max = 1.3
        self.handler.aero_obj.l_d_max = 122

        # Air
        self.handler.atm_obj.altitude = float(self.txt_altitude.get())

    def compute_stall_speed(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_stall_speed()

    def compute_optimal_speed(self):
        self.populate_from_frame_to_objects()
        self.handler.compute_optimal_speed()

    # def open_window(self):
    #     window = Window(self)
    #     window.grab_set()

    # def test(self):
    #     afdf = AirfoilDataFrame(self)
    #     afdf.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
