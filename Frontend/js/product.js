// Defining async function
async function getProduct(url) {
    
    showLoader('table-product-loader')

    // Storing response
    const response = await fetch(url);
   
    // Storing data in form of JSON
    let data = await response.json();
    console.log(data);

    if (response) {
        hideLoader('table-product-loader');
    }

    //showProductList
    let tBodyHTML = '';
    for (let i = 0; i <= data.length - 1; i++) {
        tBodyHTML += `
        <tr data-product-id = "" data-product-name = "" data-product-uom-id = "" data-product-unit-price = "" data-product-bonus-points = "">
            <td>${data[i]['product_name']}</td>
            <td>${data[i]['uom_id']}</td>
            <td>${data[i]['product_unit_price']}</td>
            <td>${data[i]['product_bonus_points']}</td>
            <td>
                <button>
                    delete
                </button>
            </td>
        </tr>
        `;
    }
    // Setting innerHTML as tab variable
    document.getElementById("table-product-body").innerHTML = tBodyHTML;
}


// Calling that async function
productList = getProduct(productListApiUrl);