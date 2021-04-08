import keyboard
from PIL import Image, ImageGrab
import pyperclip
from pyzbar.pyzbar import decode
import configparser
import os, sys
from os import path
import tkinter as tk

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
config = configparser.ConfigParser()
path_conf = "config.ini"

def createConfig(path):
    config.add_section("Settings")
    config.set("Settings", "Start", "F5")
    config.set("Settings", "Exit", "F10")
    with open(path, "w") as config_file:
        config.write(config_file)


if not os.path.exists(path_conf):
    createConfig(path_conf)


config.read(path_conf)
Start = config.get("Settings", "Start")
Exit = config.get("Settings", "Exit")

print("По умолчанию клавиша декодирования F5")
print("Изменить горячую клавишу можно в файле config.ini")
print("Сейчас:")
print("Декодировать:" + config.get("Settings", "Start"))
print("Выход:" + Exit)
print("################################")




def get_code():
    imgScreen = ImageGrab.grab()
    imgScreen.save('screenshot.png', 'png')
    img = Image.open(r'screenshot.png')
    code = decode(img)
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
    popup.geometry('320x100-25+200')
    popup.config(background='#003366')
    popup.after(1500, popup.destroy)
    popup.attributes("-topmost", True)
    popup.attributes("-alpha", 0.8)
    popup.overrideredirect(True)
    NORM_FONT = ("Arial Black", 11, 'bold')
    label = tk.Label(popup, background="#003366", foreground="black", text=msg, font=NORM_FONT, anchor='center', wraplength='250')
    label.pack(side="top", fill="both", expand=True)
    popup.mainloop()


if __name__ == '__main__':
    keyboard.add_hotkey(Start, get_code)
    keyboard.wait(Exit)