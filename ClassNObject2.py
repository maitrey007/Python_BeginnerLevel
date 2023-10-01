class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def __str__(self): #this function is used to print an object 
        return "Name: {},Age: {},Height: {}".format(self.name,self.age,self.height)    

person1=Person("Mike",34,150)
print(person1)   #printing the object 
