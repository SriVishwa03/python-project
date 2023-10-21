from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mc
root=Tk()
root.title('employee management system')
root.state('zoomed')
root.resizable(0,0)
root.configure(bg='#D2E0FB')
root.iconbitmap('icon1.ico')
#=========================================FUNCTIONS===================================================================================

def add():
    if nameentry.get() == '' or ageentry.get() == '' or dojentry.get() == '' or mailentry.get() == '' or gender.get() == '' or contactentry.get() == '' or addressentry.get() == '':
        messagebox.showerror('Message','Please Fill All Fields')
    else:
        e_name=i_name.get()
        e_age=i_age.get()
        e_doj=i_doj.get()
        e_mail=i_mail.get()
        e_gender=i_gender.get()
        e_contact=i_contact.get()
        e_address=i_address.get()
        
        con=mc.connect(host='localhost',user='root',passwd='',database='management')
        cur=con.cursor()
        cur.execute("insert into e1 (name,age,doj,mail,gender,contact,address) values ('"+e_name+"','"+e_age+"','"+e_doj+"','"+e_mail+"','"+e_gender+"','"+e_contact+"','"+e_address+"')")
        print('Inserted Sucessfully :)')
        con.close()
        messagebox.showinfo('Sucessfull','Insert Sucessfully :)')
        '''
        f=open('project.txt','w')
        f.readilines()
        f.close()
        clear()'''
        fetch()
def update():
    pass
def delete():
    pass
def clear():
    i_name.set('')
    i_name.set('')
    i_age.set('')
    i_doj.set('')
    i_mail.set('')
    i_gender.set('')
    i_contact.set('')
    i_address.set('')
def fetch():
     tv.delete(*tv.get_children())
     con=mc.connect(host='localhost',user='root',passwd='',database='management')
     cur=con.cursor()
     cur.execute('select * from e1')
     output=cur.fetchall()
     for row in output:
        tv.insert('',END,values=row)
     con.close()
'''     
def select(point):
    selected=tv.focus()
    data=tv.item(selected)
    global row
    row=data["values"]
    i_name.set(row[1])
    i_age.set([2])
    i_doj.set([3])
    i_mail.set([4])
    i_gender.set([5])
    i_contact.set(row[6])
    #i_address.set(row[7])
'''    
#=====================================================================================================================================
firstframe=Frame(root,bg='#A7D397',bd=10,width=20,height=3)
firstframe.pack(fill=X)
#=====================================================================================================================================
hlbl=Label(firstframe,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
hlbl.pack()
#=====================================================================================================================================
secframe=Frame(root,bg='#A7D397',bd=10,width=20,height=12)
secframe.pack(fill=X)
#=====================================================================================================================================

i_name=StringVar()
i_age=StringVar()
i_doj=StringVar()
i_mail=StringVar()
i_gender=StringVar()
i_contact=StringVar()
i_address=StringVar()


namelbl=Label(secframe,text='NAME',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
namelbl.grid(row=0,column=0,padx=20,pady=20,sticky="w")
nameentry=Entry(secframe,width=25,font=('ariel',10),textvariable=i_name)
nameentry.grid(row=0,column=1,padx=20,pady=20,sticky="w")

agelbl=Label(secframe,text='AGE',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
agelbl.grid(row=0,column=2,padx=20,pady=20,sticky="w")
ageentry=Entry(secframe,width=25,font=('ariel',10),textvariable=i_age)
ageentry.grid(row=0,column=3,padx=20,pady=20,sticky="w")

dojlbl=Label(secframe,text='D.O.J',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
dojlbl.grid(row=0,column=4,padx=20,pady=20,sticky="w")
dojentry=Entry(secframe,width=25,font=('ariel',10),textvariable=i_doj)
dojentry.grid(row=0,column=5,padx=20,pady=20,sticky="w")

maillbl=Label(secframe,text='EMAIL',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
maillbl.grid(row=1,column=0,padx=20,pady=20,sticky="w")
mailentry=Entry(secframe,width=25,font=('ariel',10),textvariable=i_mail)
mailentry.grid(row=1,column=1,padx=20,pady=20,sticky="w")

genderlbl=Label(secframe,text='GENDER',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
genderlbl.grid(row=1,column=2,padx=20,pady=20,sticky="w")
gender=ttk.Combobox(secframe,font=('times new roman',15),width=28,state='readonly',textvariable=i_gender)
gender['values']=('Male','Female','Others')
gender.grid(row=1,column=3,padx=20,pady=20,sticky="w")


contactlbl=Label(secframe,text='CONTACT',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
contactlbl.grid(row=1,column=4,padx=20,pady=20,sticky="w")
contactentry=Entry(secframe,width=25,font=('ariel',10),textvariable=i_contact)
contactentry.grid(row=1,column=5,padx=20,pady=20,sticky="w")

addresslbl=Label(secframe,text='ADDRESS',font=('times new roman',20,'bold'),bg='#A7D397',fg='#001524')
addresslbl.grid(row=2,column=0,padx=2,pady=10,sticky="w")
addressentry=Entry(secframe,width=65,font=('times new roman',16),textvariable=i_address)
addressentry.grid(row=3,column=0,columnspan=5,sticky="w")

#=============================================BUTTONS=================================================================================

addbutton=Button(secframe,text='ADD DETAILS',width=15,height=2,bg='#35A29F',fg='white',command=add)
addbutton.grid(row=4,column=0,pady=10)

#updatebutton=Button(secframe,text='UPDATE DETAILS',width=15,height=2,bg='red',fg='white',command=update)
#updatebutton.grid(row=4,column=1,pady=10)

#delbutton=Button(secframe,text='DELETE DETAILS',width=15,height=2,bg='pink',fg='white',command=delete)
#delbutton.grid(row=4,column=2,pady=10)

clearbutton=Button(secframe,text='CLEAR DETAILS',width=15,height=2,bg='#35A29F',fg='white',command=clear)
clearbutton.grid(row=4,column=2,pady=10)

#============================================TREE VIEW================================================================================

thirdframe=Frame(root,bg='#A7D397',bd=3)
thirdframe.pack(fill=X)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(thirdframe, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")

tv.heading("1", text="Name")
tv.column("1",width=200)
tv.heading("2", text="Age")
tv.column("2", width=60)
tv.heading("3", text="D.O.B")
tv.column("3", width=130)
tv.heading("4", text="Email")
tv.column("4",width=310)
tv.heading("5", text="Gender")
tv.column("5", width=160)
tv.heading("6", text="Contact")
tv.column("6",width=210)
tv.heading("7", text="Address")
tv['show'] = 'headings'
#tv.bind("<ButtonRelease-1>",select)
tv.pack(fill=X)


fetch()
root.mainloop()
