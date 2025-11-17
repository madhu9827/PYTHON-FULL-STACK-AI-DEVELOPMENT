let employees=[{eid:101,ename:'madhu'},
    {eid:102,ename:'deepu'}
]
let createEmployee=(emp)=>{
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            let flag=true;
            if(flag){
                resolve("data inserted")
                employees.push(emp)
            }
            else{
                reject("failed")
            }
           
        },4000)

    });
}
let getEmployees=()=>{
    setTimeout(()=>{
        let rows="";
        for(let emp of employees){
            rows=rows+`<tr>
                        <td>${emp.eid}</td>
                        <td>${emp.ename}</td>
                       </tr>`
        }
        document.getElementById('tb_data').innerHTML=rows
    },1000)
}
createEmployee({eid:103,ename:"priya"})
.then((msg)=>{
    console.log(msg);
    getEmployees()
})
.catch((err)=>{
    console.log(err)
})