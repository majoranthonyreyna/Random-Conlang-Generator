import tkinter as tk
import project.gui

class ApplicationController:
	""" Runs the entire application """
	def __init__(self):
		self.state = "menu"
		self.root = tk.Tk()

	def run(self):
		print("##### Random Conlang Generator #####")

		# Setup tkinter
		app = project.gui.GUI(self.root, self)
		self.root.protocol("WM_DELETE_WINDOW", app.quit)
		self.root.title("Random Conlang Generator")
		self.root.geometry("400x400")		# Default Width x Height

		# Run tkinter
		app.mainloop()

		self.quit()

	def quit(self):
		print("Ending...")
