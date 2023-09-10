// Define your api urls here
const mainUrl = 'http://127.0.0.1:5000';

const getMemberUrl = `${mainUrl}/getMember`;
const getMemberLevelUrl = `${mainUrl}/getMemberLevel`;
const getUOMUrl = `${mainUrl}/getUOM`;
const getProductUrl = `${mainUrl}/getProduct`;
const getOrderUrl = `${mainUrl}/getOrder`;
const getOrderItemUrl = `${mainUrl}/getOrderItem`;

const insertMemberUrl =`${mainUrl}/insertMember`;
const insertMemberLevelUrl =`${mainUrl}/insertMemberLevel`;
const insertUOMUrl =`${mainUrl}/insertUOM`;
const insertProductUrl =`${mainUrl}/insertProduct`;
const insertOrderUrl =`${mainUrl}/insertOrder`;
const insertOrderItemUrl =`${mainUrl}/insertOrderItem`;

const deleteMemberUrl =`${mainUrl}/deleteMember`;
const deleteMemberLevelUrl =`${mainUrl}/deleteMemberLevel`;
const deleteUOMUrl =`${mainUrl}/deleteUOMr`;
const deleteProductUrl =`${mainUrl}/deleteProduct`;
const deleteOrderUrl =`${mainUrl}/deleteOrder`;
const deleteOrderItemUrl =`${mainUrl}/deleteOrderItem`;

const updateMemberUrl =`${mainUrl}/updateMember`;
const updateMemberLevelUrl =`${mainUrl}/updateMemberLevel`;
const updateUOMUrl =`${mainUrl}/updateUOM`;
const updateProductUrl =`${mainUrl}/updateProduct`;
const updateOrderUrl =`${mainUrl}/updateOrder`;
const updateOrderItemUrl =`${mainUrl}/updateOrderItem`;


//Function to convert HTML collection into Array
function collectionToArray(collection){
    var i, length = collection.length,
    array = [];
    for (i = 0;i< length;i++){
        array.push(collection[i]);
    }
    return array;
};

// Function to hide the Element
function hideElement(elementID) {
    document.getElementById(elementID).style.display = 'none';
};

// Function to show the Element
function showElement(elementID) {
    document.getElementById(elementID).style.display = 'block';
};


// Defining async function to fetch response only
async function fetchResponse(fetchUrl) {
    const response = await fetch(fetchUrl);
    let data = await response.json();

    if (response) {
        return data;
    }
};

