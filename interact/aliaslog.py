try:
    import mysql.connector
except:
    print("mysql-connector-python (installation reqd. - yes)")
    time.sleep(3)
    quit()
else:
    pass



def newalias(sqlpass="",sqluser="root",sqlhost="localhost",key="",data=""):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass
            )
        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to server. Probably because invalid credentials.\n")
        return
    else:
        try:
            cursor.execute("create database if not exists shortcuts")
            cursor.execute("use shortcuts")
            cursor.execute("create table if not exists shortcutlog(_key_ varchar(100) not null unique,_data_ varchar(300) not null unique)")
            cursor.execute(f"insert into shortcutlog values('{key}','{data}')")
            mydb.commit()
        except:
            print("\nInvalid data.\n")
            return
        else:
            return
    


def getalias(sqlpass="",sqluser="root",sqlhost="localhost",key=""):
    p=""
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = "shortcuts"
            )
        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        lik=[]
        cursor.execute(f"select _key_ from shortcutlog")
        for k in cursor:
            lik.append(k[0])
        if key not in lik:
            print("\nKey not found.\n")
            return p
        else:
            cursor.execute(f"select _data_ from shortcutlog where _key_ = '{key}'")
            for x in cursor:
                p = x[0]
            return p



def deletealias(sqlpass="",sqluser="root",sqlhost="localhost",key=""):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = "shortcuts"
            )
        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        lik=[]
        cursor.execute(f"select _key_ from shortcutlog")
        for k in cursor:
            lik.append(k[0])
        if key not in lik:
            print("\nKey not found.\n")
            return
        else:
            cursor.execute(f"delete from shortcutlog where _key_ = '{key}'")
            mydb.commit()
            return



def updatealias(sqlpass="",sqluser="root",sqlhost="localhost",key="",newdata=""):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = "shortcuts"
            )
        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        lik=[]
        cursor.execute(f"select _key_ from shortcutlog")
        for k in cursor:
            lik.append(k[0])
        if key not in lik:
            print("\nKey not found.\n")
            return
        else:
            cursor.execute(f"update shortcutlog set _data_ = '{newdata}' where _key_ = '{key}'")
            mydb.commit()
            return



def showalias(sqlpass="",sqluser="root",sqlhost="localhost"):
    try:
        mydb = mysql.connector.connect(
            host = sqlhost.strip(),
            user = sqluser.strip(),
            passwd = sqlpass,
            database = "shortcuts"
            )
        cursor = mydb.cursor()
    except:
        print("\nError. Couldn't connect to database. Probably because database doesn't exist, invalid credentials or invalid database name.\n")
        return
    else:
        cursor.execute(f"select * from shortcutlog")
        print("\nFormat -> Key : Data\n")
        print("\n---Alias list---\n")
        for x in cursor:
            print(x[0]+" : "+x[1])
        return

    
