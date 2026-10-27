'''Overload Operators
Outline:
Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.'''
class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a <  other.a):
            return "obj 1 is less than obj 2"
        else:
            return "obj 2 is less than obj 1"
    def __eq__(self, other):
        if (self.a == other.a):
            return "both are equal"
        else:
            return "both are not equal"
obj1 = A(2)
obj2 = A(3)
print ("passed values:" ,obj1.a,obj2.a)
print(obj1 < obj2)
obj3 = A(4)
obj4 = A(4)
print("passes values:", obj3  , obj4)
print(obj3 == obj4)