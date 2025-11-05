let add=(a,b)=>a+b+1
let r1=add(10,20)
console.log(r1)


let wish=name=>"hello"+name+"gM"
let msg=wish("rahul")
console.log(msg)//fat arrow with implict

let wish1=(name)=>{
    return "hello"+name+"gm"
}
let msgs=wish1("rahul")
console.log(msgs)

//what is the advantage of using fat arrow function---concise code,implict return