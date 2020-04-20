import time
import random

try:
    import sys
except:
    print("os-sys (installation reqd. - yes")
    time.sleep(3)
    quit()
else:
    pass

aa=0
bb=0
cc=0
dd=0
cout=0

try:
    import os
except:
    aa=1
else:
    time.sleep(0.5)
    sys.stdout.write("\rChecking...|")
    import os.path

try:
    import getpass
except:
    bb=1
else:
    time.sleep(0.5)
    sys.stdout.write("\rChecking.../")

try:
    import mysql.connector
except:
    cc=1
else:
    time.sleep(0.5)
    sys.stdout.write("\rChecking...-")

try:
    import shutil
except:
    dd=1
else:
    time.sleep(0.5)
    sys.stdout.write("\rChecking...\\")

sys.stdout.write("\n")

if aa==1:
    sys.stdout.write("os (installation reqd. - yes)")
    cout+=1
if bb==1:
    sys.stdout.write("getpass (installation reqd. - yes)")
    cout+=1
if cc==1:
    sys.stdout.write("mysql-connector-python (installation reqd. - yes)")
    cout+=1
if dd==1:
    sys.stdout.write("shutil (installation reqd. - yes)")
    cout+=1

if cout>0:
    time.sleep(3)
    quit()
else:
    time.sleep(0.5)
    
syner = ("Syntax for updates : updates=[(<table1>,<targetcolumn1>,<newdata1 (int or string)>,"
         "<conditioncolumn1 (can be blank by entering '')>,<pattern1> (can be blank by entering '')),\n"
         "                             (<table2>,<targetcolumn2>,<newdata2 (int or string)>,"
         "<conditioncolumn2 (can be blank by entering '')>,<pattern2> (can be blank by entering '')),\n"
         "                          ...(<table'n'>,<targetcolumn'n'>,<newdata'n' (int or string)>,"
         "<conditioncolumn'n' (can be blank by entering '')>,<pattern'n'> (can be blank by entering ''))]")

def error(m='An error occured.'):
    if m.strip() == "":
        m=' '*7
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 9:
            l = l+" "*(9-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-ERROR"+"-"*(maximum-5)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def warn(m=' '*9):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 11:
            l = l+" "*(11-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-WARNING"+"-"*(maximum-7)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def info(m=' '*6):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 8:
            l = l+" "*(8-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-INFO"+"-"*(maximum-4)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")

        

def tip(m=' '*5):
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < 7:
            l = l+" "*(7-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-TIP"+"-"*(maximum-3)+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")



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



def menu(title=" ",items=[],reuse=0):
    li = items
    if isinstance(li , list) == False:
        print("ArgTypeError : menu(<string> , <list> , reuse)")
        return
    n = 1
    li = list(li)
    if reuse==0:
        print(f"\n------{title}------\n")
        for l in li:
            print(f"{n}. {l}")
            n+=1
        print("\n------"+"-"*len(title)+"------\n")
        return
    elif reuse==1:
        usermenu=f"\n------{title}------\n\n"
        for l in li:
            usermenu+=f"{n}. {l}\n"
            n+=1
        usermenu+="\n------"+"-"*len(title)+"------\n\n"
        return usermenu
    else:
        print(f"\n------{title}------\n")
        for l in li:
            print(f"{n}. {l}")
            n+=1
        print("\n------"+"-"*len(title)+"------\n")
        return



def box(title='-',m=' '):
    title=str(title)
    if isinstance(m,str):
        li = m.split("\n")
    elif isinstance(m,list):
        li=[]
        for it in m:
            li.append(it.strip("\n"))
    else:
        li = [str(m)]
    maximum = 0
    for l in li:
        if len(l) < len(title)+2:
            l = l+" "*((len(title)+2)-len(l))
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-"+title+"-"*(maximum-len(title))+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+\n")



def login(sqlhost="localhost",sqluser="",sqlpass="",checkdb="",dbtable="credentials"):
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
                host = sqlhost.strip(),
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



def get_items(sqlhost="localhost",sqluser="",sqlpass="",checkdb="",dbtable="",reqcol="*",wherecol="",pattern=""):
    itemlist = []
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = checkdb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        if wherecol.strip()=="":
            try:
                cursor.execute(f"select {reqcol.strip()} from {dbtable.strip()}")
            except:
                print("\nError. Check your arguments again.\n")
                return
            else:
                for item in cursor:
                    itemlist.append(item)
                return itemlist
        else:
            if pattern.strip()=="":
                print("\nPattern required.\n")
                return
            else:
                try:
                    cursor.execute(f"select {reqcol.strip()} from {dbtable.strip()} where {wherecol.strip()} like '{pattern}'")
                except:
                    print("\nError. Check your arguments again.\n")
                    return
                else:
                    for item in cursor:
                        itemlist.append(item)
                    return itemlist



def update(sqlhost="localhost",sqluser="",sqlpass="",checkdb="",dbtable="",reqcol="",newdata="",wherecol="",pattern=""):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = checkdb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        if str(newdata).strip() == "":
            print("\nError. New data can't be blank.\n")
            return
        
        if wherecol.strip()=="":
            try:
                cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = {newdata}")
                mydb.commit()
            except:
                print("\nError. Check your arguments again.\n")
                return
            else:
                return
        else:
            if pattern.strip()=="":
                print("\nPattern required.\n")
                return
            else:
                try:
                    cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = {newdata} where {wherecol.strip()} like '{pattern}'")
                    mydb.commit()
                except:
                    print("\nError. Check your arguments again.\n")
                    return
                else:
                    return


def multi_update(sqlhost="localhost",sqluser="",sqlpass="",checkdb="",updates=[]):
    global syner
    if isinstance(updates , list) == False:
        print("ArgTypeError : multi_update(<string> , <string> , <string> , <list>)")
        return
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = checkdb.strip()
            )

        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        number = 1
        for up in updates:
            try:
                if len(up)==3:
                    dbtable,reqcol,newdata = up
                elif len(up)==5:
                    dbtable,reqcol,newdata,wherecol,pattern = up
            except:
                print(f"\nError in query {number}. Probably missing arguments or invalid data.\n")
                print(syner)
                number+=1
                continue
            else:
                pass
            if str(newdata).strip() == "":
                print(f"\nError in query {number}. New data can't be blank.\n")
                print(syner)
                number+=1
                continue
        
            if len(up)==3:
                try:
                    cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = {newdata}")
                    mydb.commit()
                except:
                    print(f"\nError in query {number}. Check your arguments again.\n")
                    print(syner)
                    number+=1
                    continue
                else:
                    number+=1
                    continue
            else:
                if pattern.strip()=="":
                    print(f"\nError in query {number}. Pattern required.\n")
                    print(syner)
                    number+=1
                    continue
                else:
                    try:
                        cursor.execute(f"update {dbtable.strip()} set {reqcol.strip()} = {newdata} where {wherecol.strip()} like '{pattern}'")
                        mydb.commit()
                    except:
                        print(f"\nError in query {number}. Check your arguments again.\n")
                        print(syner)
                        number+=1
                        continue
                    else:
                        number+=1
                        continue
                


