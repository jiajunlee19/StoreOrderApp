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

    const id = e.target.dataset.memberId;
    console.log(id)
    // postResponse(deleteMemberUrl, id);
})

