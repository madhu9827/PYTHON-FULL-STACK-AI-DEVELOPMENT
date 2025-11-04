//print least number in three numbers
const input = require('prompt-sync')();
let num = parseInt(input("Enter number: "));
let num1=parseInt(input("enter number:"));
let num2=parseInt(input("enter number"))
if(num<num1 && num1 < num2){
    console.log("num is least number")
}else if(num1<num2){
    console.log("num1 is leastnumber")
}
else{
    console.log("num2 is least number")
}