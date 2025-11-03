//positive or not
const input=require('prompt-sync')();
let num=parseInt(input("enter number"))
if(num===0){
    console.log("neither positive or negative number")
}
else if(num>0){
    console.log("positive number")
}
else{
    console.log("negative number")
}