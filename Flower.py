# Tryna Rodman
# 7/2/23
# Description: This code demonstrates the implementation of a Flower class that represents different flowers.
# The Flower class has attributes such as 'name' and methods like 'grow' and 'bloom'.
# In the main function, two Flower objects are created and their methods are called.

class Flower:
    def __init__(self, name):
        self.name = name  # Attribute: Name of the flower

    def grow(self):
        print("The " + self.name + " is growing.")  # Method: Prints the growth message of the flower

    def bloom(self):
        print("The " + self.name + " is blooming.")  # Method: Prints the blooming message of the flower

def main():
    flower1 = Flower("Rose")  # Creating a Flower object with name "Rose"
    flower1.grow()  # Calling the grow method of the first flower object
    flower1.bloom()  # Calling the bloom method of the first flower object

    flower2 = Flower("Daisy")  # Creating another Flower object with name "Daisy"
    flower2.grow()  # Calling the grow method of the second flower object
    flower2.bloom()  # Calling the bloom method of the second flower object

if __name__ == "__main__":
    main()