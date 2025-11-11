// without filter
let numbers=[11,5,6,7,8,9,12]
let even=[]
for(let num of numbers){
    if(num%2===0){
        even.push(num)
    }
}
console.log(even)