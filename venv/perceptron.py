import random
import turtle
# p = [[1,1.5,3,1.5,2,6.5],
#       [2,3,3.5,1,1,6]]
#
# t = [1,1,1,0,0,0]
#
# w = random.uniform(0, 1)
# b = random.uniform(0,1)
#
#
#
#
#
# print(w)
# print(b)
#
# for i in t:
#     print(i)
#
# for i in p:
#     for x in i:
#         print(x)
from builtins import print


class Percepton:


    def __init__(self):
        # self.p = [[6.5,1.5, 3,5, 1.5, 2,1,4.5,6],
        #         [6,3,3.5,6.5,1,1,2,5.5,5.5]]
        # Macierz x i y
        # self.p = [[1,1.5,3,1,2,3.4,4.5,4,1.5,2,3,4,5,5.5,6,6],
        #           [2,3,3.5,4,5,5,5.5,6,1,1,2,3.5,3,4,5.5,1]]
        # Vektor wartosci
        # self.t = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        # Poczadkowe wartosci w i b
        self.p = [[1,1.5,1.5,2,3,3,1,4,2,5,3.5,5.5,4.5,6],[2,1,3,1,3.5,2,4,3.5,5,3,5,4,5.5,5.5]]
        self.t=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

        self.w = random.uniform(0, 1)
        self.w2 = random.uniform(0, 1)
        self.b = random.uniform(0, 1)

    def lern(self):
        a = 0;
        # for i in range(0,2222222222):
        while True:
            wat = 0
            for x in range(0,len(self.p[0])):
                a = (self.w * self.p[0][x]) + (self.w2 * self.p[1][x]) + self.b

                if(a>0):
                    y = 1
                else:
                    y = 0
                e = self.t[x] - y
                if(e > 0 or e < 0):
                    wat = 1
                    self.w = self.w + e * self.p[0][x]
                    self.w2 = self.w2 + e * self.p[1][x]
                    self.b = self.b + e
            if (wat == 0):
                break






    def what(self,x,y):
        a = self.w * x + self.w2 * y + self.b
        print(a)
        if (a > 0):
            y = 1
        else:
            y = 0

        print(y)


per = Percepton()
per.lern()
print("Koniec nauki")
while True:
    x = input()
    y = input()
    per.what(float(x),float(y))