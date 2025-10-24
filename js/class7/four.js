let users=[{"uid":1,"uname":"madhu","gender":"Female"},
    {"uid":2,"uname":"lali","gender":"Female"},
    {"uid":3,"uname":"tanu","gender":"Male"},
    {"uid":4,"uname":"prakash","gender":"Male"}]
for( let user of users){
    if(user.gender==="Male"){
        console.log(user.uname)
    }
}

for( let user of users){
    if(user.gender==="Female"){
        console.log(user.uname)
    }
}