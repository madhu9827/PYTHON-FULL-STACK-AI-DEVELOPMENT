//callback

function sum(a,b){
    return a+b;
}
function multi(a,b){
    return a*b;
}
function calc(a,b,callback){
    return callback(a,b)
}
let r1=calc(10,20,sum);
console.log(r1)
let r2=calc(10,20,multi);
console.log(r2)
//r4
//r3
//r2
//r1