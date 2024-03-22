import tkinter as tk
import re
from tkinter import ttk
import json
import smtplib
import datetime

def prediction(email):
    
    def submit():
        flag=0
        r = rnke.get()
        x = gdrb.get()
        y = ctgyb.get()
        
        if re.search(r"^\d+$",r):
            rerror.config(text=" ")
            flag+=1
        else:
            rerror.config(text="invalid eamcet rank")
            

        if x=="1.Male" or x=="2.Female":
            gerror.config(text="")
            flag+=1
        else:
            gerror.config(text="Invalid option")
        
        
        if y=="1.OC" or y=="2.BC_A" or y=="3.BC_B" or y=="4.BC_C" or y=="5.BC_D" or y=="6.BC_E" or y=="7.SC" or y=="8.ST" or y=="9.EWS":
            cerror.config(text="")
            flag+=1
        else:
            cerror.config(text="Invalid option")

        if flag==3:
                window =tk.Tk()
                window.title("result")
                window.geometry(f"{1600}x{900}")
                window.config(bg="White")
                tps = tk.Label(window, height=5,bg="Purple",width=250)
                tps.pack()
                tps = tk.Label(window, height=7,bg="LightYellow",width=3)
                tps.pack()
                m,n,l="","",""
                with open("ranks.json","r") as f:
                    jdic=json.load(f)
                    m="Rank:"+r+"\nCategory:"+y.split('.')[1]+"\nGender:"+x.split('.')[1]+"\n\n"
                    for i in jdic:
                        if int(jdic[i][x.split('.')[0]][y.split('.')[0]])>=int(r):
                            n=n+i+"(closing rank is "+jdic[i][x.split('.')[0]][y.split('.')[0]]+")"+"\n"
                        
                        else:
                            l=l+i+"(closing rank is "+jdic[i][x.split('.')[0]][y.split('.')[0]]+")"+"\n"
                            
                    if n=="":      
                        m=m+"You may not get seat in the following branches\n"+l
                    elif l=="":
                        m=m+"You may get seat in the following branches\n"+n
                    else:
                        m=m+"You may get seat in the following branches\n"+n+"\n"+"You may not get seat in the following branches\n"+l
                    sendmail(email,m)
                result= tk.Label(window, text=m, font=("Helvetica", 20),bg="LIghtYellow")
                result.pack()
                t="NOTE : This prediction is made by using previous year closing ranks and it will be sent to your email"
                note = tk.Text(window, height=3, width=73,bg="LightGreen")
                note.insert(tk.END, t)
                note.pack()
                
                
            
    window = tk.Tk()
    window.title("details")
    window.geometry(f"{1600}x{900}")
    window.config(bg="White")
    tps = tk.Label(window, height=5,bg="Purple",width=250)
    tps.pack()
    det = tk.Label(window, text="Enter Your Details", font=("Helvetica", 25),bg="White")
    det.pack(pady=2)
    tp = tk.Label(window, height=4,bg="White")
    tp.pack()
    
    rnk = tk.Label(window, text="Eamcet Rank", font=("Helvetica", 20),bg="White")
    rnk.pack()
    rnke=tk.Entry(window,width=25,bg="LightGrey")
    rnke.pack()
    rerror = tk.Label(window,fg="red",font=("Helvetica", 10),bg="White")
    rerror.pack()
    
    tp1 = tk.Label(window, height=2,bg="White")
    tp1.pack()
    gdr = tk.Label(window, text="Gender", font=("Helvetica", 20),bg="White")
    gdr.pack()
    gdrv = tk.StringVar()
    gdrb = ttk.Combobox(window, textvariable=gdrv)
    gdrb['values'] = ("1.Male","2.Female")
    gdrb.pack()
    gerror = tk.Label(window,fg="red",font=("Helvetica", 10),bg="White")
    gerror.pack(pady=3)
    
    tp2 = tk.Label(window, height=4,bg="White")
    tp2.pack()
    ctgy = tk.Label(window, text="Category", font=("Helvetica", 20),bg="White")
    ctgy.pack()
    ctgyv = tk.StringVar()
    ctgyb = ttk.Combobox(window, textvariable=ctgyv)
    ctgyb['values'] = ("1.OC","2.BC_A","3.BC_B","4.BC_C","5.BC_D","6.BC_E","7.SC","8.ST","9.EWS")
    ctgyb.pack()
    cerror = tk.Label(window,fg="red",font=("Helvetica", 10),bg="White")
    cerror.pack(pady=3)
    tp3 = tk.Label(window, height=5,bg="White")
    tp3.pack()
    
    sub= tk.Button(window, text="submit", width=12, command=submit ,font=("Helvetica", 10),bg="green")
    sub.pack(pady=5)



def sendmail(email,message): 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kmitbranchpredictor@gmail.com","ohmfokbortiqnoai")
    fromadd= "kmitbranchpredictor@gmail.com"
    toadd = email
    subj = "kmitbranchpredictor"
    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromadd , toadd , subj, date, message )
    s.sendmail("kmitbranchpredictor@gmail.com",email,msg)
    s.quit()
    print("Sent Email")               
        


def login():
    email=lgne.get()
    if re.search(r"^[\w.-]+@[\w.-]+[.][\w]+$",email):
        error.config(text="")
        prediction(email)
        return 0
    else:
        error.config(text="Invalid Email address")

window = tk.Tk()
window.title("kmit")
window.geometry(f"{1600}x{900}")
window.config(bg="White")
top = tk.Label(window, height=5 , bg="Purple" , width = 250)
top.pack()
hdg = tk.Label(window, text="KMIT BRANCH PREDICTION", font=("Helvetica", 30), bg="Purple",width=250 , fg ="White")
hdg.pack()
top1 = tk.Label(window, height=12 ,bg="White" , width = 250)
top1.pack()
lgn = tk.Label(window, text="Enter Your E-mail Address", font=("Helvetica", 20),width=250,bg="White")
lgn.pack()
lgne=tk.Entry(window,width=35,bg="LightGrey")
lgne.pack()
lgnb= tk.Button(window, text="submit", width=12, command=login,font=("Helvetica", 10),bg="Green",fg="White")
lgnb.pack(pady=5)
error = tk.Label(window,fg="red",font=("Helvetica", 12),bg="White")
error.pack(pady=3)

window.mainloop()
