// Calling Fetch utils function, arguments: url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID
fetchResponseToTableBody(
    getProductUrl, 
    'table-product-loader', 
    ['product_name', 'uom_name', 'product_unit_price', 'product_bonus_points'], 
    'table-product-head', 'table-product-body'
    );