#ΧΡΟΝΟΠΟΥΛΟΣ ΠΑΝΑΓΙΩΤΗΣ 321/2015222

#ΚΕΡΔΗ
performance=(0, 2.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),(0, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),(0, 0, 2.5, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0),(0, 0, 1, 4, 100, 0, 0, 0, 0, 0, 0, 0, 0),(0, 0, 0, 2, 20, 450, 0, 0, 0, 0, 0, 0, 0),(0, 0, 0, 1, 7, 50, 1600, 0, 0, 0, 0, 0, 0),(0, 0, 0, 1, 3, 20, 100, 5000, 0, 0, 0, 0, 0),(0, 0, 0, 0, 2, 10, 50, 1000, 15000, 0, 0, 0, 0),(0, 0, 0, 0, 1, 5, 25, 200, 4000, 40000, 0, 0, 0),(2, 0, 0, 0, 0, 2, 20, 80, 500, 10000, 100000, 0, 0),(2, 0, 0, 0, 0, 1, 10, 50, 250, 1500, 15000, 500000, 0),(4, 0, 0, 0, 0, 0, 5, 25, 150, 1000, 2500, 25000, 1000000)

numbers=int(input(" Give how many numbers from (1-12) : "))
while numbers<1 or numbers>12:#WHILE ΠΟΥ ΕΛΕΓΧΕΙ ΤΟ ΠΛΗΘΟΣ ΤΩΝ ΑΡΙΘΜΩΝ ΠΟΥ ΘΑ ΘΕΣΕΙ Ο ΧΡΗΣΤΗΣ (1-12)
    numbers=int(input(" Give how many numbers from (1-12) : "))
    
rnumbers=[0]*numbers
for kappa in range(0, numbers):
    rnumbers[kappa]=int(input(" Give number from (1-80) : "))
    while rnumbers[kappa]<1 or rnumbers[kappa]>80:#WHILE ΠΟΥ ΕΛΕΓΧΕΙ ΠΟΙΟΥΣ ΑΡΙΘΜΟΥΣ ΘΑ ΘΕΣΕΙ Ο ΧΡΗΣΤΗΣ (1-80) 
        rnumbers[kappa]=int(input(" Give number again from (1-80) : "))
        
amount=int(input(" Give the amount (1, 2, 5, 10) : "))
while amount!=1 and amount!=2 and amount!=5 and amount!=10:#WHILE ΠΟΥ ΕΛΕΓΧΕΙ ΠΟΙΟ ΠΟΣΟ ΘΑ ΘΕΣΕΙ Ο ΧΡΗΣΤΗΣ (1, 2, 5, 10)
    amount=int(input(" Give the amount again (1, 2, 5, 10) : "))
         
from random import randrange
numbersfound=0 #ΑΡΙΘΜΟΥΣ ΠΟΥ ΠΕΤΥΧΕ
inheritancenumbers=[0]*20
for kippo in range(0, 19):
    inheritancenumbers[kippo]=[randrange(80)+1]#ΤΥΧΑΙΟΙ ΑΡΙΘΜΟΙ
    print(inheritancenumbers)
    for kippo in range(0, numbers):
        for keppo in range(0, numbers):
            if rnumbers[kippo]==inheritancenumbers[keppo]:
                numbersfound=numbersfound+1
print(" Winnings from this lottery : ", amount*performance[numbers][numbersfound])
print (" Numbers we found : ", numbersfound)
if numbersfound==0:
    print(" No winnings from this lottery ")

