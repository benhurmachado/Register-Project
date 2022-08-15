from time import sleep
from os import system

#assign values for name and age
class Person: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

#main function to run the code
def main():

    people = []

    def search(people):
        #setting up the values for the lambda function inside the ".sort" to order the registers
        people.sort(key=lambda x: (x.age, x.name))
        for person in range(len(people)):
            #setting the ages to the right category using conditions
            if people[person].age <= 12: 
                category = "Kid"
            if people[person].age >= 13:
                category = "Teenager"
            if people[person].age >= 20:
                category = "Adult"
            if people[person].age >= 65:
                category = "Elderly"

            #showing to the user the people that already been registered
            print(f"Name: {people[person].name}, Age: {people[person].age}, Category: {category}") 

    def register(people):
        #using try and except to avoid some bugs
        try:
            name = str(input("Name: ").upper())
            age = int(input("Age: "))
            people.append(Person(name, age))
        except ValueError:
            print("Invalid option, please insert name and age properly")
            sleep(3)
            system("cls")
            main()
            
    #what the user is going to see to runs the code and select an option
    def hud(): 
        print("=" * 29)
        print("{:^30}".format("WELCOME TO THE REGISTER CODE"))
        print("=" * 29)
        print("[ 1 ] REGISTER \n[ 2 ] VIEW EXISTING REGISTRATIONS \n[ 3 ] QUIT")
        print("SELECT AN OPTION:")

    while True:
        hud()
        #user select an option
        option = str(input()) 
        if option == "1":
            #calling the register function
            register(people)
            print("LOADING...")
            #sleep function from time library to give dynamic for the code
            sleep(2) 
            #terminal cleaner
            system("cls") 
        elif option == "2":
            #calling the search function
            search(people)
            print("LOADING...")
            sleep(4)
            system("cls")
        elif option == "3":
            system("cls")
            break
        else:
            print('Invalid option...')
            sleep(1)
            system("cls")
main()

