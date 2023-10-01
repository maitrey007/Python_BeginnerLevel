class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def __str__(self):
        return "Name:{} ,Age:{}, Height:{}".format(self.name,self.age,self.height)

class Worker(Person): #inheiting the  parent class

    def __init__(self,name,age,height,salary):
        super(Worker,self).__init__(name,age,height)
        self.salary=salary

    def __str__(self): #over writing the str function
        text=super(Worker,self).__str__()
        text +=", Salary : {}".format(self.salary)
        return text  
    def cal_yearly_sal(self):
       return self.salary *12          

worker1=Worker("Mike",34,170,1200)
print(worker1)
print(worker1.cal_yearly_sal())    
