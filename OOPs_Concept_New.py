# -*- coding: utf-8 -*-
"""OOPS Concept"""
#Try adding a inverse method to inverse fraction

class Fraction(object):
    """A number represented as a fraction"""
    def __init__(self,num,denom):
        assert type(num) == int and type(denom) == int
        self.num =num
        self.denom= denom
        """So far we have defined the internal representation of the data""" 
    def __str__(self):
        """ return a string represenatation of self """
        return str(self.num)+ "/"+ str(self.denom)
    def __add__(self,other):
        top= self.num*other.denom+ self.denom*other.num
        bott= self.denom*other.denom
        return Fraction(top,bott)
    """ return a fraction object of same type as Fraction"""
    def __float__(self):
        return self.num/self.denom
        
    def inverse(self):
        return Fraction(self.denom,self.num)   #defining your own method
        """returns a new fraction representing data type of Fraction object"""
       
#Now lets use the Fraction Object""""

a= Fraction(3,4)
b= Fraction(3,4)        

c= a+b  # c is a fraction object 
print(float(c))
print(Fraction.__float__(c))

print(float(a.inverse()))
