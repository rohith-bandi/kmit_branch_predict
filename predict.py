import json
import re
import smtplib
import datetime

def validemail(email):
    if re.search(r"^[\w.-]+@[\w.-]+.\w+$",email):
        return True
    else:
        return False


def login():
    while 1:
        email=input("Enter your email address:")
        if validemail(email):
            prediction(email)
            return 0
        else:
            print("Invalid email address")
            
        
def prediction(email):
        while 1:
            rank=input("Enter your eamcet rank:")
            if re.search(r"^\d+$",rank):
                break
            else:
                print("Invalid eamcet rank")
        print()        
        print("1.Male\n2.Female")        
        while 1:
            gender=input("Enter your gender:")
            if gender=="1" or gender=="2":
                break
            else:
                print("Invalid option")
        print()
        print('1.OC\n2.BC_A\n3.BC_B\n4.BC_C\n5.BC_D\n6.BC_E\n7.SC\n8.ST\n9.EWS')
        while 1:
            category=input("Enter Your category:")
            if re.search(r"^\d+$",category):
                if int(category)>=1 and int(category)<=9:
                    break
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        with open("ranks.json","r") as f:
            jdic=json.load(f)
            x="KMIT BRANCH PREDICTION\n\n"
            for i in jdic:
                if int(jdic[i][gender][category])>=int(rank):
                    y="You may get seat in "+i+"\n"
                    print(y,end='')
                    x=x+y
                else:
                    y="You have may not get seat in "+i+"\n"
                    print(y,end='')
                    x=x+y        
       
        sendmail(email,x)    


        
def sendmail(email,message): 
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kmitbranchpredictor@gmail.com","ohmfokbortiqnoai")
    from_addr = "kmitbranchpredictor@gmail.com"
    to_addr = email
    subj = "kmitbranchpredictor"
    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message )
    s.sendmail("kmitbranchpredictor@gmail.com",email,msg)
    s.quit()
    print("Prediction is sent to your Email")               
        


def display():
    print("1.LOGIN\n2.EXIT")
    opt=input("Enter your option:")
    if opt=="1":
        login()
        print()
        display()
    elif opt=="2":
        return 0
    else:
        print("Invalid option")
        print()
        display()
        
print("***********************\nKMIT BRANCH PREDICTION\n***********************")
print()
display()
