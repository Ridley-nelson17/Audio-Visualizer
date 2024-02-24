import matplotlib as plotter
from os import path
import tkinter

# Set environment variables
__here__ = path.abspath(path.dirname(__file__))
__BIN__ = path.join(__here__, 'bin')


import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import sounddevice as sd

class AudioVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Visualizer")
        self.root.geometry("800x400")

        self.buffer_size = 1024  # Adjust this value as needed
        self.num_channels = 2  # Stereo

        self.fig_width = 8
        self.fig_height = 4
        self.fig_aspect_ratio = self.fig_width / self.fig_height

        self.fig = Figure(figsize=(self.fig_width, self.fig_height))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.stream = sd.InputStream(channels=self.num_channels, callback=self.audio_callback)
        self.stream.start()

    def calculate_figure_size(self):
        # Calculate figure size dynamically if needed
        pass

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.ax.clear()
        self.ax.plot(np.arange(len(indata)), indata)
        self.ax.set_title('Audio Visualizer')
        self.ax.set_xlabel('Samples')
        self.ax.set_ylabel('Amplitude')
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioVisualizer(root)
    root.mainloop()
