# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Aaron Green
# Created: YYYY-MM-DD
def main():

    #get " user's first and last names
    #def uname():
    first = input( "Enter your first name: ")
    last = input("Enter your last name: ")
    #TODO modify this to generate a Marist-style username
    uname = first + str(".")+ last
    print (uname.lower())
    #ask user to create a new password
    passwd = input("Create a new password: ")
    #TODO modify this to ensure the password has at least 8 characters
    while len(passwd) < 8:
        print("This password is not good")
        print("Enter new password")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    print("Account configured. Your new email address is", uname.lower()S + "@marist.edu")

def notStrongenough():
    if len(passwd)<8:
       return True
    elif password.lower()== passwd:
       return True
    elif passwaor.upper()== passwd:
        return True
    else:
        for i in password:
            if i is digit():
                return False
    return True
    
main() 
 
#def getName():
   # first = input
   # last = input
   # return[first,last]
#name = getName()
#name[0]
#name[1]

#def createUname(name):
    #return name[0]+''+name[i]
