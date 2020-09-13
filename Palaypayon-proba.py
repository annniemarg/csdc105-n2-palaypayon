 # Author          : Anne Margaret F. Palaypayon
   # Course and Year : BSIT-2
   # Filename        : Palaypayon-proba.py
   # Description     : Write a program that prints a triangle shape composed of specific ASCII character.
   # Honor Code      : I have not given nor received any unathorized help in
   #                   completing this exercise. I am also well aware of the 
   #                   policies stipulated in the AdNU student handbook.

size=int(input("Enter how many rows: "))
ch=input()
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print(ch, end=' ')
    print(" ")