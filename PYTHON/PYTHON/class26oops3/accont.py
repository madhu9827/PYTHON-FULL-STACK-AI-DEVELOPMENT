class accont:
    min_bal=500
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
    @classmethod
    def get_min_bal(cls):
        pass
    @staticmethod
    def cal_interest():
        tax=5
a1=accont(101,"tanuj")
a2=accont(102,"lali")
print(a1.__dict__)
print(a2.__dict__)
