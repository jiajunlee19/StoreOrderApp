// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getUOMUrl, 
    'table-uom-loader', 
    ['uom_id', 'uom_name'], 
    'table-uom-head', 'table-uom-body'
    );