import pyautogui as pag
import time
import os


def join_meeting(id_, check_flag):
    id_ = id_.strip()

    if check_flag == "check":
        print(
            '"check" retrieves ONLY the first ID found in your book and may not retrieve the correct ID'
        )
        print('"check" is NOT case-sensitive')

        time.sleep(1)

        with open(".saved", "r") as file:
            li = file.readlines()
        found = 0
        for i in li:
            check = i.split(":")
            if id_.lower() in check[0].strip().lower() or id_ in check[1].strip():
                id_ = check[1].strip()
                print(check[0].strip() + ": " + check[1].strip("\n"))
                found += 1
        if found >= 2:
            print(f"Warning: {found} results found")
            print("Picking first result")
        elif found < 1:
            print("Warning: 0 results found")
    elif check_flag == "nocheck":
        pass
    elif check_flag == "save":
        name = input("Meeting name: ")
        name = name.strip()
        with open(".saved", "a") as file:
            file.write(name + ": " + id_ + "\n")
        print(f'\n"{name}: {id_}" saved')
    else:
        return "Invalid argument"

    os.system(r"C:\Users\siddh\OneDrive\Desktop\zoom.lnk")

    join_button = pag.locateOnScreen("join.png", confidence=0.8, grayscale=True)

    time.sleep(1)

    pag.moveTo(join_button)
    pag.click()

    time.sleep(0.5)

    entry = pag.locateOnScreen("entry.png", confidence=0.8, grayscale=True)

    pag.moveTo(entry)
    pag.click()

    pag.typewrite(id_)

    vid_check = pag.locateOnScreen("vid.png", confidence=0.8, grayscale=True)

    pag.moveTo(vid_check)
    pag.click()

    meeting = pag.locateOnScreen("meeting.png", confidence=0.8, grayscale=True)

    pag.moveTo(meeting)
    pag.click()

    with open(".recent", "a") as f:
        f.write(id_ + "\n")

    return id_
    
def log_(opt):
    if opt == "add":
        name = input("Meeting name: ")
        id_ = input("Meeting ID: ")

        id_ = id_.replace(" ", "").strip()
        name = name.strip()

        with open(".saved", "a") as file:
            file.write(name + ": " + id_ + "\n")

        return f'"\n{name}: {id_}" saved'

    elif opt == "saved":
        print()
        with open(".saved", "r") as file:
            li = file.readlines()
        c = 0
        for i in li:
            print(i.strip("\n"))
            c += 1
        return f"\n{c} saved meeting(s)"

    elif opt == "del":
        print()
        with open(".saved", "r") as file:
            li = file.readlines()
        c = 0
        for i in li:
            print(i.strip("\n"))
            c += 1
        print(f"\n{c} saved meeting(s)\n")

        name = input("Meeting name: ")
        id_ = input("Meeting ID: ")

        name = name.strip()
        id_ = id_.strip()

        with open(".saved", "w") as f:
            for line in li:
                if line.strip("\n") != f"{name}: {id_}":
                    f.write(line)

        return f'\nAll saved "{name}: {id_}" deleted'

    elif opt == "search":
        with open(".saved", "r") as file:
            li = file.readlines()

        search = input("Meeting name or ID: ")
        n = 0
        print()
        for i in li:
            check = i.split(":")
            if search in check[0].strip() or search in check[1].strip():
                print(check[0].strip() + ": " + check[1].strip("\n"))
                n += 1
        return f"\n{n} result(s) found"

    elif opt == "recent":
        print()
        with open(".recent", "r") as file:
            li = file.readlines()
        k = 0
        for i in li:
            print(i.strip("\n"))
            k += 1
            if k == 10:
                break
        return "\nRecent meetings"
    else:
        return "Invalid argument"


os.system("cls")
print("pyautoZoom 2.3\n")

while True:
    user = input(">>")
    if user == "":
        continue
    cmd = user.split("\"")
    if cmd[0].lower().strip() == "join":
        print(join_meeting(cmd[1].strip(), cmd[2].strip()))
    elif "log" in cmd[0].lower().strip():
        option = cmd[0].lower().strip().split(" ")[1]
        print(log_(option))
    elif cmd[0] == "quit":
        break
    else:
        print("Invalid command")
