from customtkinter import *
import os


class FunctionEditor():

	def __init__(self):
		self.root = CTk()
		set_appearance_mode("dark")
		set_default_color_theme("green")
		self.commandName = CTkEntry(self.root)
		self.commandName.configure(placeholder_text="Command Name")
		self.dropdown = StringVar()
		self.dropdown.set("Reply")
		self.commandMode = CTkOptionMenu(
		    self.root,
		    variable=self.dropdown,
		    values=["Reply", "Ban Command", "Kick Command"])
		self.commandMode.configure(width="15", height="1")
		self.commandName.pack(pady=5)
		self.commandResponse = CTkEntry(self.root)
		self.commandResponse.configure(placeholder_text="Command Response")
		self.commandResponse.pack(pady=9)
		self.commandMode.pack(pady=5)
		self.dropdownToIndex = {"Reply": 0, "Ban Command": 1, "Kick Command": 2}
		self.b = CTkButton(self.root,
		                   text="Create Command",
		                   command=self.createCommand)
		self.b.pack(pady=10)
		with open('app.ini', 'r') as f:
			config = f.read()
		botHelper = {"False": True, "True": False}
		hasHelpCommand = True
		for settings in config.split('\n'):
			setting = settings.split('=')
			if setting[0] == "NoDefaultHelpCommand":
				hasHelpCommand = botHelper[setting[1]]
		if hasHelpCommand:
			self.commandsCreated = ['help']
		else:
			self.commandsCreated = []
		with open("app_funcs.ini", "r") as f:
			d = f.read()

		for thing in d.split("\n"):
			if thing == "":
				continue
			newLabel = CTkLabel(self.root, text="Command: " + thing.split(",")[0])
			newLabel.configure(width=96)
			newLabel.pack()
			self.commandsCreated.append(thing.split(',')[0])

		self.nb = CTkButton(self.root, text="Compile", command=self.compile)
		self.cb = CTkButton(self.root,
		                    text="Remove All Commands",
		                    command=self.clear)
		self.cb.pack(side=BOTTOM, pady=5)
		self.nb.pack(side=BOTTOM, pady=5)
		self.root.attributes("-fullscreen", True)
		self.root.configure
		self.root.mainloop()

	def createCodeCommand(self):
		if self.commandName.get() in self.commandsCreated:
			return
		with open("app_funcs.ini", "r") as f:
			d = f.read()
		starter = d + "\n"
		if d == "":
			starter = ""
		with open("app_funcs.ini", "w") as f:
			a = str(self.commandName.get())
			self.commandsCreated.append(a)
			b = self.dropdownToIndex[str(self.dropdown.get())]
			c = str(self.commandResponse.get())
			f.write(f"{starter}{a},{b},{c}")

	def clear(self):
		open("app_funcs.ini", "w").close()

	def compile(self):
		self.root.destroy()
		#open build.sh/build.bat in the correct operating system
		try:
			os.system("clear")
			os.system("chmod +x .\build.sh")
			os.system("build.sh")
		except:
			os.system("cls")
			os.system("build.bat")

	def createCommand(self):
		if len(self.commandName.get().split(' ')) != 1:
			return
		if self.commandResponse.get() == "":
			return
		if self.commandName.get() in self.commandsCreated:
			return
		if self.commandName.get() == "":
			return
		newLabel = CTkLabel(self.root, text=f"Command: {self.commandName.get()}")
		newLabel.configure(width=96)
		newLabel.pack()
		self.createCodeCommand()


FunctionEditor()
