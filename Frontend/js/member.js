// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getMemberUrl, 
    'table-member-loader', 
    ['member_id', 'member_name', 'member_bonus_points'], 
    'table-member-head', 'table-member-body'
    );