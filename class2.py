from tkinter import *
from tkinter import messagebox as msg

bill=Tk()
bill.geometry("500x500")


def home():
    Current=int(enter.get())
    Previous=int(enter1.get())
    Total=Current-Previous
    if(Total<0):
        ans.config(text="Error:Current<Previous",fg="red")
        return
    elif(Total<=100):
        ans.config(text="Free",font=("Times New Roman",20),fg="green")
    else:
        Bill_amount=(Total-100)*2
        ans.config(text=f"Total Units: {Total}\nBill Amount: \u20B9{Bill_amount}", fg="blue")

def commercial():
    Current=int(enter.get())
    Previous=int(enter1.get())
    Total=Current-Previous
    if(Total<0):
        ans.config(text="Error:Current<Previous",fg="red")
        return
    Bill_amount=2*Total
    ans.config(text=f"Total Units:{Total} \n Bill Amount: \u20B9{Bill_amount}" , fg="Green")
    

def industrial():
    Current=int(enter.get())
    Previous=int(enter1.get())
    Total=Current-Previous
    if(Total<0):
        ans.config(text="Error:Current<Previous",fg="red")
        return
    Bill_amount=5*Total
    ans.config(text=f"Total Units:{Total}\n Bill_amount:\u20B9{Bill_amount}",fg="Black")
    


head=Label(bill,text="Electricity Bill",bg="blue",fg="white",font=("Times New Roman",30))
head.pack()

current=Label(bill,text="Current Unit",bg="Yellow",fg="black",font=("Times new Roman",20))
current.place(x=50,y=100)

enter=Entry(bill,font=("Times new Roman",20),bg="white",fg="purple")
enter.place(x=250,y=100)

previous=Label(bill,text="Previous Unit",bg="Yellow",fg="Black",font=("Times New Roman",20))
previous.place(x=50,y=200)

enter1=Entry(bill,font=("TImes New Roman",20),bg="white",fg="purple")
enter1.place(x=250,y=200)


btn=Button(bill,text="Home",bg="Maroon",fg="white",font=("Times New Roman",15),command=home)
btn.place(x=100,y=250)


btn1=Button(bill,text="Commercial",bg="Maroon",fg="white",font=("Times New Roman",15),command=commercial)
btn1.place(x=200,y=250)


btn2=Button(bill,text="Industrial",bg="Maroon",fg="White",font=("Times new roman",15),command=industrial)
btn2.place(x=350,y=250)


ans=Label(bill,font=("Times new Roman",20),fg="green")
ans.place(x=200,y=300)


bill.mainloop()