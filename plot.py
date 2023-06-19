import numpy as np
import matplotlib.pyplot as plt


def plot_stall_speed(y, y_name, x, x_name):
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        return
    plt.figure().set_figwidth(9)
    plt.plot(x, y)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    # plt.legend()
    plt.show()
