function changecolor(){
    // let btnref=document.getElementById('xyz')
    // console.log(btnref)
    // btnref.style.backgroundColor='yellow'
    document.getElementById('xyz').style.backgroundColor="yellow"

}
function changecolor1(){
    document.getElementsByTagName('button')[1].style.backgroundColor="green"

}
function changecolor2(){
    document.querySelector('.btn3').style.backgroundColor="orange"

} 
function changecolor3(){
    document.getElementsByClassName('btn')[0].style.backgroundColor="pink"
}
function changecolor4(x){
    x.style.backgroundColor="yellow"

}
function convertToUppercase(){
    let y=document.getElementById("input")
    y.value=y.value.toUpperCase();
}