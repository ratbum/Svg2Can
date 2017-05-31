from tkinter import *
from svg2can import *
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


if __name__ == '__main__':

	master = Tk()
	
	w = Canvas(master, width=160, height=248)
	w.pack()
	
	svg2can = Svg2Can()
	svg2can.draw_svg_from_file_on_canvas(w, os.path.join(__location__, './hangman.svg'))
	
	mainloop()