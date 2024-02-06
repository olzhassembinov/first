class Upper:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
        pass
    x = 5


p1 = Upper("Olzhas", 20)
print(p1.name)
print(p1.age)
print(p1.x)
print(p1)