// Defining async function to fetch response, hide loader once loaded, update table HTML
async function fetchResponseToTableBody(fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, 
    columnListDisplay, deleteUrl, columnListDelete, columnListUpdate, addViewButtonFlag = false) {
    
    //show loader until a response is fetched
    showElement(loaderElementID);

    // Fetch response
    const response = await fetch(fetchUrl);
   
    // Storing data in form of JSON
    let data = await response.json();
    // console.log(data); 
    // console.log(typeof data) 

    //if response fetched, hide the loader
    if (response) {
        hideElement(loaderElementID);
    }

    //Initialize table HTML
    let tHeadHTML = '';
    let tBodyHTML = '';

    if (addViewButtonFlag) {
        tHeadHTML = '<th>Order Detail</th>';
    }


    //for each row object, generate table body HTML
    data.forEach((object, i) => {

        //Generate data attribute for table body HTML
        let trAttrList = [];
        let trAttr = '';
        Object.keys(object).forEach(key => {
            trAttrList.push(`data-${key} = "${object[key]}"`)
        });
        trAttr = `id="row-${i}" ${trAttrList.join(' ')}`

        // filter only object with keys defined in columnListDisplay to show in final table
        let objectDisplay = object
       if (columnListDisplay && columnListDisplay.length > 0) {
            objectDisplay = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListDisplay.includes(key)))
       };

        //for 1st row object, generate table header HTML
        if (i === 0) {
            let th ="";
            Object.keys(objectDisplay).forEach(key => {
                th += `<th>${key}</th>`;
            });
            tHeadHTML += `
                ${th}
                <th>Action</th>
            `;
        };


        //Generate strings for table body HTML
        let td = '';
        Object.keys(objectDisplay).forEach(key => {
            td += `<td>${objectDisplay[key]}</td>`;
        });

        
        // filter only object with keys defined in columnListDelete
        let objectDelete = object
        if (columnListDelete && columnListDelete.length > 0) {
            objectDelete = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListDelete.includes(key)))
        }

        //for each key in objectDelete, create one line of <input> form
        let inputFormDelete = '';
        Object.keys(objectDelete).forEach(key => {
            inputFormDelete += `<input type="hidden" id="${key}" name="${key}" value="${objectDelete[key]}" required>`
        });  


        // filter only object with keys defined in columnListUpdate
        let objectUpdate = object
        if (columnListUpdate && columnListUpdate.length > 0) {
            objectUpdate = Object.fromEntries(Object.entries(object).filter( ([key,val]) => columnListUpdate.includes(key)))
        }

        //for each key in objectUpdate, editButtonOnClick replace placeholder & value text
        // document.getElementById('update-member_id').innerHTML = 'member_id: ' + document.getElementById('row-${i}').getAttribute('data-member_id');
        let editButtonOnClick = '';
        Object.keys(objectUpdate).forEach(key => {
            editButtonOnClick += `
                document.getElementById('update-${key}-placeholder').value = document.getElementById('row-${i}').getAttribute('data-${key}');
            `;
        }); 
        

        //show view button in column1
        tdView = '';
        if (addViewButtonFlag) {
            tdView = `
                <td>
                    <button class="button-view-order" onclick="
                        clickedOrder = document.getElementById('row-${i}').getAttribute('data-order_id');
                        location = '${mainUrl}/orderItem/' + clickedOrder;
                    ">
                        view
                    </button>
                </td>
            `
        };

        //Finalizing tableHTML
        tBodyHTML += `
            <tr ${trAttr}>
                ${tdView}
                ${td}
                <td>
                    <button onclick="${editButtonOnClick}">edit</button>
                    <form action="${deleteUrl}" method="post">
                        ${inputFormDelete}
                        <input type="submit" value="delete" onclick="return confirm('Are you sure to delete this item?')">
                    </form>
                </td>
            </tr>
        `;

    });


    // Update table innerHTML
    document.getElementById(tableHeadElementID).innerHTML = tHeadHTML;
    document.getElementById(tableBodyElementID).innerHTML = tBodyHTML;

    return data

};



// Function to set action HTML (insert/update)
function setActionHTML(action, targetElementID, targetUrl, object, confirmMsg) {

    let HTML = '';
    Object.keys(object).forEach(key => {
        
        if (object[key] === 'readonly') {
            HTML += `
                <label id="${action}-${key}" name="${key}">${key}: </label>
                <input type="text" id="${action}-${key}-placeholder" name="${key}" placeholder="placeholder" required readonly><br>
            `;
        }

        else if (object[key] === 'hidden') {
            HTML += `
                <input type="hidden" id="${action}-${key}-placeholder" name="${key}" placeholder="placeholder" required readonly>
            `;
        }  
        
        else if (object[key] === 'number') {
            HTML += `
                <label id="${action}-${key}" name="${key}">${key}: </label>
                <input type="${object[key]}" step=any id="${action}-${key}" name="${key}" required><br>
            `;
        }        

        else if (object[key] === 'select') {
            HTML += `
                <label id="${action}-${key}" name="${key}">${key}: </label>
                <select id="${action}-${key}-select" name="${key}" required>
                    <option value="placeholder">placeholder</option>
                </select><br>
            `;
        }       

        else {
            HTML += `
                <label id="${action}-${key}" name="${key}">${key}: </label>
                <input type="${object[key]}" id="${action}-${key}" name="${key}" required><br>
            `;
        }
    });

    onClickSubmitMsg = ''
    if (confirmMsg && confirmMsg.length > 0) {
        onClickSubmitMsg = `onclick="return confirm('${confirmMsg}')"`
    }

    document.getElementById(`${targetElementID}`).innerHTML = `
        <form action="${targetUrl}" method="post">
            ${HTML}
            <input type="submit" value="submit & ${action}" ${onClickSubmitMsg}>
        </form>
    `;

    hideElement(targetElementID);

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
