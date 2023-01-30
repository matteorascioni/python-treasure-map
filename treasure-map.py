#Defining the map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
#Put the map inside a list to create a multidimension list and print it
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

#Dividing the 2 character of a string from the position input 
first_digit = position[0]
second_digit = position[1]

#Create 2 different pointers to search inside the list
row_pointer = int(second_digit) - 1 
column_pointer = int(first_digit) - 1
#Pointing to the right value inside the list and change it with a new one with the X string to mark the "treasure".
map[row_pointer][column_pointer] = 'X'

print(f"{row1}\n{row2}\n{row3}")

