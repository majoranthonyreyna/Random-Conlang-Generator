import os
import logging
logging.basicConfig(filename="main.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s")

try:
	import project.control
	import project.settings

	def main():
		# Initialize globals
		project.settings.init()
		project.settings.baseDir = os.getcwd()

		# Start controller
		controller = project.control.ApplicationController()
		controller.run()

	if __name__ == "__main__":
		main()

except Exception as e:
	logging.exception("Caught at main")
	raise e
