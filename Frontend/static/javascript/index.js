// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, deleteUrl, columnListDelete, columnListUpdate
fetchResponseToTableBody(
    getOrderUrl, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['order_id', 'order_created_date', 'member_name'], 
    deleteOrderUrl,
    ['order_id'],
    ['order_id', 'member_id','member_name'],
    true
);

// set Insert HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'insert',
    'insert', 
    insertOrderUrl, 
    {
        'member_id': 'hidden',
        'member_name': 'select'
    },
    'Are you sure to add this new item ?'
);

// set update HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'update',
    'update', 
    updateOrderUrl,
    {   
        'order_id': 'readonly',
        'member_id': 'hidden',
        'member_name': 'readonly'
    },
    'Are you sure to update the selected item ?'
);


// set dropdown options
//arguments: fetchUrl, columnListFilter, action, primaryKey, objectDropDown
fetchResponseToDropDown(
    getMemberUrl, 
    ['member_id', 'member_name'], 
    'insert',
    'member_name',
    {'member_name': 'member_id'}
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