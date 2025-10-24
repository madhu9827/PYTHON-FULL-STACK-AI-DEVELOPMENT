let users=[{"id":101,"name":"tanu","email":"tanu3212gmail.com","gender":"male"},
    {"id":102,"name":"madhu","email":"madhu@gmail.com","gender":"female"},
    {"id":103,"name":"lali","email":"lali@gmail.com","gender":"female"}]
for(user of users){
    if(user.gender==="male")
    {
        console.log(user.name+" Gender:"+user.gender)
    }
}