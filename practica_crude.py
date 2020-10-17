
import sqlite3
from tkinter import*
from tkinter import messagebox




miConexion=sqlite3.connect("database practica")

miCursor=miConexion.cursor()
try:
	miCursor.execute('''CREATE TABLE ESSENTIAL_DATA (ID INTEGER PRIMARY KEY AUTOINCREMENT , NAME VARCHAR(20), PASSWORD VARCHAR(20), 
	MAIL VARCHAR(20), COMMENTS VARCHAR(100))''')
except:
	pass



####Insertar datos

def Submit ():


	
	info=(str(numName.get()),str(numPass.get()),str(numMail.get()),str(numComments.get()))

	miCursor.execute("INSERT INTO ESSENTIAL_DATA VALUES (NULL,?,?,?,?)", info)
	
	miConexion.commit()

	
	
	



###Leer datos-----

def ReadDB ():

	num=numID.get()

	stringRead=f"SELECT* FROM ESSENTIAL_DATA  WHERE ID='{num}'"
	
	miCursor.execute(stringRead)

	myresult = miCursor.fetchone()

	numName.set(myresult[1])
	numPass.set(myresult[2])
	numMail.set(myresult[3])
	numComments.set(myresult[4])


	miConexion.commit()

	
	

	

###Update------

def UpdateDB():

	if numName.get()!=" ":
		col="NAME"
		value=str(numName.get())
	elif numPass.get()!=" ":
		col="PASSWORD"
		value=str(numPass.get())
	elif numMail.get()!=" ":
		col="Mail"
		value=str(numMail.get())
	elif numComments.get()!=" ":
		col="Comments"
		value=str(numComments.get())
	else:
		pass

	id=numID.get()

	stringUpdate=f"UPDATE ESSENTIAL_DATA SET {col}='{value}' WHERE ID={id}"

	miCursor.execute(stringUpdate)

	miConexion.commit()

	

	

###Delete------

def DeleteDB():
	
	num=numID.get()

	stringDelete=(f"DELETE FROM ESSENTIAL_DATA WHERE ID= '{num}'")
	
	miCursor.execute(stringDelete)

	miConexion.commit()


	
def closeDb():

	miConexion.close()
	
	messagebox.showwarning("Warning","Now the database is closed")

	
def FunAbout():
	messagebox.showinfo("About","Created by Raúl Vicente Martín")
	

	

root=Tk()

menubar=Menu(root)
menufile=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=menufile)
menufile.add_command(label="New")
menufile.add_command(label="Save")
menufile.add_command(label="Save as")
menuTools=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Tools", menu=menuTools)
menuTools.add_command(label="Copy")
menuTools.add_command(label="Paste")
menuTools.add_command(label="Delete")
menuHelp=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=menuHelp)
menuHelp.add_command(label="About",command=lambda:FunAbout())
menuHelp.add_command(label="License")

menubar.add_command(label="Close", command=lambda:closeDb())

root.config(menu=menubar)



idlabel=Label(root, text="ID")
idlabel.config(bg="white", fg="black")
idlabel.grid(row=1, column=1,padx=10, pady=10)

NameLabel=Label(root,text="Name")
NameLabel.config(bg="white", fg="black")
NameLabel.grid(row=2, column=1,padx=10, pady=10)

PasswordLabel=Label(root, text="Password")
PasswordLabel.config(bg="white", fg="black")
PasswordLabel.grid(row=3, column=1,padx=10, pady=10)

MailLabel=Label(root, text="Email")
MailLabel.config(bg="white", fg="black")
MailLabel.grid(row=4, column=1,padx=10, pady=10)

CommentsLabel=Label(root, text="Comments")
CommentsLabel.config(bg="white", fg="black")
CommentsLabel.grid(row=5, column=1,padx=10, pady=10)


numID=StringVar()
entryID=Entry(root,textvariable=numID)
entryID.grid(row=1, column=2,padx=10, pady=10)

numName=StringVar()
entryName=Entry(root,textvariable=numName)
entryName.grid(row=2, column=2,padx=10, pady=10)

numPass=StringVar()
entryPass=Entry(root,textvariable=numPass)
entryPass.grid(row=3, column=2,padx=10, pady=10)

numMail=StringVar()
entryMail=Entry(root,textvariable=numMail)
entryMail.grid(row=4, column=2,padx=10, pady=10)

numComments=StringVar()
entryComments=Entry(root,textvariable=numComments)
entryComments.grid(row=5, column=2,padx=10, pady=10,sticky="nsew")

SubmitButt=Button(root, text="Create", command=lambda:Submit())

SubmitButt.grid(row=6, column=0, pady=10,padx=5,sticky="nsew")

DeleteButt=Button(root, text="Delete", command=lambda:DeleteDB())
DeleteButt.grid(row=6, column=1,pady=10,padx=5,sticky="nsew")

UpdateButt=Button(root, text="Update", command=lambda:UpdateDB())
UpdateButt.grid(row=6, column=2,pady=10,padx=5,sticky="nsew")

ReadButt=Button(root, text="Read", command=lambda:ReadDB())
ReadButt.grid(row=6, column=3,pady=10,padx=5,sticky="nsew")

CloseButt=Button(root, text="Close", command=lambda:closeDb())
CloseButt.grid(row=6, column=4,pady=10,padx=5, sticky="nsew")

root.mainloop()
