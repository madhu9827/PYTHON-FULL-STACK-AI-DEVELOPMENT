let a=[10,20,30,40]
let b=[30,50,60,70,80]
let c=[...a,...b]
console.log(c)

// //merge objects
// let emp1={ename:"rahul",email:'madhu@gmail.com'};
// let emps1={email:'madhu@gmail.com',loc:'waynawd'}
// let emp_details1={...emp1,...emps1}
// console.log(emp_details)
//extract array/objects
let num=[10,20,30,40]
let num1=[...num,50,60,70]
console.log(num1)
//extract objects
let emp={ename:"rahul",email:'madhu@gmail.com'};
let user={...emp,avail:true}
console.log(user)
