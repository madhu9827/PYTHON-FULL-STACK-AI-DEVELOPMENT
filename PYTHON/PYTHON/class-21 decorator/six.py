from six1 import login_req
def home_page(is_login):
    print("home page")
def product(is_login):
    print("product page")
@login_req
def orders(is_login):
    print("orders page")
@login_req
def profile(is_login):
    print("profile page")
'''
home_page(False)
product(False)
orders(False)
profile(False) '''

home_page(True)
product(False)
orders(False)
profile(False)