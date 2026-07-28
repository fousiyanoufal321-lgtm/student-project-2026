class Car:
    def details(self,name,color):
        self.name=name
        self.color=color


c1=Car()
c2=Car()

c1.details("BMW", "Black")
c2.details("Audi","White")
print(c1.name)
print(c2.color)
