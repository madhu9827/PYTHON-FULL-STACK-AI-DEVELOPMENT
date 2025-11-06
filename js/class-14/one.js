function users(users){
    let rows=""
    for(let user of users){
            rows=rows+`<tr>
                        <td>${user.id}</td>
                        <td>${user.firstName}</td>
                        <td>${user.gender}</td>
                        <td>${user.email}</td>
                    </tr>`
        }
    document.getElementById('userData').innerHTML=rows
}
fetch('https://dummyjson.com/users')
  .then((response) => response.json())
  .then((json) => users(json.users));