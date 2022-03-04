import sys

if len(sys.argv) != 4:
    print("Requires 3 arguments (length width height)")
    quit(0)

try:
    l = int(sys.argv[1])
    w = int(sys.argv[2])
    h = int(sys.argv[3])
except:
    print("Arguments must be integers")
    quit(0)
else:
    pass
    
if l > 20 or w > 20 or h > 20:
    print("Max dimension 20x20x20")
    quit(0)

initial_l = "__" * l + "_"

final_l = "__" * l

space = "  " * l

h_count = h
w_count = w

h_space = 0

print(" " * w_count + initial_l)

for i in range(w-1, -1, -1):

    fill = space

    if i == 0:
        fill = final_l

    if h_count == 0:
       w_space = h_space
       print(" " * i + "/" + fill + "/" + " " * w_space + "/")
       w_count-=1
    else:
        print(" " * i + "/" + fill + "/" + " " * h_space + "|")
        h_count-=1
        h_space+=1
        

remaining_h = h_count
remaining_w = w_count

h_space-=1

for i in range(0, h):
    
    fill = space
    
    if i == h-1:
        fill = final_l
    
    if remaining_h == 0:
        print("|" + fill + "|" + " " * h_space + "/")
        h_space-=1
    else:
        print("|" + fill + "|" + " " * h_space + "|")
        remaining_h-=1