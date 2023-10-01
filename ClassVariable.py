class Person:
    amount=0

    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
        Person.amount +=1

    def __del__(self) :
        Person.amount -=1

person1=Person("Mike",23,180)
person2=Person("Ani",22,170)
print(person1.name)
print(person2.name)
print(person1.age)  
print(person2.age)        
del person1
print(Person.amount)
del person2
print(Person.amount)
