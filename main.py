import time
import tkinter as tk
from tkinter import *

import cv2
import keyboard
import numpy as np
import PIL
import pyautogui
import pyperclip
from cv2 import data
from pyzbar.pyzbar import decode

print("Ctrl+1 для декодирования QR")
print("Ctrl+0 для выхода")


def get_code():
    pyautogui.screenshot('screenshot.png')
    img = cv2.imread('screenshot.png')
    code = decode(img)
    # print(code)
    if len(code) == 0:
        message = "Код не распознан!"
        popupmsg(message)
    else:
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
            pyperclip.copy(myData)
            message = "Ваш код {} скопирован в буфер обмена. Для вставки используйте Ctrl+V".format(myData)
            popupmsg(message)


def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry('500x200')
    popup.config(bg='#aaffff')
    popup.attributes("-topmost", True)
    popup.wm_title("Qr code decoder")
    NORM_FONT = ("Helvetica", 10)
    label = tk.Label(popup, text=msg, font=NORM_FONT, bg='#aaffff')
    label.pack(side="top", fill="x", pady=30)
    B1 = tk.Button(popup, text="   Ok!   ", command=popup.destroy,)
    B1.pack()
    popup.mainloop()


keyboard.add_hotkey('Ctrl + 1', get_code)
keyboard.wait('Ctrl + 0')
