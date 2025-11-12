let emp={eid:101,
    ename:"rahul",
    details:{
        email:'rg@gmail.com',
        loc:'wayaand'
    }
}
// // console.log(ename)//reference error
// console.log(email)
// console.log(emp.details.loc)//wayaand
// let {ename}=emp;
// console.log(ename);//rahul

let {ename,details}=emp
let{loc}=details;
console.log(ename);//rahul
console.log(loc)//wayaand