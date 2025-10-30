function display(){
    let cdt=new Date().toLocaleString();
    console.log(cdt)
    let ptag_ref=document.getElementById('xyz')
    console.log(ptag_ref)
    ptag_ref.innerHTML=cdt;
}
//instead of this we will write one line of code
document.getElementById('xyz').innerHTML=new Date().toLocaleString()