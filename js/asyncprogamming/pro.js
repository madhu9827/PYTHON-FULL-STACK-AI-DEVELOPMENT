let go=(success,failure)=>{
    let ac_bal=28000;
    if(ac_bal>=15000){
        success("go to enjoy")
    }
    else{
        failure("go to pro stack")
    }
}
go((msg)=>{console.log(msg)},(err)=>{console.log(err)})
//promise-for achieving asumchoronous pogram