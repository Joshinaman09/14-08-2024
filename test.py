class parent_class:  

    def summation(self,num1,num2):  

        return num1+num2;  

class child_class(parent_class):  #inheriting parent_class

    def Average(self,num1,num2): 

        return num1/num2;  

fm=child_class() 

print(fm.Average(10,20))

print(fm.Summation(78,10))