 # Author          : Anne Margaret F. Palaypayon
   # Course and Year : BSIT-2
   # Filename        : Palaypayon-probb.py
   # Description     : Write a program that reads an integer $n$ and prints the sequence $F_n$ of Fibonacci numbers as a comma-separated list on a single line.
   # Honor Code      : I have not given nor received any unathorized help in
   #                   completing this exercise. I am also well aware of the 
   #                   policies stipulated in the AdNU student handbook.

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1