PlayerName = input("Please enter your name ")
print("Welcome " + PlayerName + " would you like to hear a joke?: ")
Responce1 = input()
if Responce1.lower() == "yea" or Responce1.lower() == "yes":
    print("Knock Knock")
    Responce2 = input()
    if Responce2.lower() == "who's there" or Responce2.lower() == "whos there":
        print("Frog")
        Responce3 = input()
        if Responce3.lower() == "frog who":
           print("Frog-et about it")
        else:
          print("OOOO You Almost had it, You gotta be Quicker than that!")
          
      
    else:
            print("Well I guess you didnt want to hear a joke for real...")
           
else:
    print("Well it was a good joke....")
        
