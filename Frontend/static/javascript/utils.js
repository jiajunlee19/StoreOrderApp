// Define your api urls here
const mainUrl = 'http://127.0.0.1:5000';

const getMemberUrl = `${mainUrl}/getMember`;
const getMemberLevelUrl = `${mainUrl}/getMemberLevel`;
const getUOMUrl = `${mainUrl}/getUOM`;
const getProductUrl = `${mainUrl}/getProduct`;
const getOrderUrl = `${mainUrl}/getOrder`;

const insertMemberUrl =`${mainUrl}/insertMember`;

const deleteMemberUrl =`${mainUrl}/deleteMember`;

const updateMemberUrl =`${mainUrl}/updateMember`;

const productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
const productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';

const orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';


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


// Defining async function to fetch response function, hide loader once loaded, update table HTML
async function fetchResponseToTableBody(fetchUrl, loaderElementID, tableHeadElementID, tableBodyElementID, 
    columnListDisplay, deleteUrl, columnListDelete) {
    
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


    //for each row object, generate table body HTML
    data.forEach((object, i) => {

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
            tHeadHTML = `
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
        Object.keys(objectDelete).forEach((key, i) => {
            inputFormDelete += `<input type="hidden" id="${key}" name="${key}" value="${objectDelete[key]}" required>`
        });  
        

        //Finalizing tableHTML
        tBodyHTML += `
            <tr>
                ${td}
                <td>
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



    // update
    let table = document.getElementById('table-body')

    for (let i = 0; i < table.rows.length; i++) {
        console.log(table.rows[i])
        table.rows[i].onclick = function () {
            rIndex = this.rowIndex;
            console.log(rIndex)

            document.getElementById('a').value = this.cells[0].innerHTML;

            table.rows[rIndex].cells[0].innerHTML = document.getElementById('a').value;
        }
    }
};



// Function to set action HTML (insert/update)
function setActionHTML(action, targetElementID, targetUrl, object, confirmMsg) {

    let HTML = '';
    Object.keys(object).forEach(key => {
        
        if (object[key] === 'hidden') {
            HTML += `
                <input type="${object[key]}" id="${action}-${key}" name="${key}" required>
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




//on click button-submit-insert
// document.addEventListener('submit', function(e) {
//     if (!e.target.matches('.submit-insert')) {
//         return;
//     }

//     const data = new FormData(e.target);
//     const value = Object.fromEntries(data.entries());
//     console.log(value)
    
// })

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
