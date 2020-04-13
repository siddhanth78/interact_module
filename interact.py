import os
import os.path
import time
import getpass
import mysql.connector
import random


def error(m='An error occured.',f=0,e=0):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"ERROR : {m}" , flush = mode , end=e)

        

def warn(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"WARNING : {m}" , flush = mode , end=e)

        

def info(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"INFO : {m}" , flush = mode , end=e)

        

def tip(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"TIP : {m}" , flush = mode , end=e)



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



def msg(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"{m}" , flush = mode , end=e)



def star(m='\n',f=0,e='\n'):
    if f == 0:
        mode = False
    elif f == 1:
        mode = True
    else:
        mode = False
        
    print(f"*{m}" , flush = mode , end=e)



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



def login(sqluser="",sqlpass="",checkdb="",dbtable="credentials"):
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
            cursor.execute(f"create table if not exists {dbtable.strip()} (m_id varchar(5) not null unique,Username varchar(20) not null unique , Password varchar(20) not null unique)")
            cursor.execute(f"select * from {dbtable.strip()}")
            for i in cursor:
                mid,us,pa = i
                if usern == us and passw == pa:
                    print("\nCredentials valid.\n")
                    valid = 1
                    break
            else:
                print("\nInvalid credentials.\n")
                valid = 0
                
    return(mid , usern , passw ,valid)



def sign_up(sqluser="",sqlpass="",outdb="",dbtable="credentials"):
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
                mid=""
                no1=random.randint(0,9)
                no2=random.randint(10,99)
                ch1=random.randint(65,90)
                ch2=random.randint(65,90)
                mid=str(chr(ch1))+str(no1)+str(chr(ch2))+str(no2)
                print(f"\nYour m_id : {mid}\n")
                cursor.execute(f"create table if not exists {dbtable.strip()} (m_id varchar(5) not null unique,Username varchar(20) not null unique , Password varchar(20) not null unique)")
                cursor.execute(f"insert into {dbtable.strip()} values('{mid}','{usern}','{passw}')")
                mydb.commit()
            except:
                print("\nError. Couldn't register. Possibly because username/password/m_id already exists or invalid username/password (No special characters other than '_' allowed).\n")
                valid = 0
            else:
                print("\nYou have been registered. Welcome.\n")
                valid = 1
                
    return(mid , usern , passw ,valid)
    


def clr():
    os.system('cls')
    

    
def greet():
    time.sleep(1)
    print("\nINTERACT 1.1.4\n",flush=True)
    time.sleep(3)
    os.system('cls')
    time.sleep(2)

greet()


    
