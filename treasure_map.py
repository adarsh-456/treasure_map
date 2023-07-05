import random
row1=["🤣", "🤣", "🤣"]
row2=["👹", "👹", "👹"]
row3=["💀", "💀", "💀"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
list1=[11,12,13,21,22,23,31,32,33]
number=str(random.choice(list1))
row=int(number[1])
colomn=int(number[0])
map[row-1][colomn-1]="👑"

guessed_location =input("guess the treasure location between 11 to 33 :")
if number==guessed_location:
    print("YOU WIN!")
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("YOU lost!")
    print("The location of treasure is: "+number)

