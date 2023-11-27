import cv2
from tkinter import filedialog
import tkinter as tk

def open_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    if file_path:
        image = cv2.imread(file_path)
        return image
    else:
        return None

def show_image(image):
    if image is not None:
        cv2.imshow('Selected Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("이미지를 선택하지 않았습니다.")

def read_selected_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            return image
        else:
            print("이미지를 읽을 수 없습니다.")
            return None
    else:
        return None
