import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quitButton = tk.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack(side="bottom")
    
    def quit(self):
        """ Quit (or close window) callback """
        self.controller.state = "quit"
        self.master.quit()          # breaks app.mainloop() in the ApplicationController
