function calc(){
    let numbers=[10,20,30,40]
    for(let num of numbers){
        if(num%2!==0){
            return; 
            //break;//it stops the iteration and come out form loop
        }
        console.log(num)
    }
    console.log("gm")
}
calc()