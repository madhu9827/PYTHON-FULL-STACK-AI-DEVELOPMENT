//wap is divisble by 7 or not
const input = require('prompt-sync')();
let num = parseInt(input("Enter number: "));
if (num % 7 == 0) {
    console.log("It is divisible by 7");
} else {
    console.log("Not divisible by 7");
}
