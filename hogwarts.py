#Hogwarts
#Program asks for a name and assigns that person to one of the four harry potter houses

#Init
import time
import random

#Functions
def main():
    while True:
        print("Welcome to Hogwarts")
        name=input("What is your name: ").lower()
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print(house(name))
        start=input("Do you want to be assigned to a new house").lower()
        if start=="yes":
            print("Restarting now...")
        if start=="no":
            break

#This function checks a name and returns a house from harry potter
def house(name):
    if name == "harry" or name == "hermione" or name == "ron":
        return("Gryffindor")
    if name == "newt" or name== "nymphadora" or name == "pomona" or name == "credric":
        return("Hufflepuff")
    if name == "luna" or name == "cho" or name == "filius":
        return("Ravenclaw")
    if name == "voldemort" or name == "draco" or name == "severus":
        return("Slytherin")
    else: 
        x=random.randint(1,4)
        if x==1:
            return ("Gryyfindor")
        if x==2:
            return ("Hufflepuff")
        if x==3:
            return ("Ravenclaw")
        if x==4:
            return ("Slytherin")

#Main
main()
