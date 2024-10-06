#ΧΡΟΝΟΠΟΥΛΟΣ ΠΑΝΑΓΙΩΤΗΣ 321/2015222

def exercise1():#ΣΥΝΑΡΤΗΣΗ exercise1
   string=input( "\n Give a string : " )#ΔΩΣΕ STRING
   for kappa in range(0, len(string) ):#ΜΙΑ FOR ΓΙΑ ΤΟ ΜΗΚΟΣ ΤΟΥ STRING
      if string[kappa] >= '0' and string[kappa] <= '9':
         char=int(string[kappa])
         for keppo in range(1, char ):#ΜΙΑ FOR ΓΙΑ ΤΟΥΣ ΠΟΣΟΥΣ ΧΑΡΑΚΤΗΡΕΣ ΘΑ ΕΚΤΥΠΩΣΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ
            print( string[kappa+1], end = "")
      else:
               print( string[kappa], end = "")
   return

while True:#ΕΠΑΝΑΛΗΨΗ WHILE ΟΠΟΥ ΚΑΛΟΥΜΕ ΤΗΝ ΠΑΡΑΠΑΝΩ ΣΥΝΑΡΤΗΣΗ ΕΠΑΝΑΛΗΠΤΙΚΑ
   exercise1()
