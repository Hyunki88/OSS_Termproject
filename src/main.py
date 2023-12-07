import tkinter as tk
import subprocess

def run_filter1():
    subprocess.run(["python", "mosaic.py"])

def run_filter2():
    subprocess.run(["python", "liquify.py"])

def run_filter3():
    subprocess.run(["python", "lens.py"])

def run_filter4():
    subprocess.run(["python", "wave.py"])

def run_filter5():
    subprocess.run(["python","Edge.py"])

def on_closing():
    root.destroy()

root = tk.Tk()
root.title("Image Editor")
root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text="필터를 고르세요")
label.pack()

filter1_button = tk.Button(root, text="모자이크", command=run_filter1)
filter1_button.pack()

filter2_button = tk.Button(root, text="리퀴파이", command=run_filter2)
filter2_button.pack()

filter3_button = tk.Button(root, text="볼록렌즈", command=run_filter3)
filter3_button.pack()

filter4_button = tk.Button(root, text="물결필터", command=run_filter4)
filter4_button.pack()

filter5_button = tk.Button(root, text="선 필터", command=run_filter5)
filter5_button.pack()
root.mainloop()
