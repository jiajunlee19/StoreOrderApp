// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, deleteUrl, columnListDelete, columnListUpdate
fetchResponseToTableBody(
    getMemberLevelUrl, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['member_level_id', 'member_level', 'bonus_points_min', 'bonus_points_max'], 
    deleteMemberLevelUrl,
    ['member_level_id'],
    ['member_level_id', 'member_level']
);

// set Insert HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'insert',
    'insert', 
    insertMemberLevelUrl, 
    {
        'member_level': 'text',
        'bonus_points_min': 'number',
        'bonus_points_max': 'number'
    },
    'Are you sure to add this new item ?'
);

// set update HTML
// arguments: action, targetElementID, targetUrl, object, confirmMsg
setActionHTML(
    'update',
    'update', 
    updateMemberLevelUrl, 
    {   
        'member_level_id': 'readonly',
        'member_level': 'readonly',
        'bonus_points_min': 'number',
        'bonus_points_max': 'number'
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