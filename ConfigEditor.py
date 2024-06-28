from customtkinter import *
import tkinter as tk
class ConfigEditor:
	def __init__(self):
		self.root=CTk()
		set_appearance_mode("dark")
		set_default_color_theme("green")
		self.Title=CTkLabel(self.root, text="Config Editor", font=("Arial",25))
		
		self.Title.pack(pady=10,anchor="n")
		
		self.has_help=StringVar(value="on")
		self.has_help.set("on")
		self.NDHC=CTkSwitch(self.root, text="Use Default Help Command.", variable=self.has_help, command=self.switch,onvalue="on",offvalue="off", font=("Arial",25))
		
		self.NDHC.pack(pady=10)
		
		self.Token=CTkEntry(self.root)
		self.Status=CTkEntry(self.root)
		self.Use=True
		self.Token.configure(
			width=450,
			height=45,
			placeholder_text="Discord Token"
		)
		self.Status.configure(
			width=450,
			height=45,
			placeholder_text="Discord App Status"
		)
		
		self.Token.pack(pady=10)
		self.Status.pack(pady=10)
		self.Prefix=StringVar(value="")
		self.Prefix.set("!")
		self.PrefixMenu=CTkOptionMenu(self.root,variable=self.Prefix, values=["?","!","/","#","*","$"])
		self.PrefixMenu.pack(pady=10)
		
		self.Apply=CTkButton(self.root, text="Apply Changes", command=self.apply)
		self.Apply.pack(anchor="center")
		self.root.mainloop()
	def apply(self):
		with open("app.ini","w") as f:
			f.write("Prefix="+self.Prefix.get())
			f.write("\nToken="+self.Token.get())
			f.write("\nNoDefaultHelpCommand="+str(not self.Use))
			f.write("\nStatus="+self.Status.get())
	def switch(self):
		self.Use=not self.Use
		
ConfigEditor()