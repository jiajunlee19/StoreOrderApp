// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, actionUrl, columnListAction
fetchResponseToTableBody(
    getMemberUrl, 
    'table-loader', 
    'table-head', 
    'table-body',
    ['member_id', 'member_name', 'member_bonus_points'], 
    deleteMemberUrl,
    ['member_id']
);

// set Insert HTML
setActionHTML(
    'insert',
    'insert', 
    insertMemberUrl, 
    {
        'member_name': 'text',
        'member_password': 'password',
        'member_bonus_points': 'number'
    },
    'Are you sure to add this new item ?'
);

// set update HTML
setActionHTML(
    'update',
    'update', 
    updateMemberUrl, 
    {   
        'member_id': 'hidden',
        'member_password': 'password',
        'member_bonus_points': 'number'
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