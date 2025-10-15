let a={} //js-object
let emp={
    "eid":101,
    "ename":"madhu"
    }
//read object
console.log(a)
console.log(emp)
console.log(emp.eid)
console.log(emp.ename)
console.log(emp.loc)
//update
emp.esal="5000.55"
console.log(emp)//add
emp.eid=102
console.log(emp)
console.log(typeof(a))
//delete
delete emp.eid
console(emp)