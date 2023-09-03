// Define your api urls here
const mainUrl = 'http://127.0.0.1:5000';

const getMemberUrl = `${mainUrl}/getMember`;
const getMemberLevelUrl = `${mainUrl}/getMemberLevel`;
const getUOMUrl = `${mainUrl}/getUOM`;
const getProductUrl = `${mainUrl}/getProduct`;
const getOrderUrl = `${mainUrl}/getOrder`;

const productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
const productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';

const orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// Function to hide the loader
function hideLoader(elementID) {
    document.getElementById(elementID).style.display = 'none';
};

// Function to show the loader
function showLoader(elementID) {
    document.getElementById(elementID).style.display = 'block';
}

// Defining async function to fetch response function, hide loader once loaded, update table HTML
async function fetchResponseToTableBody(url, loaderElementID, columnList, tableHeadElementID, tableBodyElementID) {
    
    showLoader(loaderElementID)

    // Storing response
    const response = await fetch(url);
   
    // Storing data in form of JSON
    let data = await response.json();
    console.log(data); //data is a list of objects

    if (response) {
        hideLoader(loaderElementID);
    }

    // Generate table HTMLs
    let tHeadHTML = '';
    let tBodyHTML = '';

    data.forEach(object => {
        // filter only object with keys defined in columnList
        /*
        const objectFiltered = Object.keys(object).filter(key => columnList.includes(key)).reduce((obj, key) => {
            obj[key] = object[key];
            return obj
        }, {});
        */
       if (columnList && columnList.length > 0) {
            object = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnList.includes(key)))
       }
        // console.log(object)

        //Form lists based on object keys
        let headerList = [];
        let dataList = [];
        let valueList = [];
        Object.keys(object).forEach(key => {
            header = `<th>${key}</th>`;
            headerList.push(header)

            data = `data-${key.replace('_','-')} = "${object[key]}"`;
            dataList.push(data);

            value = `<td>${object[key]}</td>`;
            valueList.push(value);
        });

        //join lists into strings
        th = headerList.join('');
        trAttr = dataList.join(' ');
        td = valueList.join('');

        tHeadHTML += `
            ${th}
            <th>Action</th>
        `;

        tBodyHTML += `
            <tr ${trAttr}>
                ${td}
                <td>
                    <button>
                        delete
                    </button>
                </td>
            </tr>
        `;

    });

    // Update table innerHTML
    document.getElementById(tableHeadElementID).innerHTML = tHeadHTML;
    document.getElementById(tableBodyElementID).innerHTML = tBodyHTML;
}

