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


//Function to fetch data and assign dropdown options with relevant UID pair
async function fetchUOM(fetchUrl, columnListFilter, primaryKey, objectDropDown) {
    data = await fetchResponse(fetchUrl);

    //
    let dataFull = {};
    let optionDropDown = {};
    data.forEach(object => {
        
        let objectFilter = object
        if (columnListFilter && columnListFilter.length > 0) {
            objectFilter = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListFilter.includes(key)))
        };

        dataFull[objectFilter[primaryKey]] = objectFilter

        Object.keys(objectDropDown).forEach(e => {
            optionDropDown[e] += `<option value="${objectFilter[e]}">${objectFilter[e]}</option>`
        });

    });

    //for each drop-down column, change select dropdown options accordinly based on optionDropDown dict
    Object.keys(optionDropDown).forEach(key => {

        document.getElementById(`insert-${key}-select`).innerHTML = optionDropDown[key];

        document.getElementById(`insert-${key}-select`).addEventListener('change', function() {

            document.getElementById(`insert-${objectDropDown[key]}-placeholder`).value = dataFull[this.value][objectDropDown[key]]

        });

    }); 

};

fetchUOM(
    getUOMUrl, 
    ['uom_id', 'uom_name'], 
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