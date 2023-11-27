import cv2
from tkinter import filedialog
import tkinter as tk

def save_image(img):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        try:
            cv2.imwrite(file_path, img)
            print(f"이미지가 {file_path}에 저장되었습니다.")
        except Exception as e:
            print(f"이미지 저장 중 오류 발생: {e}")


