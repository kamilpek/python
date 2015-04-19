class A:
    i = 1
    def __init__(self, a = 1):
        self.a = a

    def f(self):
        return self.a

    def getI(self):
        return self.__class__.i

class B1(A):
    j = -1
    def __init__(self):
        A.__init__(self,2)
        self.__class__.i += 1
        self.b = 3

    def f(self):
        return self.b - self.a

    def getI(self):
        return self.__class__.i + self.__class__.j

class B2(A):
    j = 0
    def __init__(self):
        A.__init__(self,4)
        self.__class__.i += 2
        self.b = 11

    def f(self):
        return self.a * self.b

    def getI(self):
        return self.__class__.i - self.__class__.j

class C(B1, B2):
    def __init__(self):
        B2.__init__(self)
        B1.__init__(self)

c = C()

print c.a, c.b, c.__class__.i, c.__class__.j, c.f(), c.getI()