// let ct=new Date().toLocaleTimeString();
// document.getElementsByTagName('p')[0].innerHTML=ct
setInterval(()=>{
    document.getElementsByTagName('p')[0].innerHTML=new Date().toLocaleTimeString()
},1000)