def sign_up(sqlhost="localhost",sqluser="",sqlpass="",outdb="",dbtable="credentials"):
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
    while True:
        repassw = getpass.getpass(prompt="Confirm password : ")
        if repassw.strip() == "":
            print("\nPassword must be filled.\n")
            continue
        
        if repassw != passw:
            print("\nPasswords do not match.\n")
            continue
        elif repassw == passw:
            break

    if outdb.strip()=="":
        pass
    else:
        try:
            mydb = mysql.connector.connect(
                host = sqlhost.strip(),
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



def readfile(filepath="",return_="whole",amt=0):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        file = open(filepath,'r')
        if return_ == "whole":
            if amt==0:
                data=file.read()
                file.close()
                return data
            else:
                data=file.read(amt)
                file.close()
                return data
        elif return_ == "lines":
            if amt==0:
                data=file.readlines()
                file.close()
                return data
            else:
                data=[]
                for x in range(amt):
                    data.append(file.readline())
                file.close()
                return data
        else:
            data=file.read()
            file.close()
            return data


def writefile(filepath="",newdata="",mode="append"):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        if mode == "append":
            file = open(filepath,'a')
            file.write(newdata)
            file.close()
        elif mode == "overwrite":
            file = open(filepath,'w')
            file.write(newdata)
            file.close()
        else:
            file = open(filepath,'a')
            file.write(newdata)
            file.close()


def createfile(filepath=""):
    if os.path.exists(filepath)==True:
        print("\nFile already exists.\n")
    elif os.path.exists(filepath)==False:
        file = open(filepath,'x')
        file.close()



def deletefile(filepath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.remove(filepath)



def runfile(filepath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.system(filepath)



def rename(filepath="",newpath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.rename(filepath,newpath)



def movefile(filepath="",newpath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        os.replace(filepath,newpath)



def copyfile(filepath="",copypath=""):
    try:
        file = open(filepath,'r')
        file.close()
    except:
        print("\nError. Either file doesn't exist or an error occured.\n")
        return
    else:
        shutil.copyfile(filepath,copypath)



def pause(min_=0,sec=0,msec=0):
    time.sleep((min_*60)+(sec*1)+(msec*0.001))


        
def greet():
    os.system('cls')
    print("INTERACT 1.3.5. Visit https://github.com/siddhanth78/interact_module/blob/master/interact_description.txt for more info.\n\n",flush=True)

greet()   
