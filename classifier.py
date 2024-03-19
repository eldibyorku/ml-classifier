import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Assuming 'dataset_0_100.csv' exists and is formatted correctly.
df = pd.read_csv('dataset_0_100.csv')

# Initialize weights and biases as global variables
weight_1_1 = 0.0
weight_2_1 = 0.0
weight_1_2 = 0.0
weight_2_2 = 0.0
bias_1 = 0.0
bias_2 = 0.0

def classify_vectorized():
    """Vectorized classification based on current weights and biases."""
    output_1 = df['x'] * weight_1_1 + df['y'] * weight_2_1 + bias_1
    output_2 = df['x'] * weight_1_2 + df['y'] * weight_2_2 + bias_2
    return output_1 > output_2

def update_value(val):
    """Callback function for slider value change."""
    global weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2
    # Update weights and biases from sliders
    weight_1_1 = weight_1_1_slider.get()
    weight_1_2 = weight_1_2_slider.get()
    weight_2_1 = weight_2_1_slider.get()
    weight_2_2 = weight_2_2_slider.get()
    bias_1 = bias_1_slider.get()
    bias_2 = bias_2_slider.get()
    update_plot()

def update_plot():
    """Updates the plot based on current weights, biases, and classified colors."""
    classified = classify_vectorized()
    plot.clear()
    plot.scatter(df.loc[classified, 'x'], df.loc[classified, 'y'], color='red', label='Class 1')
    plot.scatter(df.loc[~classified, 'x'], df.loc[~classified, 'y'], color='blue', label='Class 0')
    plot_setup()

def plot_setup():
    """Sets up standard plot settings."""
    plot.set_title('Plot of Points')
    plot.set_xlabel('X axis')
    plot.set_ylabel('Y axis')
    plot.grid(True)
    plot.legend()
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Weights & Biases Control")

# Create a figure for the plot
fig = Figure(figsize=(5, 4), dpi=100)
plot = fig.add_subplot(1, 1, 1)



# Create a canvas for the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Define and pack sliders
weight_1_1_slider = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient='horizontal', label='weight_1_1', command=update_value)
weight_1_1_slider.pack()
# Repeat for other sliders...
weight_1_2_slider = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient='horizontal', label='weight_1_2', command=update_value)
weight_1_2_slider.pack()
weight_2_1_slider = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient='horizontal', label='weight_2_1', command=update_value)
weight_2_1_slider.pack()
weight_2_2_slider = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient='horizontal', label='weight_2_2', command=update_value)
weight_2_2_slider.pack()
bias_1_slider = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient='horizontal', label='bias_1', command=update_value)
bias_1_slider.pack()
bias_2_slider = tk.Scale(root, from_=-10, to=10, resolution=0.01, orient='horizontal', label='bias_2', command=update_value)
bias_2_slider.pack()

# Initial plot setup
plot_setup()
# Start the Tkinter event loop
root.mainloop()
