from tkinter import *
import os
class FunctionEditor():
	def __init__(self):
		self.root=Tk()
		self.root.geometry("960x540")
		self.debug=Text(self.root)
		self.debug.configure(background='black')
		self.debug.configure(fg="white")
		self.commandName=Entry(self.root)
		self.commandName.config(
			bg="#000000",
			fg="#FFFFFF",
			placeholder="Command Name"
		)
		self.dropdown=StringVar()
		self.dropdown.set("Reply")
		self.commandMode=OptionMenu(self.root,self.dropdown,*["Reply","Ban Command","Kick Command"])
		self.commandMode.config(
			fg="#FCFCFC",
			bg="#08F",
			indicatoron=0,
			width="15",
			height="1",
			activebackground="#2AF"
		)
		self.commandName.pack(pady=5)
		self.commandResponse=Entry(self.root)
		self.commandResponse.config(
			bg="#000000",
			fg="#FFFFFF",
			placeholder="Command Response"
		)
		self.commandResponse.pack(pady=9)
		self.commandMode.pack(pady=5)
		self.dropdownToIndex={"Reply":0,"Ban Command":1,"Kick Command":2}
		self.b=Button(
			self.root,
			text="Create Command",
			command=self.createCommand
		)
		self.b.config(
			bg="#0088FF",
			fg="#FFFFFF",								highlightbackground="#0011FF",
			activebackground="#0011DD"
		)
		self.b.pack(pady=10)
		with open('app.ini', 'r') as f:
			config=f.read()
		botHelper={"False":True, "True":False}
		hasHelpCommand=True
		for settings in config.split('\n'):
			setting = settings.split('=')
			if setting[0]=="NoDefaultHelpCommand":
				hasHelpCommand=botHelper[setting[1]]
		if hasHelpCommand:
			self.commandsCreated=['help']
		else:
			self.commandsCreated=[]
		with open("app_funcs.ini","r") as f:
				d=f.read()
				
		for thing in d.split("\n"):
			if thing=="":
				continue
			newLabel=Label(self.root, text="Command: "+thing.split(",")[0])
			newLabel.config(
				bg="#00A8FF",
				width=96
			)
			newLabel.pack()
			self.commandsCreated.append(thing.split(',')[0])
		self.debug.insert("1.0","\nDebug Console")
		self.debug.pack(side=BOTTOM)
		self.nb=Button(
			self.root,
			text="Compile",
			command=self.compile
		)
		self.nb.config(
			fg="#EEEEEE",
			bg="#0066FF",
			activebackground="#0022AA"
		)
		self.cb=Button(
			self.root,
			text="Remove All Commands",
			command=self.clear
		)
		self.cb.config(
			fg="#FFFF00",
			bg="#FF0000",
			activebackground="#AF0000",
			highlightbackground="#AA0000"
		)
		self.cb.pack(side=BOTTOM,pady=5)
		self.nb.pack(side=BOTTOM,pady=5)
		self.root.attributes("-fullscreen", True)
		self.root.configure(background="#2A2A2A")
		self.root.mainloop()
	def createCodeCommand(self):
		if self.commandName.get() in self.commandsCreated:
			self.debug.insert("0.0","\nCommand Already Exists, Please restart if you recently cleared!")
			return
		with open("app_funcs.ini","r") as f:
			d=f.read()
		starter=d+"\n"
		if d=="":
			starter=""
		with open("app_funcs.ini","w") as f:
			a=str(self.commandName.get())
			self.debug.insert("0.0",chars=f"\nCommand Created: {a}")
			self.commandsCreated.append(a)
			b=self.dropdownToIndex[str(self.dropdown.get())]
			c=str(self.commandResponse.get())
			f.write(f"{starter}{a},{b},{c}")
	def clear(self):
		open("app_funcs.ini","w").close()
		self.debug.insert("0.0",chars="\nCLEARED ALL commands, Restart To See Changes")
	def compile(self):
		self.root.destroy()
		os.system("build.bat")
	def createCommand(self):
		if len(self.commandName.get().split(' '))!=1:
			self.debug.insert("0.0", "\nCommand Name cannot have spaces.")
			return
		if self.commandResponse.get()=="":
			self.debug.insert("0.0", "\nCommand Response cannot be Empty.")
			return
		if self.commandName.get() in self.commandsCreated:
			self.debug.insert("0.0","\nCommand Already Exists, Please restart if you recently cleared!")
			return
		if self.commandName.get()=="":
			self.debug.insert("0.0",chars="\nNo Command Name Chosen!")
			return
		newLabel=Label(self.root,
			text=f"Command: {self.commandName.get()}"
		)
		newLabel.config(
			bg="#00A8FF",
			width=96
		)
		newLabel.pack()
		self.createCodeCommand()

FunctionEditor()