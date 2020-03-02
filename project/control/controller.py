import tkinter as tk
import project.gui
import project.settings

class ApplicationController:
	""" Runs the entire application """
	def __init__(self):
		self.state = "menu"
		self.root = tk.Tk()

	def run(self):
		print("##### Random Conlang Generator #####")

		# Setup tkinter
		app = project.gui.GUI(self.root, self)
		self.root.protocol("WM_DELETE_WINDOW", app.quit)	# Connect close window to app.quit
		self.root.title("Random Conlang Generator")			# Set title of window
		self.root.geometry("400x400")						# Default Width x Height
		icon = tk.PhotoImage(file=project.settings.baseDir + "/data/pictures/alpha.png")		# Define window icon
		self.root.iconphoto(False, icon)					# Add window icon

		# Run tkinter
		app.mainloop()

		self.quit()

	def quit(self):
		print("Ending...")
