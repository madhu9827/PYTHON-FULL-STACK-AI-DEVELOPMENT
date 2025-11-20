var users;
async function display_users(){
    users= await fetch('https://jsonplaceholder.typicode.com/users')//it returns one promise object
    .then((resp)=>{return resp.json()})
    .then((data)=>{return data})
console.log(users);
let rows="";
for( let user of users){
    rows=rows+`<tr>
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
                </tr>`
}
document.getElementById('tb_data').innerHTML=rows
}
display_users()