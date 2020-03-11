from tkinter import *
from tkinter import ttk
import mysql.connector
import json
import pymongo
import threading
window = Tk()
window.title("SKS Data Converter")
window.wm_iconbitmap('favicon.ico')
window.iconbitmap(default='favicon.ico')
group = LabelFrame(window, text="From Database info", padx=5, pady=5, bg='#80ccff')
group.pack(padx=10, pady=10)
#label section
lbl = Label(group, text="From Database Type: ")
lbl.grid(column=0, row=0)
lbl1 = Label(group, text="Host Name: ")
lbl1.grid(column=0, row=3)
lbl2 = Label(group, text="User Name: ")
lbl2.grid(column=0, row=4)
lbl3 = Label(group, text="Password: ")
lbl3.grid(column=0, row=5)
lbl4 = Label(group, text="Database Name: ")
lbl4.grid(column=0, row=6)
lbl4 = Label(group, text="Port: ")
lbl4.grid(column=0, row=7)
status = Label(group)
status.grid(column=1, row=8)
#combobox section
combo = ttk.Combobox(group)
combo['values']= ("-Select Database Type-", "MySql","MsSql", "MongoDB")
combo.current(0) #set the selected item
combo.grid(column=1, row=0)
# text entry
hostName = Entry(group,width=30)
hostName.grid(column=1, row=3)
userName = Entry(group,width=30)
userName.grid(column=1, row=4)
passWord = Entry(group,show="*",width=30)
passWord.grid(column=1, row=5)
database_name = Entry(group,width=30)
database_name.grid(column=1, row=6)
port = Entry(group,width=30)
port.grid(column=1, row=7)
# functions
def read_database():
    combo_data = combo.get()
    if combo_data=="MySql":
        if hostName.get()=="":
            status.configure(text='Please Write Host Name')
        if userName.get()=="":
            status.configure(text='Please Write User Name')
        mydb = mysql.connector.connect(
        host=hostName.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=database_name.get(),
        port=port.get()
        )
        if(mydb!=""):
            status.configure(text="Connected to Database. Database Name: "+database_name.get())
    if combo_data == "-Select Database Type-":
       status.configure(text='Please Select A Database Type')
        
   
    
# functions
# button section
btn = Button(group, text="Connect Database", bg="#008ae6", fg="white", command=read_database)
btn.grid(column=0, row=8)
window['bg'] = '#80ccff'

window.mainloop()