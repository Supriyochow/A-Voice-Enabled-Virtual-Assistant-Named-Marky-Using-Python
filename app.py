import tkinter as tk
#tkinter has a root window

root=tk.Tk()

#button function
button=tk.Button(root,text="Test Button",fg='white',bg='blue',activebackground='yellow',height=1,font="Courier",activeforeground='red',bd=6,highlightcolor='red',pady=10)
button.pack()
button.flash()

root.mainloop()