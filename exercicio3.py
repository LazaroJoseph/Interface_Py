from tkinter import *
class Application:
    def __init__(self, master=None):
      self.widget1 = Frame(master)
      self.widget1.pack()
      self.msg = Label(self.widget1, text="LACTEA")
      self.msg.pack ()
root = Tk()
Application(root)
root.mainloop()