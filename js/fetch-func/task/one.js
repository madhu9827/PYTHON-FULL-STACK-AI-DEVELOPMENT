let display_Products=()=>{
    fetch('https://dummyjson.com/products')
    .then((resp)=>{return resp.json()})
    .then((product_data)=>{
        let rows="";
        for(let product of product_data.products){
            rows=rows+`<tr>
                        <td>${product.id}</td>
                        <td>${product.title}</td>
                        <td>${product.price}</td>
                        <td>${product.category}</td>
                        </tr>`
        }
    document.getElementsByTagName('tbody')[0].innerHTML=rows
})
.catch((err)=>{
    document.getElementsByTagName('tbody')[0].innerHTML="no data";
})
}
display_Products()