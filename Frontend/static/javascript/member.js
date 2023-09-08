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
setInsertHTML(
    'insert', 
    insertMemberUrl, 
    {
        'member_name': 'text',
        'member_password': 'password',
        'member_bonus_points': 'number'
    }
);

// on click button-add
document.addEventListener('click', function(e) {
    if (!e.target.matches('.button-add')) {
        return;
    }

    if (document.getElementById('insert').style.display === 'none') {
        showElement('insert');
    }

    else {
        hideElement('insert');
    }
    
})


//on click button-submit-insert
// document.addEventListener('submit', function(e) {
//     if (!e.target.matches('.submit-insert')) {
//         return;
//     }

//     const data = new FormData(e.target);
//     const value = Object.fromEntries(data.entries());
//     console.log(value)
    
// })

//on click button-delete-row
// document.addEventListener('click', function(e) {
//     if (!e.target.matches('.button-delete-row')) {
//         return;
//     }

//     const id = e.target.getAttribute('data-member-id');
//     const id_json = {"id": id};
//     console.log(id)

//     const isDelete = confirm(`Are you sure to delete "${id}" ?`);

//     if (isDelete) {
//         postResponse(deleteMemberUrl, new URLSearchParams(id_json))
//         this.location.reload()
//     }
    
// })