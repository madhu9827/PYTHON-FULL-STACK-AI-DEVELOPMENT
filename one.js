//wap--given number is even or odd
//read data from user
let input= require('prompt-sync')()

let num= parseInt(input("enter number:"))
if(num %2 ==0){
    console.log("even number")
}
else{
    console.log("odd number")
}