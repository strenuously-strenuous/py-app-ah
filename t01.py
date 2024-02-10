
import tkinter
from tkinter import PhotoImage
import os
import datetime

root = tkinter.Tk()
root.geometry("600x600")
root.config(padx=20, pady=20)
root.title("JSON Maker by Ayaan")
photo = PhotoImage(file = 'ticktr.png')
root.iconphoto(False, photo) 
frame = tkinter.Frame(root)

def submit():
  print("Package Name: ", _package_name.get())
  print("Time: ", datetime.datetime.now().time())


# welcome texts & btn
welcome = tkinter.Label(frame, text="Welcome to JSON Maker", font=("Arial", 12),justify="center", padx=10, pady=10)
note = tkinter.Label(frame, text="Note: Please fill out all fields to generate file", font=("Arial", 8), justify="center", padx=10, pady=10)
btn = tkinter.Button(frame, text="Generate", command=submit, justify="left", padx=18, pady=4, bg="green", fg="white", border=0)
# welcome texts & btn Insertions
welcome.pack()
note.pack()
# btn.pack(row=3, column=0, pady=50, columnspan=3)


# Label widgets creation
package_name = tkinter.Label(frame, text="Package Heading")
package_name.pack(side='left')
_package_name = tkinter.Entry(frame)
_package_name.pack(side='right', fill='both', expand="true")
subheading = tkinter.Label(frame, text="Subheading")
_subheading = tkinter.Entry(frame)
overview = tkinter.Label(frame, text="Overview")
_overview = tkinter.Entry(frame)


# Entry widgets creation




# Entry Integration
# Label Integration

subheading.pack(side='left')
_subheading.pack(side='right')
overview.pack(side='left')
_overview.pack(side='right')





frame.pack()
root.mainloop()