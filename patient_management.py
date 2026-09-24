import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
con=sqlite3.connect("hospital.db");cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,phone TEXT,doctor TEXT,diagnosis TEXT)")
con.commit()
def refresh():
    for i in tree.get_children():tree.delete(i)
    for r in cur.execute("SELECT name,age,phone,doctor,diagnosis FROM patients ORDER BY id DESC"):tree.insert("", "end", values=r)
def add():
    try:
        cur.execute("INSERT INTO patients(name,age,phone,doctor,diagnosis) VALUES(?,?,?,?,?)",(name.get(),int(age.get()),phone.get(),doctor.get(),diag.get()));con.commit();refresh()
    except ValueError:messagebox.showerror("Error","Age must be a number.")
def delete():
    s=tree.selection()
    if s:
        namev=tree.item(s[0])["values"][0];cur.execute("DELETE FROM patients WHERE name=?",(namev,));con.commit();refresh()
root=tk.Tk();root.title("Hospital Patient Management System");root.geometry("900x500")
name=tk.StringVar();age=tk.StringVar();phone=tk.StringVar();doctor=tk.StringVar();diag=tk.StringVar()
f=tk.Frame(root);f.pack(pady=10)
for lab,var in [("Name",name),("Age",age),("Phone",phone),("Doctor",doctor),("Diagnosis",diag)]:
    tk.Label(f,text=lab).pack(side="left");tk.Entry(f,textvariable=var,width=13).pack(side="left",padx=3)
tk.Button(f,text="Add Patient",command=add).pack(side="left");tk.Button(f,text="Delete",command=delete).pack(side="left")
tree=ttk.Treeview(root,columns=("Name","Age","Phone","Doctor","Diagnosis"),show="headings")
for c in ("Name","Age","Phone","Doctor","Diagnosis"):tree.heading(c,text=c)
tree.pack(fill="both",expand=True,padx=10,pady=10);refresh();root.mainloop()
