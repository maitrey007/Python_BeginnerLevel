class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def __HelloWorld__(self):
        print("Hello world")

    def __del__(self):
        print("Object is deleted")

             
person1=Person("Mike",34,160)#calling a constructor 
print(person1.name)
print(person1.age) 
print(person1.height) 
person2=Person("Ani",21,179)
print(person2.name)
print(person1.__HelloWorld__())     #calling a method 
del person2    # deleting an object
