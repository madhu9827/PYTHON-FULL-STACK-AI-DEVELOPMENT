let numbers=[11,5,6,7,8,9,12]
let evens=numbers.filter((num)=>{
    return num%2===0;
})
console.log(evens) 

//implicit
let num=[1,2,3,4,5,6,7,8,9,10]
let eves=num.filter(num=>num%2===0)
console.log(eves)