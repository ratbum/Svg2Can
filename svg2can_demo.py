from tkinter import *
from svg2can import *
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


if __name__ == '__main__':

	master = Tk()
	
	w = Canvas(master, width=160, height=248)
	w.pack()
	
	
	svg2can = Svg2Can()
	
	svg2can.draw_svg_from_file_on_canvas(w, os.path.join(__location__, './hangman.svg'))
	#left, top, width, height
	'''
	w.create_rectangle(15, 15, 12+15, 218+15, fill='black')
	w.create_rectangle(15, 15, 86+15, 15+12, fill='black')
	w.create_rectangle(15, 221, 130+15, 221+12, fill='black')
	'''
	
	mainloop()