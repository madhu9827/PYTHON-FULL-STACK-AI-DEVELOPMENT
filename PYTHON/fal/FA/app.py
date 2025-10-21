from fastapi import FastAPI
from database import get_db_connection
from pydantic import BaseModel
app=FastAPI()
@app.get('/')
def home_page():
    return{"msg":"application root received"}
class Employee(BaseModel):
    eid:int
    ename:str
    esal:float
@app.post("/emp")
async def create_emp(emp:Employee):
        print(emp)
        dbcon=get_db_connection()
        cur=dbcon.cursor()
        sql_str='INSERT into employees(eid,ename,esal) values(%s,%s,%s);'
        values=(emp.eid,emp.ename,emp.esal)
        print(values)
        cur.execute(sql_str,values)
        dbcon.commit()
        dbcon.close()
        return{"msg":"new emp is created successfuly"}


@app.get("/emp")
async def get_employees():
    dbcon=get_db_connection()
    cur=dbcon.cursor()
    sql_str="Select *from employees" 
    cur.execute(sql_str)
    employees=cur.fetchall()
    dbcon.commit()
    return employees
