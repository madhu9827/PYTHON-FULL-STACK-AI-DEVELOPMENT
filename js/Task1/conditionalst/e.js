const input = require('prompt-sync')();
let num = parseInt(input("Enter number: "));
if(num%2==0){
    console.log("even number")
}else{
    console.log("odd number")
}