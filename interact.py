def error(e):
    print(f"\nERROR : {e}\n")

def warn(w):
    print(f"\nWARNING : {w}\n")

def info(i):
    print(f"\nINFO : {i}\n")

def tip(t):
    print(f"\nTIP : {t}\n")

def custom_yesno(yn):
    conf = input(f"\n{yn} (y/n) : ")
    if conf.lower() in ['y' , 'yes']:
        con = 1
    elif conf.lower() in ['n' , 'no']:
        con = 0
    print()
    return con
    
def yesno():
    conf = input("\nConfirm? (y/n) : ")
    if conf.lower() in ['y' , 'yes']:
        con = 1
    elif conf.lower() in ['n' , 'no']:
        con = 0
    print()
    return con

def exit_yesno():
    conf = input(f"\nExit from application? (y/n) : ")
    if conf.lower() in ['y' , 'yes']:
        con = 1
    elif conf.lower() in ['n' , 'no']:
        con = 0
    print()
    return con

def ask_ques(q):
    ans = input(f"{q} : ")
    print()
    return ans

def msg(m):
    print(f"\n{m}\n")

def star(st):
    print(f"\n*{st}\n")

def menu(title,li):
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

def box(bst):
    li = bst.split("\n")
    maximum = 0
    for l in li:
        part = len(l)
        if part > maximum:
            maximum = part
    print("+-"+"-"*maximum+"-+")
    print("| "+" "*maximum+" |")
    for p in li:
        print("| "+p+" "*(maximum-len(p))+" |")
    print("| "+" "*maximum+" |")
    print("+-"+"-"*maximum+"-+")


def interact():
    print("'interact' module")
    print("Used for system-user interaction.")
    print("Functions :\n")
    print("error(<string>) : Display custom error message")
    print("warn(<string>) : Display custom warning message")
    print("info(<string>) : Display custom information")
    print("msg(<string>) : Display custom message")
    print("tip(<string>) : Display custom tip")
    print("star(<string>) : Display custom starred message")
    print("box(<string>) : Display custom boxed information")
    print("yesno() : Ask a yes-no confirmation. Returns an integer (0 - 'no' , 1 - 'yes')")
    print("exit_yesno() : Ask a yes-no confirmation before exitting. Returns an integer (0 - 'no' , 1 - 'yes')")
    print("custom_yesno(<string>) : Ask a custom yes-no confirmation. Returns an integer (0 - 'no' , 1 - 'yes')")
    print("ask_q(<string>) : Ask a question. Returns a string")
    print("menu(<string> , <list>) : Display a menu for the user. Items are automatically numbered\n")
    
def greet():
    print("\nYou are using Interact. Run 'interact()' to know more.\n")

greet()


    
