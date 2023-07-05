import pyautogui as pag
import time
import os
import sys


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


print(join_meeting(sys.argv[1], sys.argv[2]))
