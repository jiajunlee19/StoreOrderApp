// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, deleteUrl, columnListDelete, columnListUpdate
fetchResponseToTableBody(
    getProductUrl, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['product_name', 'uom_name', 'product_unit_price', 'product_bonus_points'], 
    deleteProductUrl,
    ['product_id'],
    ['product_id', 'product_name', 'uom_id', 'uom_name']
);

// set Insert HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'insert',
    'insert', 
    insertProductUrl, 
    {
        'product_name': 'text',
        'uom_id': 'hidden',
        'uom_name': 'select',
        'product_unit_price': 'number',
        'product_bonus_points': 'number'
    },
    'Are you sure to add this new item ?'
);

// set update HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'update',
    'update', 
    updateProductUrl, 
    {   
        'product_id': 'hidden',
        'product_name': 'readonly',
        'uom_id': 'hidden',
        'uom_name': 'readonly',
        'product_unit_price': 'number',
        'product_bonus_points': 'number'
    },
    'Are you sure to update the selected item ?'
);


fetchResponseToDropDown(
    getUOMUrl, 
    ['uom_id', 'uom_name'], 
    'insert',
    'uom_name',
    {'uom_name': 'uom_id'}
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