class Person:
    pass
class Teacher(Person): # 继承
    pass
class Worker(Person):
    pass
class Programmer(Person):
    pass

class Factory:
    def get_person(self, p_type):
        if p_type == "t":
            return Teacher()
        elif p_type == "w":
            return Worker()
        elif p_type == "p":
            return Programmer()
factory = Factory()
worker = factory.get_person("w")
print(type(worker))
teacher = factory.get_person("t")
print(type(teacher))
programmer = factory.get_person("p")
print(type(programmer))