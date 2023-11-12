class User:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

user1 = User("Joe", "Smith", 68)
print(user1.age)