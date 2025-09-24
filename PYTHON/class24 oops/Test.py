class Test:
    def m1(self):
        print("m1 method")
    @classmethod
    def m2(cls):
        print("m2 method")
    @staticmethod
    def m3():
        print("m3 method")
t1=Test()
t2=Test()

t1.m1()
t1.m2()
t1.m3()

t2.m1()
t2.m2()
t2.m3()