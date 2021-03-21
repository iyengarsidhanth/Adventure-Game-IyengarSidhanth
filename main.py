print("Welcome to the Police Chase,You using a motercycle and trying to get far away from the  cops and you have jewels from the jewelry.Try,to not get caught and Good Luck!!")

print("What would you like to do")
print("(A) rest")
print("(B) Drink water")
print("(C) full speed")
print("(D) Check Stats")
print("(E) moderate speed")


exit="f"


while(exit !='q'):
 

 print("If you want to leave the game press 'q' or to continue press any other key ")
 exit= input("Enter your choice: ").lower()
 
 if(exit=="a"):
   print("You want to rest")
 if( exit=="b"):
  print("You want to drink water")
 if( exit=="c"):
  print("You want to  go full speed!")
 if( exit=="d"):
  print("You want to Check Stats")
 if(exit=="e"):
  print("You want to go moderate speed")


