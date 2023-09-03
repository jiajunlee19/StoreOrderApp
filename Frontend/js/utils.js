// Define your api here
const productListApiUrl = 'http://127.0.0.1:5000/getProduct';
const uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
const productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
const productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
const orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
const orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// Function to show/hide the loader
function hideLoader(elementID) {
    document.getElementById(elementID).style.display = 'none';
};

function showLoader(elementID) {
    document.getElementById(elementID).style.display = 'block';
}