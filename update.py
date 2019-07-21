from tkinter import *
import mysql.connector
import tkinter.messagebox
md=mysql.connector.connect(host='localhost',user='root',password='root',database='dbms')
mycursor=md.cursor()
class Application:
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=1200,height=720,bg="lightgreen")
        self.left.pack()
        self.heading=Label(self.left,text='UPDATE APPOITMENTS',fg='steelblue',font=('arial 40 bold'),bg='lightgreen')
        self.heading.place(x=80,y=20)
        self.name=Label(self.left,text='Enter patient name',font=('arial 18 bold'),bg='lightgreen')
        self.name.place(x=20,y=80)
        self.uname=Entry(self.left,width=40)
        self.uname.place(x=260,y=90)
        self.btn=Button(self.left,text='SEARCH',bg='steelblue',width=20,command=self.search)
        self.btn.place(x=260,y=120)
    def search(self):
        self.input=self.uname.get()
        sql="""select * from appoitment where Name=%s"""
        mycursor.execute(sql, (self.input, ))
        self.res=mycursor.fetchall()
        if self.res==[]:
            tkinter.messagebox.showinfo('Warning','no data is present')
        else:
            for self.res1 in self.res:
                self.name1=self.res1[1]
                self.age=self.res1[2]
                self.gender=self.res1[3]
                self.city=self.res1[4]
                self.phone=self.res1[5]
                self.time=self.res1[6]
            self.lname=Label(self.left,text='Name',font=('arial 14 bold'),bg='lightgreen')
            self.lname.place(x=20,y=180)
            self.lage=Label(self.left,text='Age',font=('arial 14 bold'),bg='lightgreen')
            self.lage.place(x=20,y=220)
            self.lgender=Label(self.left,text='Gender',font=('arial 14 bold'),bg='lightgreen')
            self.lgender.place(x=20,y=260)
            self.llocation=Label(self.left,text='Location',font=('arial 14 bold'),bg='lightgreen')
            self.llocation.place(x=20,y=300)
            self.lphone=Label(self.left,text='Phone',font=('arial 14 bold'),bg='lightgreen')
            self.lphone.place(x=20,y=340)
            self.ltime=Label(self.left,text='Time',font=('arial 14 bold'),bg='lightgreen')
            self.ltime.place(x=20,y=380)
            self.lname=Entry(self.left,width=40)
            self.lname.place(x=260,y=190)
            self.lname.insert(END,str(self.name1))
            self.lage=Entry(self.left,width=40)
            self.lage.place(x=260,y=230)
            self.lage.insert(END,str(self.age))
            self.lgender=Entry(self.left,width=40)
            self.lgender.place(x=260,y=270)
            self.lgender.insert(END,str(self.gender))
            self.llocation=Entry(self.left,width=40)
            self.llocation.place(x=260,y=310)
            self.llocation.insert(END,str(self.city))
            self.lphone=Entry(self.left,width=40)
            self.lphone.place(x=260,y=350)
            self.lphone.insert(END,str(self.phone))
            self.ltime=Entry(self.left,width=40)
            self.ltime.place(x=260,y=390)
            self.ltime.insert(END,str(self.time))
            self.btn1=Button(self.left,text='UPDATE',bg='steelblue',width=20,command=self.update)
            self.btn1.place(x=260,y=420)
            self.btn2=Button(self.left,text='DELETE',bg='red',width=20,command=self.delete)
            self.btn2.place(x=100,y=420)
    def update(self):
        self.ent1=self.lname.get()
        self.ent2=self.lage.get()
        self.ent3=self.lgender.get()
        self.ent4=self.llocation.get()
        self.ent5=self.lphone.get()
        self.ent6=self.ltime.get()
        querry='update appoitment set Name=%s,Age=%s,Gender=%s,Location=%s,Phone=%s,Schedule_time=%s where Name=%s'
        Name=self.ent1
        value=(self.ent1,self.ent2,self.ent3,self.ent4,self.ent5,self.ent6,Name)
        mycursor.execute(querry,value)
        md.commit()
        tkinter.messagebox.showinfo('successfully','Data is updated')
    def delete(self):
        self.ent1=self.lname.get()
        self.ent2=self.lage.get()
        self.ent3=self.lgender.get()
        self.ent4=self.llocation.get()
        self.ent5=self.lphone.get()
        self.ent6=self.ltime.get()
        query='delete from appoitment where Name=%s'
        Name=self.ent1
        mycursor.execute(query,(Name,))
        tkinter.messagebox.showinfo('successfully ','Data is deleted')
        md.commit()
        self.lname.destroy()
        self.lage.destroy()
        self.lgender.destroy()
        self.llocation.destroy()
        self.lphone.destroy()
        self.ltime.destroy()
            
root=Tk()
Application(root)
root.resizable(False,False)
root.mainloop()