"""
Created on 01/21/21

Program to Assignment #5

@author: Michelle Medina
"""


count = 0

def VerifyUser(uid,pw):
    #If the user logs in correctly, display a welcome message
    if (uid == "username" and pw=="password"):
        print('Hello, welcome!')
        return True;
    else:
        print("\nIncorrect Username/Password\n")
        
    #If the functions returns False, then you need to first check if the counter is 3
    global count
    count = count +1
    if (count == 3):
        #you need to display a Goodbye message
        print("Maxed out on tries, Goodbye!")
    else:
        #Else increment the global counter and display the number of incorrect attempts
        print("you have tried {} times, max is 3.\n".format(count))
        main()
    return False;
    

def aboutPage():
    print("\nAbout Page: Here is some text about a company \n")
    main()
       


def main():
    print("Enter 1 to login")
    print("Enter 2 to see About page")
    print("Enter 3 to end")
    choice = int(input("Make a choice: "))
    if choice == 1:
        uid = input("\nWhat is your Username? ")
        pw = input("What is your password? ")                                
     #get user ID and Password and pass them to VerifyUser function
        VerifyUser(uid,pw)                                 

    elif choice == 2:                                
        #display some text about a company or a website
        aboutPage()                              

    elif choice == 3:
        #display a good bye message
        print("Goodbye!")
    else: 
    #display a message that choice is invalid 
        print("Sorry, invalid choice - try again!")                         
                                      
main()
