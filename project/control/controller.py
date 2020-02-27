class ApplicationController:
	""" Runs the entire application """
	def __init__(self):
		self.state = "menu"

	def run(self):
		print("##### Random Conlang Generator #####")
		while self.state != "quit":
			c = input("Type q to quit: ")
			if c == "q" or c == "Q":
				self.state = "quit"

		self.quit()

	def quit(self):
		print("Ending...")
