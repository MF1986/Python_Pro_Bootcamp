#ROW 1 = 11, 12, 13
#ROW 2 = 21, 22, 23
#ROW 3 = 31, 32, 33

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")

x = int(position[0])
y = int(position[1])
map[x -1][y -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
