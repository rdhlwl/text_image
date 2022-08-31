import tkinter as tk
from tkinter import filedialog, PhotoImage
import pytesseract as ts
ts.pytesseract.tesseract_cmd = r"C:\\Users\\Noord\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
from PIL import Image
import ctypes


#window
window = tk.Tk()
window.title("Image to Text")
window.geometry("750x750")
ctypes.windll.shcore.SetProcessDpiAwareness(1)    #quality
window.update_idletasks()


#image path
window.image_path = filedialog.askopenfilename(title = "Select an Image",
    filetypes= (("PNG Files", "*.png"),))
image_path_label = tk.Label(window, text = window.image_path,
    font = ("TkMenuFont", 18)).pack(padx = 10, pady = 10)


#tesseract read img
img = Image.open(window.image_path)
image_text = ts.image_to_string(img)


#show image
img1 = PhotoImage(file = window.image_path)
image_box = tk.Label(window, image = img1).pack()


#selectable entry with resulting text
text_box = tk.Text(window, width = 100, font = ("TKMenuFont", 16))
text_box.insert(1.0, image_text)
text_box.pack(padx = 10, pady = 10)


#run
window.mainloop()
