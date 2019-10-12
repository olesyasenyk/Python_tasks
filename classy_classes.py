# complete this Class, the Person class has been created. 
# fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter 
# which should return johns age is 34
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info="{}s age is {}".format(self.name,self.age)
        
    def inform(self):
        print(self.info)