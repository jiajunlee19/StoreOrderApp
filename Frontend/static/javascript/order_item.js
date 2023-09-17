// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, deleteUrl, columnListDelete, columnListUpdate
fetchResponseToTableBody(
    getOrderItemUrl + "/" + clickedOrder, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['order_item_id', 'product_name', 'uom_name', 'order_item_quantity'], 
    deleteOrderItemUrl,
    ['order_item_id', 'order_id'],
    ['order_item_id', 'product_id', 'product_name', 'uom_id', 'uom_name']
);

// set Insert HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'insert',
    'insert', 
    insertOrderItemUrl, 
    {
        'order_id': 'readonly',
        'product_id': 'readonly',
        'product_name': 'select',
        'uom_id': 'readonly',
        'uom_name': 'select',
        'order_item_quantity': 'number'
    },
    'Are you sure to add this new item ?'
);

// set update HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'update',
    'update', 
    updateOrderItemUrl, 
    {   
        'order_item_id': 'readonly',
        'order_id': 'readonly',
        'product_id': 'hidden',
        'product_name': 'readonly',
        'uom_id': 'hidden',
        'uom_name': 'readonly',
        'order_item_quantity': 'number'
    },
    'Are you sure to update the selected item ?'
);

//Change h2 into order_id
document.querySelector('.h2').innerHTML = `
    Viewing Order: ${clickedOrder}
`;


// set dropdown options
// arguments: fetchUrl, columnListFilter, action, dropDownID, updateID, primaryKeyList
fetchResponseToDropDown2(
    getProductUrl, 
    ['product_id', 'product_name'], 
    'insert',
    'product_name',
    ['product_id'],
    ['product_name']
);




//change order_id to current_order_id
document.getElementById('insert-order_id-placeholder').value = clickedOrder
// document.getElementById('update-order_id-placeholder').value = clickedOrder
// console.log(document.getElementById('insert-order_id-placeholder').value)


// on click Events
document.addEventListener('click', function(e) {

    //button-add
    if (e.target.matches('.button-add')) {

        if (document.getElementById('insert').style.display === 'none') {
            showElement('insert');
        }
        else {
            hideElement('insert');
        }
    }

    //button-update
    else if (e.target.matches('.button-update')) {

        if (document.getElementById('update').style.display === 'none') {
            showElement('update');
        }
        else {
            hideElement('update');
        }
    }  

    else {
        return;
    } 
});