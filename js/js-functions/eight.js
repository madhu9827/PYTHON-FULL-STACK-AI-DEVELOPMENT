let numbers=[10,20,15,13,36]
for(let num of numbers){
    if(num%2!==0){
        break;//comes out from loop not block
    }
    console.log(num)
}
