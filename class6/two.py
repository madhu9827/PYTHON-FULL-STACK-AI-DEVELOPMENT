import order as ord
print(type(ord.price))

from order import price,order_status
print(price)

from order import price,order_status as status,order as ord
print(type(status))
print(type(ord))
print(status())