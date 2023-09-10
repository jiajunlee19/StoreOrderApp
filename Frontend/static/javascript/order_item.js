// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, deleteUrl, columnListDelete, columnListUpdate
fetchResponseToTableBody(
    getOrderItemUrl, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['order_item_id', 'product_id', 'uom_id', 'order_item_quantity'], 
    deleteOrderItemUrl,
    ['order_item_id'],
    ['order_item_quantity']
);

// set Insert HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'insert',
    'insert', 
    insertOrderItemUrl, 
    {
        'product_id': 'text',
        'uom_id': 'text',
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
        'product_id': 'readonly',
        'uom_id': 'readonly',
        'order_item_quantity': 'number'
    },
    'Are you sure to update the selected item ?'
);


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