'''

Blueprint

l = __ * length

initial l = __ * length + _

w = / * width

h = | * height

V = l x w x h

Example:

1x1x1

 ___
/__/|
|__|/


2x2x2

  _____
 /    /|
/____/ |
|    | /
|____|/


3x5x8

     _______
    /      /|
   /      / |
  /      /  |
 /      /   |
/______/    |
|      |    |
|      |    |
|      |    |
|      |    /
|      |   /
|      |  /
|      | /
|______|/


6x1x4


 _____________
/____________/|
|            ||
|            ||
|            ||
|____________|/

'''



l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))

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