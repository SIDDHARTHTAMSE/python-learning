# Multiple Inheritance

# One child inherits from multiple parents.



# Example 1

class Father:

    def property(self):
        print("Father Property")

class Mother:

    def jewellery(self):
        print("Mother Jewellery")

class Child(Father, Mother):
    pass

c = Child()

c.property()
c.jewellery()


# Example 2

class Camera:

    def click(self):
        print("Photo Taken")

class Music:

    def play(self):
        print("Music Playing")

class Phone(Camera, Music):
    pass

p = Phone()

p.click()
p.play()