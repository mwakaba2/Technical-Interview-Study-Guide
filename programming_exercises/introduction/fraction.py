#need this for truediv to work for 2.7
from __future__ import division

def reduced(m,n):
    num = m
    den = n
    # Using Euclid's Algorithm to solve gcd
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return Fraction(num//n, den//n)

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self,other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        added = reduced(newnum,newden)
        return added

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        subtracted = reduced(newnum,newden)
        return subtracted

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        multiplied = reduced(newnum, newden)
        return multiplied

    def __truediv__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        divided = reduced(newnum, newden)
        return divided

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x - y)
print(x * y)
print(x / y)
print(x.getNum())
print(x.getDen())
