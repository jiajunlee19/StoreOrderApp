// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getMemberLevelUrl, 
    'table-memberLevel-loader', 
    ['member_level_id', 'member_level', 'bonus_points_min', 'bonus_points_max'], 
    'table-memberLevel-head', 'table-memberLevel-body'
    );