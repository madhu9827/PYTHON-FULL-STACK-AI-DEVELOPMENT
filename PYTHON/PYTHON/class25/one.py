class one:
    def __init__(self,id,name):
        self.one_id=id
        self.one_name=name
    def open(self):
        print("it is opened")
a1=one(101,"madhu")
a2=one(102,"lali")
a3=one(103,"tanu")

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)