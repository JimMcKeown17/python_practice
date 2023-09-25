def add(*args):
    ans=0
    for arg in args:
        ans += arg
    return ans

# print(add(2,3,4,5,55))

def calculate(n,**kwargs):
    print(kwargs["multiply"])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

print(calculate(2,add=3, multiply=4))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="foo")
print(my_car.model)