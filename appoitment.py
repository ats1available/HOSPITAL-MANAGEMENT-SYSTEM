from tkinter import *
import mysql.connector
import tkinter.messagebox
import os
md=mysql.connector.connect(host='localhost',user='root',password='root',database='dbms')
mycursor=md.cursor()
class Appoitment:
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=800,height=720,bg="lightgreen")
        self.left.pack(side=LEFT)
        self.right=Frame(master,width=400,height=720,bg="steelblue")
        self.right.pack(side=RIGHT)
        self.head=Label(self.left,text="METRO HOSPITAL",font=("arial 40 bold"),fg="white",bg='lightgreen')
        self.head.place(x=130,y=0)
        self.name=Label(self.left,text="NAME",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.name.place(x=20,y=80)
        self.age=Label(self.left,text="AGE",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.age.place(x=20,y=120)
        self.gender=Label(self.left,text="GENDER",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.gender.place(x=20,y=160)
        self.location=Label(self.left,text="LOCATION",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.location.place(x=20,y=200)
        self.phone=Label(self.left,text="PHONE",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.phone.place(x=20,y=240)
        self.time=Label(self.left,text="TIME",font=("arial 18 bold"),fg="black",bg='lightgreen')
        self.time.place(x=20,y=280)
        self.name_ent=Entry(self.left,width=35)
        self.name_ent.place(x=180,y=85)
        self.age_ent=Entry(self.left,width=35)
        self.age_ent.place(x=180,y=125)
        self.gender_ent=Entry(self.left,width=35)
        self.gender_ent.place(x=180,y=165)
        self.location_ent=Entry(self.left,width=35)
        self.location_ent.place(x=180,y=205)
        self.phone_ent=Entry(self.left,width=35)
        self.phone_ent.place(x=180,y=245)
        self.time_ent=Entry(self.left,width=35)
        self.time_ent.place(x=180,y=285)
        self.btn=Button(self.left,text="Submit",font=("arial 14 bold"),bg='lightblue',width=25,fg='black',command=self.fixed)
        self.btn.place(x=180,y=340)
        self.box=Text(self.right,width=45,height=40)
        self.box.place(x=18,y=55)
        sql1="select ID from appoitment"
        mycursor.execute(sql1)
        self.val=mycursor.fetchall()
        self.k=0
        for self.fi in self.val:
            self.k=self.k+1
        self.box.insert(END,str(self.k)+" Appoitment has been created")
        self.log=Label(self.right,text="LOGS",font=('arial 30 bold'), fg='black',bg='steelblue')
        self.log.place(x=0,y=0)
        self.btn1=Button(self.left,text="Update",bg='lightblue',font=("arial 14 bold"),width=25,fg='black',command=self.update)
        self.btn1.place(x=180,y=390)
    def update(self):
        os.startfile('update.py')
    def fixed(self):
        self.val1=self.name_ent.get()
        self.val2=self.age_ent.get()
        self.val3=self.gender_ent.get()
        self.val4=self.location_ent.get()
        self.val5=self.phone_ent.get()
        self.val6=self.time_ent.get()
        print(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6)
        if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='':
            tkinter.messagebox.showinfo("WARNING","Please fill all box")
        else:
            sql="INSERT INTO appoitment(Name,Age,Gender,Location,Phone,Schedule_time)""VALUES(%s,%s,%s,%s,%s,%s)"
            val=(str(self.val1),int(self.val2),str(self.val3),str(self.val4),int(self.val5),int(self.val6))
            mycursor.execute(sql,val)
            md.commit()
            print("jdn")
            tkinter.messagebox.showinfo("successfully","Appoitment has been created for "+str(self.val1))
            
root=Tk()
Appoitment(root)
root.resizable(False,False)
root.mainloop()

888