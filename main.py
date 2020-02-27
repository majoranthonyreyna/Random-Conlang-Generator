import logging
logging.basicConfig(filename="main.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s")

try:
	import project.control

	def main():
		controller = project.control.ApplicationController()
		controller.run()

	if __name__ == "__main__":
		main()

except Exception as e:
	logging.exception("Caught at main")
	raise e
