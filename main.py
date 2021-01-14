from pyxelate import Pyxelate
from skimage import io
import matplotlib.pyplot as plt
import tkinter as tk

def main():
	img = io.imread(fname_label)
	height, width, _ = img.shape 
	factor = 14
	colors = colors_label_format
	dither = True

	p = Pyxelate(height // factor, width // factor, colors, dither)
	img_small = p.convert(img) 

	_, axes = plt.subplots(1, 2, figsize=(16, 16))
	axes[0].imshow(img)
	axes[1].imshow(img_small)
	# i.savefig("res.jpg")
	plt.show()

window = tk.Tk()
window.geometry("400x400")
window.title("Pyxel Art generator")
window.resizable(width=True, height=True)
fname_label = tk.Label(window, text="\n\nВведите название файла:\n", font=("Arial", 12))
fname_entry = tk.Entry(window, width=40)
fname_label_format = tk.Label(window, text="(допустимые форматы: .png и .jpg) \n", font=("Arial", 12), fg="orange")
colors_label = tk.Label(window, text="Введите количество цветов:\n", font=("Arial", 12))
colors_entry = tk.Entry(window, width=20)
colors_label_format = tk.Label(window, text="(от 2 до 32)\n", font=("Arial", 12), fg="orange")
button = tk.Button(window, text="Пикселизировать!", font=("Arial", 12), command=main)

fname_label.pack()
fname_entry.pack()
fname_label_format.pack()
colors_label.pack()
colors_entry.pack()
colors_label_format.pack()
button.pack()
window.mainloop()