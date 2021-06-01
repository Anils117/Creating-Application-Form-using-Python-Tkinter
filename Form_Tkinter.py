from tkinter import *
tk=Tk()
tk.title("Application Form")

mylabel=Label(tk,text="Application Form",pady=15)
mylabel.grid(row=1,column=1)

mylabel1=Label(tk,text="Enter  your  Name  :",pady=15)
mylabel1.grid(row=3,column=0)
input1=Entry(tk,width=20)
input1.grid(row=3,column=1)

mylabel2=Label(tk,text="Enter  Mother Name :",pady=15)
mylabel2.grid(row=4,column=0)
input2=Entry(tk,width=20)
input2.grid(row=4,column=1)

mylabel3=Label(tk,text="Enter  Father Name :",pady=15)
mylabel3.grid(row=5,column=0)
input3=Entry(tk,width=20)
input3.grid(row=5,column=1)

mylabel4=Label(tk,text="Your Aadhar Number :",pady=15)
mylabel4.grid(row=6,column=0)
input4=Entry(tk,width=20)
input4.grid(row=6,column=1)

mylabel5=Label(tk,text="Your Mobile Number :",pady=15)
mylabel5.grid(row=7,column=0)
input5=Entry(tk,width=20)
input5.grid(row=7,column=1)

mylabel6=Label(tk,text="Your   District    :",pady=15)
mylabel6.grid(row=8,column=0)
input6=Entry(tk,width=20)
input6.grid(row=8,column=1)

mylabel7=Label(tk,text="Your   LandMark    :",pady=15)
mylabel7.grid(row=9,column=0)
input7=Entry(tk,width=20)
input7.grid(row=9,column=1)


mybutton=Button(tk,text="Submit")
mybutton.grid(row=10,column=1)





tk.mainloop()
