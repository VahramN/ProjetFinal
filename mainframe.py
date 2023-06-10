import tkinter as tk
from tkinter import ttk
import handler


handler = handler.Handler()

# need to bring under the class


def populate_from_frame_to_objects():
    # wing aerodynamics
    handler.aero_obj.weight = float(txt_weight.get())
    handler.aero_obj.surface = float(txt_surface.get())
    handler.aero_obj.wingspan = float(txt_wingspan.get())
    # temporary values
    handler.aero_obj.cl_max = 1.3
    handler.aero_obj.l_d_max = 122

    # Air
    handler.atm_obj.altitude = float(txt_altitude.get())


def calc_stall_speed():
    populate_from_frame_to_objects()
    handler.calc_stall_speed()


def calc_optimal_speed():
    populate_from_frame_to_objects()
    handler.calc_optimal_speed()


root = tk.Tk()
root.geometry("500x500")  # width x height
root.title("MGA802 Final project")  # Adding a title

lbl_weight = tk.Label(root, text="Weight (Kg)")
lbl_surface = tk.Label(root, text="Surface (m^2)")
lbl_wingspan = tk.Label(root, text="Wingspan (m)")
lbl_altitude = tk.Label(root, text="Altitude (m)")

lbl_weight.grid(row=0, column=0, sticky='W', pady=2)
lbl_surface.grid(row=1, column=0, sticky='W', pady=2)
lbl_wingspan.grid(row=2, column=0, sticky='W', pady=2)
lbl_altitude.grid(row=3, column=0, sticky='W', pady=2)

# entry widgets, used to take entry from user
txt_weight = tk.Entry(root)
txt_surface = tk.Entry(root)
txt_wingspan = tk.Entry(root)
txt_altitude = tk.Entry(root)

# this will arrange entry widgets
txt_weight.grid(row=0, column=1, pady=2)
txt_surface.grid(row=1, column=1, pady=2)
txt_wingspan.grid(row=2, column=1, pady=2)
txt_altitude.grid(row=3, column=1, pady=2)

# button widget
btn_stall_speed = tk.Button(root, text="Stall speed", command=calc_stall_speed)
btn_optimal_speed = tk.Button(root, text="Optimal speed", command=calc_optimal_speed)

# arranging button widgets
btn_stall_speed.grid(row=10, column=0, sticky='E')
btn_optimal_speed.grid(row=10, column=1, sticky='E')

# infinite loop which can be terminated
# by keyboard or mouse interrupt
tk.mainloop()
