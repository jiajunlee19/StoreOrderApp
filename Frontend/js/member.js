// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getMemberUrl, 
    'table-member-loader', 
    ['member_id', 'member_name', 'member_bonus_points'], 
    'table-member-head', 'table-member-body'
    );


//on click button-delete-row
document.addEventListener('click', function(e) {
    if (!e.target.matches('.button-delete-row')) {
        return;
    }

    const id = e.target.getAttribute('data-member-id');
    const id_json = {"id": id};
    console.log(id)

    const isDelete = confirm(`Are you sure to delete "${id}" ?`);

    if (isDelete) {
        postResponse(deleteMemberUrl, new URLSearchParams(id_json))
        this.location.reload()
    }
    
})

