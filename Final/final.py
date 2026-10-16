"""
Dog Rescue Application
CIS106 Final Project
Mikhail Luchanok

This program helps a dog rescue group keep track of dogs.
The user can add, view, find, and delete dogs.
The program saves the dog information to a text file.
"""

# Dog class
class Dog:
    '''Store information about a dog'''

    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight


# Display the menu
def menu():
    print()
    print("Dog Rescue")
    print("----------")
    print("1. Add a Dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Delete a Dog")
    print("5. Quit")
    print()

    choice = input("Select a choice: ")
    return choice


# Add a dog
def add_dog(dogs):
    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = int(input("Age: "))
    weight = int(input("Weight: "))

    new_dog = Dog(name, breed, age, weight)
    dogs.append(new_dog)

    print(name, "was added.")


# View all dogs
def view_dogs(dogs):
    if len(dogs) == 0:
        print("No dogs found.")
    else:
        print()
        print("Rescue Dogs")
        print("-" * 55)
        print(f"{'Dog':12} {'Breed':26} {'Age':>5} {'Weight':>8}")
        print("-" * 55)

        for dog in dogs:
            print(f"{dog.name:12} {dog.breed:26} {dog.age:>5} {dog.weight:>8}")


# Find a dog by name
def find_dog(dogs):
    name = input("Enter dog name to search: ")
    found = False

    for dog in dogs:
        if dog.name.lower() == name.lower():
            found = True
            break

    if found == True:
        print("Found", name)
    else:
        print("Sorry, unable to find", name)


# Delete a dog
def delete_dog(dogs):
    name = input("Enter dog name to delete: ")
    found = False

    for dog in dogs:
        if dog.name.lower() == name.lower():
            dogs.remove(dog)
            found = True
            break

    if found == True:
        print(name, "was deleted.")
    else:
        print("Sorry, unable to find", name)


# Save dogs to a text file
def save_dogs(dogs):
    file = open("dog_rescue_output.txt", "w")

    file.write("Rescue Dogs\n")
    file.write("-" * 55 + "\n")
    file.write(f"{'Dog':12} {'Breed':26} {'Age':>5} {'Weight':>8}\n")
    file.write("-" * 55 + "\n")

    for dog in dogs:
        file.write(f"{dog.name:12} {dog.breed:26} {dog.age:>5} {dog.weight:>8}\n")

    file.close()


# Main function
def main():
    dogs = []
    choice = ""

    while choice != "5":
        choice = menu()

        if choice == "1":
            add_dog(dogs)
            save_dogs(dogs)

        elif choice == "2":
            view_dogs(dogs)

        elif choice == "3":
            find_dog(dogs)

        elif choice == "4":
            delete_dog(dogs)
            save_dogs(dogs)

        elif choice == "5":
            save_dogs(dogs)
            print("Goodbye!")

        else:
            print("Invalid choice. Please enter 1 to 5.")


main()