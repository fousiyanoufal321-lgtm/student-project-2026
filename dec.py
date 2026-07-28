def xyz(x):
    return x+10 # return abc(4,5)+10


def abc(a,b):
    return a+b


print(xyz(abc(4,5)))











def main(fn):
    def sub():
        print("hello")
        fn()
        print("hii")
    return sub()
@main # main(xyz)
def xyz():
    print("akhil")

xyz()










