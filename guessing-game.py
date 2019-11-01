def main ():
    animal = "tiger"
    

    while True:
        print( "Thinking of an animal")
        answer = input ( "Enter Your Guess").lower()
        
        if answer == animal:
            print ("You are correct")
            ans = input("Do you like this Animal Press Y or N")
            if ans == "y":
                print("Good")
            elif ans == "n":
                print("Bad")
                
            break
        elif answer[0] == "q":
            break

        else:

            print ("You are incorrect,Try Again")
                
    


main()
