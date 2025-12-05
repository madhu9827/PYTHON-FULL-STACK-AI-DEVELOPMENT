class Two:
    a=20
    def __init__(self):
        self.b=10
        self.c=20
    def m1(self):
        self.d=30
    def m2(self):
        self.e=40
t1=Two()
t1.m1()
print(t1.__dict__)

t2=Two()
t2.m2()
print(t2.__dict__)