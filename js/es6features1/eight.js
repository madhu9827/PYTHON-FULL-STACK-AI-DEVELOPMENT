
let employees=[{eid:101,ename:"madhu",esal:23445,gender:"female"},
    {eid:102,ename:"nithi",esal:34645,gender:"male"},
    {eid:103,ename:"lali",esal:34566,gender:"female"}
]
// let emp=employees.find((emp)=>{
//     return emp.gender==='male'
// })
// console.log(emp)
let emp=employees.filter(emp=>emp.gender==='female')
console.log(emp)
