#Kristian McMahon
#Linear Search

#Init
import random
attempts = 0
secret_number = random.randint(1, 100)

def linearsearch():
    global attempts
    for guess in range(1,101):
        if guess==secret_number:
            print(f"You found the secret number: {secret_number}.")
            print(f"The computer took {attempts} attempts.")
        else:
            attempts=attempts+1


#Main


#Binary Search
def binarysearch():
    global attempts
    low=1
    high=100
    found=False
    while found==False:
        for mid in range(1,101):
            mid = (low + high) // 2
            if mid>secret_number:
                high=mid-1
                attempts=attempts+1
            if mid<secret_number:
                low=mid+1
                attempts=attempts+1
            if mid==secret_number:
                found=True
    print(f"You found the secret number: {secret_number}.")
    print(f"It took the computer {attempts} attempts.")

#Main
binarysearch()
