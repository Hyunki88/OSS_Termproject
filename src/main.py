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
root.minsize(300, 300)
root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, height=3, text="필터를 고르세요", font=5, fg="blue")
label.pack(pady = 10)

filter1_button = tk.Button(root, width=10, text="모자이크", command=run_filter1)
filter1_button.pack(pady = 5)

filter2_button = tk.Button(root, width=10, text="리퀴파이", command=run_filter2)
filter2_button.pack(pady = 5)

filter3_button = tk.Button(root, width=10, text="볼록렌즈", command=run_filter3)
filter3_button.pack(pady = 5)

filter4_button = tk.Button(root, width=10, text="물결필터", command=run_filter4)
filter4_button.pack(pady = 5)

filter5_button = tk.Button(root, width=10, text="선 필터", command=run_filter5)
filter5_button.pack(pady = 5)


root.mainloop()
