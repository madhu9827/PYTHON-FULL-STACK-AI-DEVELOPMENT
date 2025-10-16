let emp=[
    {"eid":101,"ename":"lali","esal":45000},
    {"eid":102,"ename":"nithi","esal":35000},
    {"eid":103,"ename":"priya","esal":35000}
]
//read
console.log(emp[0].ename)
console.log(emp[2].ename)
console.log(emp[1].ename)

for(let em of emp){
    console.log(em.ename)
    console.log(em.eid)
}