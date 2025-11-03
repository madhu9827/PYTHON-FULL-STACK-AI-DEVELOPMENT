//wap multiple by 3 or not
const input = require('prompt-sync')();
let num = parseInt(input("Enter number: "));
if(num % 3==0){
    console.log("it is multiple by 3")
}else{
    console.log("not nultiple by 3")
}