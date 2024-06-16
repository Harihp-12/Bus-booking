from tkinter import *
from tkinter.font import *
from tkinter import ttk
import tkinter.messagebox
class1=Tk()
cool_font=Font(family='Jokerman',size=30,weight='bold')
Label(class1,text='Sundhra Travels',font=cool_font,bg='#2187ab',fg='White',width=20).place(x=520,y=100)
class1.geometry('2000x1000')
class1.config(bg='#7cc0d8')
class1.title('Travels')
class1.resizable(height='true',width='true')
dm=()
dm1=()
Name=StringVar()
passw=StringVar()
cpassw=StringVar()
Pickup=StringVar()
Drop=StringVar()
Seat=StringVar()
dropvar1=StringVar()
dropvar2=StringVar()


Label(class1,text='Name',font='Ubuntu',bg='#3ba1c5',fg='white').place(x=460,y=250)
Label(class1,text='Password',font='Ubuntu ',bg='#3ba1c5',fg='white').place(x=460,y=300)
Label(class1,text="Confirm Password",font='Ubuntu ',bg='#3ba1c5',fg='white').place(x=460,y=350)
Entry(class1,textvariable=Name,width=30).place(x=650,y=250)
Entry(class1,textvariable=passw,width=30).place(x=650,y=300)
Entry(class1,textvariable=cpassw,width=30).place(x=650,y=350)
 


def login():
                  
    if passw.get() == cpassw.get():
      tkinter.messagebox.showinfo('register',"succesfully Registered") 

      class2=Toplevel()
      class2.geometry('2000x1000')
      class2.config(bg='#66b6d2')
      class2.title('TICKETS BOOKING')
 

      Label(class2,text='Sundhara Travels',font=cool_font,bg="#2596be",fg='white').place(x=550,y=100)
      Label(class2,text='Pickup Point',font='arial 10',bg='#2596be',fg='white').place(x=530,y=250)
      dm=ttk.OptionMenu(class2,dropvar1,'---Select---',optionA,option_a,option_b,option_c,option_d,option_e,option_f,option_g,option_h,command = getvalues1)
      dm.place(x=640,y=250)
      Label(class2,text='Drop point',font='arial 10',bg='#2596be',fg='white').place(x=530,y=300)
      dm1=ttk.OptionMenu(class2,dropvar2,'--Select--',optionB,option_i,option_j,option_k,option_l,option_m,option_n,option_o,option_p,command=getvalues2)
      dm1.place(x=640,y=300)
       
      Button(class2,text='SUBMIT',font='bold 10',bg='#2596be',fg='white',command=selection).place(x=630,y=380)
    elif Name.get() == "" or passw.get() == "" or cpassw.get() == "":
        tkinter.messagebox.showinfo('register',"KINDLY FILL ALL THE DETAILS...")

      
    else:
        tkinter.messagebox.showinfo('register',"Password not matching") 
 
    class2.mainloop()

   
     
