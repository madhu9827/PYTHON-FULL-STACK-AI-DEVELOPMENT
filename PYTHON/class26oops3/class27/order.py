class order:
    def __init__(self,id,name,price): #self is a pointer pointing to current object
        self.order_id=id
        self.details=name
        self.price=price
    def add_discount(self):
        self.discount=50 
    @classmethod
    def check_avail(cls,self):
        self.avail=True
    def get_orderdetails(self):
        print("self_details")                                








o1=order(11,'mp1',12)
o1.add_discount()
o1.status="inprogress"
print(o1.price)
o2=order(12,'mp2',10)
o2.add_discount()
o2.get_orderdetails()
o3=order(13,'mp3',20)
o3.add_discount()
o3.status="delievered"
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
o3.price=48
print(o3.price)
o3.get_orderdetails()
del o2.price
print(o2.__dict__)