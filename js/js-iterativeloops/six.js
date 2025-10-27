//let numbers=[18,31,8,7,232,1055,96,11]
//let no_evens=0
/* for(let i=0;i<=numbers.length-1;i++){
    if(numbers[i]%2==0){
        no_evens++;
    }
}
console.log("no of evens",no_evens) */
//while loop
/* let numbers=[18,31,8,7,232,1055,96,11];
let i=1;
let No_evens=0;
while(i<=numbers.length-1){
    if(numbers[i]%2==0){
        No_evens++;
    }
    i++;
}
console.log(No_evens) */
//for of loop
let numbers=[18,31,8,7,232,1055,96,11]
let no_evens
for(let num of numbers){
    if(num%2===0){
        no_evens++;
    }
}
console.log(no_evens)