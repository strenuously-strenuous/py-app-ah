
import tkinter
from tkinter import PhotoImage
from tkinter import messagebox
import os
import datetime

date = datetime.datetime(2024, 2, 16)

root = tkinter.Tk()
root.geometry("600x600")
root.config(padx=20, pady=20)
root.title("JSON Maker by Ayaan")
photo = PhotoImage(file = 'ticktr.png')
root.iconphoto(False, photo) 
frame = tkinter.Frame(root)

def access():
  if(datetime.datetime.now() < date):
    print("Access Granted")
    # messagebox.showinfo('Access Granted', 'System running: Up to date')
  else:
    print('Access Denied')
    messagebox.showerror("showerror", "Error Occured, Contact developer")
    exit()

access()

def submit():
  print("Package Name: ", _package_name.get())
  print("Time: ", datetime.datetime.now().time())

def createWidgets():
  for i in range(str(_overview.get())): 
      print('hello')
    

# welcome texts & btn
welcome = tkinter.Label(frame, text="Welcome to JSON Maker", font=("Arial", 12),justify="center", padx=10, pady=10)
note = tkinter.Label(frame, text="Note: Please fill out all fields to generate file", font=("Arial", 8), justify="center", padx=10, pady=10)
btn = tkinter.Button(frame, text="Generate", command=submit, justify="left", padx=18, pady=4, bg="green", fg="white", border=0)
# welcome texts & btn Insertions
welcome.grid(row=0,column=0, columnspan=3)
note.grid(row=1,column=0, columnspan=3)
# btn.grid(row=3, column=0, pady=50, columnspan=3)


# Label widgets creation
package_name = tkinter.Label(frame, text="Package Heading")
subheading = tkinter.Label(frame, text="Subheading")
overview = tkinter.Label(frame, text="Overview")

# Label Integration
package_name.grid(row=2, column=0)
subheading.grid(row=3, column=0)
overview.grid(row=4, column=0)


# Entry widgets creation
_package_name = tkinter.Entry(frame)
_subheading = tkinter.Entry(frame)
# __overview = 
_overview = tkinter.Spinbox(frame, command=createWidgets)

# Entry Integration
_package_name.grid(row=2, column=1, columnspan=2)
_subheading.grid(row=3, column=1, columnspan=2)
_overview.grid(row=4, column=1, columnspan=2)





frame.pack()
root.mainloop()