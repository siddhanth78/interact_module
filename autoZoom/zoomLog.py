import sys


def log_(opt):
    if opt == "save":
        name = input("Meeting name: ")
        id_ = input("Meeting ID: ")

        id_ = id_.replace(" ", "").strip()
        name = name.strip()

        with open(".saved", "a") as file:
            file.write(name + ": " + id_ + "\n")

        return f'"\n{name}: {id_}" saved'

    elif opt == "book":
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


print(log_(sys.argv[1]))
