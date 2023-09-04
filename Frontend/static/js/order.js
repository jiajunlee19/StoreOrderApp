// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getOrderUrl, 
    'table-order-loader', 
    ['order_id', 'order_created_date', 'member_id'], 
    'table-order-head', 'table-order-body'
    );