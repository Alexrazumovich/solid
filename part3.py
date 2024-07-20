# class Bird():
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print(f"{self.name} is flying")
# class Ping(Bird):
#     pass
#
# p=Ping("Sara")
# p.fly()
class Bird():
    def fly(self):
        print(f"This bird is flying")
class Duck(Bird):
    def fly(self):
        print(f"This duck is flying quickly")
def fly_in_the_sky(animal):
    animal.fly()
b=Bird()
d=Duck()
fly_in_the_sky(b)
fly_in_the_sky(d)