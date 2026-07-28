class Xyz():
    def abc(selfself,a,b=None,c=None):

        if b and c:
              print(a*b*c)
        elif b:
            print(a+b)
        else:
            print("hello",a)

        x1=Xyz()
        x1.abc("akhil")
        x1.abc(5,6)
        x1.abc(3,4,5)
