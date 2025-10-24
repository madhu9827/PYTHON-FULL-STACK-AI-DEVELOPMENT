let users=[{"id":101,"name":"tanu","email":"tanu3212gmail.com","gender":"male"},
    {"id":102,"name":"madhu","email":"madhu@gmail.com","gender":"female"},
    {"id":103,"name":"lali","email":"lali@gmail.com","gender":"female"}]
    // for(var i=0;i<=users.length-1;i++)
    // {
    //     console.log(users[i].id)
    //     console.log(users[i].name)
    // }
for(user of users){
    console.log("userid"+user.id+"username"+user.name)
}