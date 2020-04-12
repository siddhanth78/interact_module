import os

def error(m="An error occured"):
    print(f"ERROR : {m}")

def warn(m="\n"):
    print(f"WARNING : {m}")

def info(m="\n"):
    print(f"INFO : {m}")

def tip(m="\n"):
    print(f"TIP : {m}")



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



def ques(m=" "):
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
    li = bst.split("\n")
    maximum = 0
    for l in li:
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-"+"-"*maximum+"-+")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("+-"+"-"*maximum+"-+")



def clr():
    os.system('cls')
    

    
def greet():
    print("\nYou are using Interact.\n")

greet()


    
