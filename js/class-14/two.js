function products(products){
    let rows=" "
    for(let product of products){
          rows=rows+`<tr>
                        <td>${product.id}</td>
                        <td>${product.title}</td>
                        <td>${product.category}</td>
                        <td>${product.price}</td>
                    </tr>`
    }
    document.getElementById('one').innerHTML=rows;
}
fetch('https://dummyjson.com/products')
  .then((response) => response.json())
  .then((json) => products(json.products));