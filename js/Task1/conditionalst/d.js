//largest 3 digit number
const input = require('prompt-sync')();
let num = parseInt(input("Enter number: "));
if(num>=100 && num <=999){
    console.log("three digit number")
}else{
    console.log("not three digit number")
}