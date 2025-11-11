const nums = [2, 4, 6, 8];
let num=nums.map((num=>num+2))
console.log(num)//4,6,8,10
//fiter
const ages = [12, 17, 18, 22, 14, 30];
let age=ages.filter((age)=>{
    return age>=18;
})
console.log(age)
//find
const numbers = [3, 7, 12, 5, 20];
let number=numbers.find((number)=>{return number==12})
console.log(number)
//for each
const animals = ['dog', 'cat', 'lion'];

animals.forEach((animal, index) => {
  console.log(`${index}: ${animal}`);
});