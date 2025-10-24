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
'''Update
Usage: Update existing employee details
REST API URL: 127.0.0.1:8000/emp/{eid}
Method Type: PUT
Required Fields: eid,ename, esal
Access Type: Public
'''

@app.put("/emp/{eid}")
def update_emp(eid: int, emp: Employee):
    dbcon = get_db_connection()
    cur = dbcon.cursor()
    sql_st = "UPDATE employees SET ename = %s, esal = %s WHERE eid = %s;"
    values = (emp.ename, emp.esal, eid)
    cur.execute(sql_st, values)
    dbcon.commit()
    rows_affected = cur.rowcount
    cur.close()
    dbcon.close()

    if rows_affected == 0:
        return {"msg": f"No employee found with ID {eid}"}
    else:
        return {"msg": f"Employee with ID {eid} updated successfully"}


# DELETE (DELETE)
'''
Update
----------
Usage: Update existing employee details
REST API URL: 127.0.0.1:8000/emp/{eid}
Method Type: PUT
Required Fields: eid,ename, esal
Access Type: Public
'''
@app.delete("/emp/{eid}")
def delete_emp(eid: int):
    dbcon = get_db_connection()
    cur = dbcon.cursor()
    sql_st = "DELETE FROM employees WHERE eid = %s;"
    cur.execute(sql_st, (eid,))
    dbcon.commit()
    rows_affected = cur.rowcount
    cur.close()
    dbcon.close()

    if rows_affected == 0:
        return {"msg": f"No employee found with ID {eid}"}
    else:
        return {"msg": f"Employee with ID {eid} deleted successfully"}
