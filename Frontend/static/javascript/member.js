// Calling Fetch utils function
//arguments: fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, columnListDisplay, actionUrl, columnListAction
fetchResponseToTableBody(
    getMemberUrl, 
    'table-member-loader', 
    'table-member-head', 
    'table-member-body',
    ['member_id', 'member_name', 'member_bonus_points'], 
    deleteMemberUrl,
    ['member_id']
);

setInsertHTML(
    'insert-member', 
    insertMemberUrl, 
    {
        'member_name': 'text',
        'member_password': 'password',
        'member_bonus_points': 'number'
    }
);

// on click button-add-member
document.addEventListener('click', function(e) {
    if (!e.target.matches('.button-add-member')) {
        return;
    }

    showElement('insert-member');
    
})