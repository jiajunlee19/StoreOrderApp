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