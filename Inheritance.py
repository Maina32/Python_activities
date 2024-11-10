#Python Inheritance
class Animal:
    def fur(self):
        print("I have fur all over my body.")
class Dog(Animal):
    def bark(self):
        print("Dog barking.")
    def walk(self):
        print("Iawalk all day.")
class puppy(Dog):
    def play(self):
        print("I play all the time.")
bosco = puppy()
bosco.play()
bosco.bark()
bosco.fur()