def selection():
     class3=Toplevel()
     class3.geometry('2000x1000')
     class3.title('SELECTION')
     class3.config(bg='#a8d5e5')
     def seat1():
        Button(class3,text='SEAT 1',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat1).place(x=420,y=150)
     def seat2():
        Button(class3,text='SEAT 2',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat2).place(x=830,y=150)
     def seat3():
        Button(class3,text='SEAT 3',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat3).place(x=420,y=200)         
     def seat4():
        Button(class3,text='SEAT 4',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat4).place(x=830,y=200)        
     def seat5():
        Button(class3,text='SEAT 5',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat5).place(x=420,y=250)         
     def seat6():
        Button(class3,text='SEAT 6',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat6).place(x=830,y=250)         
     def seat7():
        Button(class3,text='SEAT 7',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat7).place(x=420,y=300)         
     def seat8():
        Button(class3,text='SEAT 8',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat8).place(x=830,y=300)         
     def seat9():
        Button(class3,text='SEAT 9',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat9).place(x=420,y=350)         
     def seat10():     
        Button(class3,text='SEAT10',font='arial 10',bg='#2596be',activebackground='#bee0ec',command=seat10).place(x=830,y=350)                
     Label(class3,text='Sundhara Travels ',font=cool_font,bg='#3ba1c5',fg='white').place(x=470,y=50)
     Label(class3,text='Seats',font='bold 20',bg='#3ba1c5',fg='white').place(x=10,y=10)
     Button(class3,text='SEAT A',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat1).place(x=500,y=120)
     Button(class3,text='SEAT B',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat2).place(x=740,y=120)
     Button(class3,text='SEAT C',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat3).place(x=500,y=200)
     Button(class3,text='SEAT D',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat4).place(x=740,y=200)
     Button(class3,text='SEAT E',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat5).place(x=500,y=280)
     Button(class3,text='SEAT F',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat6).place(x=740,y=280)
     Button(class3,text='SEAT G',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat7).place(x=500,y=360)
     Button(class3,text='SEAT H',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat8).place(x=740,y=360)
     Button(class3,text='SEAT I',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat9).place(x=500,y=440)
     Button(class3,text='SEAT J',font='arial 10',bg='#3ba1c5',fg='white',activebackground='Black',command=seat10).place(x=740,y=440)
     Button(class3,text='Confirmation',font='arial 10',bg='#3ba1c5',fg='white',width=15,activebackground='black',command=Reciept).place(x=575,y=550)
     Button(class3,text='Quit',font='arial 10',bg='#3ba1c5',fg='white',width=15,activebackground='black',command=quit).place(x=575,y=630)
   
     class3.mainloop()

def Reciept():
    class4 = Toplevel()
    class4.geometry('2000x1000')
    class4.title('BOOKING RECIEPT')
    class4.config(bg='#d3eaf2')

    username = Name.get()
    pickpoint = dropvar1.get()
    Droppoint = dropvar2.get()

   
    seat_selected = "Seat 1"  

    Label(class4, text='Name-- ' + username, font='arial 10', bg='#51abcb', fg='white').place(x=540, y=150)
    Label(class4, text='Pick up-- ' + pickpoint, font='arial 10', bg='#51abcb', fg='white').place(x=540, y=180)
    Label(class4, text='Drop up-- ' + Droppoint, font='arial 10', bg='#51abcb', fg='white').place(x=540, y=210)
    Label(class4, text='Selected Seat-- ' + seat_selected, font='arial 10', bg='#51abcb', fg='white').place(x=540, y=240)
    Label(class4, text='Amount-- Error', font='arial 10', bg='#51abcb', fg='white').place(x=540, y=270)
    Label(class4, text="Amount-- $700", font=("arial ", 10)).place(x=540, y=300)
    Label(class4, text="Thank you for booking tickets", font=("Great Vibes", 10)).place(x=540, y=330)

    class4.mainloop()

#pickup
optionA=['Chennai']
option_a=['Pondicherry']
option_b=['vellore']
option_c=['Atthipatti']
option_d=['Thanjavur']
option_e=['Salem']
option_f=['Nagarkovil']
option_g=['Coimbarore']
option_h=['Madurai']
#Drop
optionB=['Chennai']
option_i=['Pondicherry']
option_j=['vellore']
option_k=['Atthipatti']
option_l=['Thanjavur']
option_m=['Salem']
option_n=['Nagarkovil']
option_o=['Coimbarore']
option_p=['Madurai']
     
def getvalues1(selected):
    dm.set_menu(*optionA,option_a,option_b,option_c,option_d,option_e,option_f,option_g,option_h.get(selected))
    print(dropvar1.get()) 
def getvalues2(selected):
    dm1.set_menu(*optionB,option_i,option_j,option_k,option_l,option_m,option_n,option_o,option_p.get(selected))
    print(dropvar2.get())


Button(class1,text='login',font='bold 15',bg='#51abcb',fg='white',padx=15,pady=5,command=login).place(x=650,y=400)
Button(class1,text='close',font='bold 15',bg='#51abcb',fg='white',padx=15,pady=5,command=quit).place(x=725,y=400)

class1.mainloop()