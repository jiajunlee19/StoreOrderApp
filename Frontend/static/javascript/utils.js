// Define your api urls here
const mainUrl = 'http://127.0.0.1:5000';

const getMemberUrl = `${mainUrl}/getMember`;
const getMemberLevelUrl = `${mainUrl}/getMemberLevel`;
const getUOMUrl = `${mainUrl}/getUOM`;
const getProductUrl = `${mainUrl}/getProduct`;
const getOrderUrl = `${mainUrl}/getOrder`;

const insertMemberUrl =`${mainUrl}/insertMember`;

const deleteMemberUrl =`${mainUrl}/deleteMember`;

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
};


// Defining async function to fetch response function, hide loader once loaded, update table HTML
async function fetchResponseToTableBody(fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, 
    columnListDisplay, actionUrl, columnListAction) {
    
    //show loader until a response is fetched
    showLoader(loaderElementID)

    // Fetch response
    const response = await fetch(fetchUrl);
   
    // Storing data in form of JSON
    let data = await response.json();
    console.log(data); //data is a list of objects

    //if response fetched, hide the loader
    if (response) {
        hideLoader(loaderElementID);
    }

    //Initialize table HTML
    let tHeadHTML = '';
    let tBodyHTML = '';

    //for each object (a.k.a each row object)
    data.forEach(object => {

        // filter only object with keys defined in columnListDisplay to show in final table
       if (columnListDisplay && columnListDisplay.length > 0) {
            objectDisplay = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListDisplay.includes(key)))
       }

        //Form lists based on filteredObject keys
        let headerList = [];
        let dataAttrList = [];
        let valueList = [];
        Object.keys(objectDisplay).forEach(key => {
            header = `<th>${key}</th>`;
            headerList.push(header)

            dataAttr = `data-${key.replace('_','-')} = "${objectDisplay[key]}"`;
            dataAttrList.push(dataAttr);

            value = `<td>${objectDisplay[key]}</td>`;
            valueList.push(value);
        });
        th = headerList.join('');
        trAttr = dataAttrList.join(' ');
        td = valueList.join('');

        
        // filter only object with keys defined in columnListAction to do update or delete
        if (columnListAction && columnListAction.length > 0) {
            objectAction = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListAction.includes(key)))
        }

        //for each key in object, create one line of <input> form
        let formInputList = [];
        Object.keys(objectAction).forEach(key => {
            formInput = `<input type="hidden" id="${key}" name="${key}" value="${objectAction[key]}"></input>`
            formInputList.push(formInput)
        });
        inputs = formInputList.join('');       


        //Finalizing tableHTML
        tHeadHTML += `
            ${th}
            <th>Action</th>
        `;

        tBodyHTML += `
            <tr ${trAttr}>
                ${td}
                <td>
                    <form action="${actionUrl}" method="post">
                        ${inputs}
                        <input type="submit" value="delete" onclick="return confirm('Are you sure to delete ?')">
                    </form>
                </td>
            </tr>
        `;

    });


    // Update table innerHTML
    document.getElementById(tableHeadElementID).innerHTML = tHeadHTML;
    document.getElementById(tableBodyElementID).innerHTML = tBodyHTML;
};


//on click button-delete-row
// document.addEventListener('click', function(e) {
//     if (!e.target.matches('.button-delete-row')) {
//         return;
//     }

//     const id = e.target.getAttribute('data-member-id');
//     const id_json = {"id": id};
//     console.log(id)

//     const isDelete = confirm(`Are you sure to delete "${id}" ?`);

//     if (isDelete) {
//         postResponse(deleteMemberUrl, new URLSearchParams(id_json))
//         this.location.reload()
//     }
    
// })