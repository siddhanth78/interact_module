import os
import os.path
import time
import getpass
import mysql.connector

def error(m='An error occured',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"ERROR : {m}" , flush = mode)
    elif e == 1:
        print(f"ERROR : {m}" , flush = mode , end='')
    else:
        print(f"ERROR : {m}" , flush = mode)

        

def warn(m='\n',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"WARNING : {m}" , flush = mode)
    elif e == 1:
        print(f"WARNING : {m}" , flush = mode , end='')
    else:
        print(f"WARNING : {m}" , flush = mode)

        

def info(m='\n',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"INFO : {m}" , flush = mode)
    elif e == 1:
        print(f"INFO : {m}" , flush = mode , end='')
    else:
        print(f"INFO : {m}" , flush = mode)

        

def tip(m='\n',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"TIP : {m}" , flush = mode)
    elif e == 1:
        print(f"TIP : {m}" , flush = mode , end='')
    else:
        print(f"TIP : {m}" , flush = mode)



def custom_yesno(m=" "):
    conf = input(f"{m} (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def yesno():
    conf = input("Confirm? (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def exit_yesno():
    conf = input(f"Exit from application? (y/n) : ")
    if conf.lower().strip() in ['y' , 'yes']:
        con = 1
    elif conf.lower().strip() in ['n' , 'no']:
        con = 0
    else:
        con = 2
    print()
    return con



def prompt_(m=" "):
    ans = input(f"{m} : ")
    print()
    return ans



def msg(m='\n',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"{m}" , flush = mode)
    elif e == 1:
        print(f"{m}" , flush = mode , end='')
    else:
        print(f"{m}" , flush = mode)



def star(m='\n',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    if e == 0:
        print(f"*{m}" , flush = mode)
    elif e == 1:
        print(f"*{m}" , flush = mode , end='')
    else:
        print(f"*{m}" , flush = mode)



def menu(title=" ",items=[]):
    li = items
    if isinstance(li , list) == False:
        print("ArgTypeError : menu(<string> , <list>)")
        return
    n = 1
    li = list(li)
    print(f"\n------{title}------\n")
    for l in li:
        print(f"{n}. {l}")
        n+=1
    print("\n------"+"-"*len(title)+"------\n")



def box(m=" "):
    li = m.split("\n")
    maximum = 0
    for l in li:
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-"+"-"*maximum+"-+")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+")



def login(sqluser="",sqlpass="",checkdb="",dbtable=""):
    usern = ""
    passw = ""
    valid = 0
    
    while True:
        usern = input("Username : ")
        if usern.strip() == "":
            print("\nUsername must be filled.\n")
            continue
        break
    while True:
        passw = getpass.getpass(prompt="Password : ")
        if passw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        break

    if checkdb.strip()=="":
        pass
    else:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = sqluser.strip(),
                passwd = sqlpass,
                database = checkdb.strip()
                )

            cursor = mydb.cursor()
        except:
            print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
            valid = 0
        else:
            cursor.execute(f"create table if not exists {dbtable.strip()} (Username varchar(20) not null unique , Password varchar(20) not null unique)")
            cursor.execute(f"select * from {dbtable.strip()}")
            for i in cursor:
                us,pa = i
                if usern == us and passw == pa:
                    print("\nCredentials valid.\n")
                    valid = 1
                    break
            else:
                print("\nInvalid credentials.\n")
                valid = 0
                
    return(usern , passw ,valid)



def sign_up(sqluser="",sqlpass="",outdb="",dbtable=""):
    usern = ""
    passw = ""
    valid = 0

    while True:
        usern = input("Username : ")
        if usern.strip() == "":
            print("\nUsername must be filled.\n")
            continue
        break
    while True:
        passw = getpass.getpass(prompt="Password : ")
        if passw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        break

    if outdb.strip()=="":
        pass
    else:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = sqluser.strip(),
                passwd = sqlpass,
                database = outdb.strip()
                )

            cursor = mydb.cursor()
        except:
            print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
            valid = 0
        else:
            try:
                cursor.execute(f"create table if not exists {dbtable.strip()} (Username varchar(20) not null unique , Password varchar(20) not null unique)")
                cursor.execute(f"insert into {dbtable.strip()} values('{usern}','{passw}')")
                mydb.commit()
            except:
                print("\nError. Couldn't register. Possibly because username/password already exists or invalid username/password (No special characters other than '_' allowed).\n")
                valid = 0
            else:
                print("\nYou have been registered. Welcome.\n")
                valid = 1
                
    return(usern , passw ,valid)
    


def clr():
    os.system('cls')
    

    
def greet():
    time.sleep(1)
    print("\nINTERACT 1.1.4\n",flush=True)
    time.sleep(3)
    os.system('cls')
    time.sleep(2)

greet()


    
